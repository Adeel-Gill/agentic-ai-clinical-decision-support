"""Patient-timeline construction (memory-layer 'construction' operation).

Builds one chronological event stream per ICU stay from the MIMIC-IV demo
tables. Every event keeps a provenance reference (source table + row index)
so downstream components can be audited back to the raw record.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

# Routine vital signs in icu/chartevents (MIMIC-IV metavision itemids).
VITAL_ITEMS = {
    220045: "heart_rate",
    220179: "sbp_ni",
    220180: "dbp_ni",
    220052: "map_arterial",
    220210: "resp_rate",
    223761: "temp_f",
    223762: "temp_c",
    220277: "spo2",
}

# Lab labels used by the baseline and the verification gate (matched on
# lower-cased d_labitems label).
LAB_LABELS = {
    "white blood cells": "wbc",
    "lactate": "lactate",
    "creatinine": "creatinine",
    "bilirubin, total": "bilirubin_total",
    "platelet count": "platelets",
}


@dataclass
class Timeline:
    subject_id: int
    hadm_id: int
    stay_id: int
    intime: pd.Timestamp
    outtime: pd.Timestamp
    hospital_expire_flag: int
    anchor_age: int
    gender: str
    events: pd.DataFrame = field(repr=False)  # t, etype, code, label, value, unit, abnormal, source, source_row


def _load(base: Path, rel: str, **kw) -> pd.DataFrame:
    return pd.read_csv(base / rel, **kw)


def build_timelines(demo_root: str | Path) -> tuple[dict[int, Timeline], dict]:
    """Return (stay_id -> Timeline, construction metrics)."""
    base = Path(demo_root)
    t0 = time.perf_counter()

    patients = _load(base, "hosp/patients.csv.gz")
    admissions = _load(base, "hosp/admissions.csv.gz", parse_dates=["admittime", "dischtime"])
    icustays = _load(base, "icu/icustays.csv.gz", parse_dates=["intime", "outtime"])

    d_labitems = _load(base, "hosp/d_labitems.csv.gz")
    lab_map = {
        row.itemid: LAB_LABELS[row.label.lower()]
        for row in d_labitems.itertuples()
        if isinstance(row.label, str) and row.label.lower() in LAB_LABELS
    }

    labevents = _load(
        base, "hosp/labevents.csv.gz", parse_dates=["charttime"],
        usecols=["subject_id", "hadm_id", "itemid", "charttime", "valuenum", "valueuom", "flag"],
    )
    chartevents = _load(
        base, "icu/chartevents.csv.gz", parse_dates=["charttime"],
        usecols=["subject_id", "hadm_id", "stay_id", "itemid", "charttime", "valuenum", "valueuom"],
    )
    prescriptions = _load(
        base, "hosp/prescriptions.csv.gz", parse_dates=["starttime"],
        usecols=["subject_id", "hadm_id", "starttime", "drug"],
    )

    vitals = chartevents[chartevents.itemid.isin(VITAL_ITEMS)].copy()
    vitals["label"] = vitals.itemid.map(VITAL_ITEMS)

    labs = labevents[labevents.itemid.isin(lab_map)].copy()
    labs["label"] = labs.itemid.map(lab_map)

    timelines: dict[int, Timeline] = {}
    demo = patients.set_index("subject_id")
    adm_ix = admissions.set_index("hadm_id")

    for stay in icustays.itertuples():
        rows = []
        # Vitals within the stay.
        v = vitals[vitals.stay_id == stay.stay_id]
        for r in v.itertuples():
            rows.append((r.charttime, "vital", r.label, r.valuenum, r.valueuom, None, "icu/chartevents", r.Index))
        # Labs for the same hospital admission.
        l = labs[labs.hadm_id == stay.hadm_id]
        for r in l.itertuples():
            rows.append((r.charttime, "lab", r.label, r.valuenum, r.valueuom,
                         (r.flag == "abnormal") if isinstance(r.flag, str) else False,
                         "hosp/labevents", r.Index))
        # Medication starts for the admission.
        p = prescriptions[prescriptions.hadm_id == stay.hadm_id]
        for r in p.itertuples():
            rows.append((r.starttime, "med", str(r.drug).lower(), None, None, None, "hosp/prescriptions", r.Index))
        # Prior admissions (strictly before this admission) — longitudinal context.
        this_adm = adm_ix.loc[stay.hadm_id]
        prior = admissions[(admissions.subject_id == stay.subject_id)
                           & (admissions.dischtime < this_adm.admittime)]
        for r in prior.itertuples():
            rows.append((r.dischtime, "prior_admission", r.admission_type, None, None, None, "hosp/admissions", r.Index))

        ev = pd.DataFrame(rows, columns=["t", "etype", "label", "value", "unit", "abnormal", "source", "source_row"])
        ev = ev.dropna(subset=["t"]).sort_values("t").reset_index(drop=True)
        timelines[stay.stay_id] = Timeline(
            subject_id=stay.subject_id, hadm_id=stay.hadm_id, stay_id=stay.stay_id,
            intime=stay.intime, outtime=stay.outtime,
            hospital_expire_flag=int(this_adm.hospital_expire_flag),
            anchor_age=int(demo.loc[stay.subject_id, "anchor_age"]),
            gender=str(demo.loc[stay.subject_id, "gender"]),
            events=ev,
        )

    elapsed = time.perf_counter() - t0
    sizes = pd.Series({sid: len(t.events) for sid, t in timelines.items()})
    metrics = {
        "n_stays": len(timelines),
        "construction_seconds_total": round(elapsed, 2),
        "events_per_stay": {
            "median": float(sizes.median()),
            "p25": float(sizes.quantile(0.25)),
            "p75": float(sizes.quantile(0.75)),
            "min": int(sizes.min()),
            "max": int(sizes.max()),
        },
        "event_type_share": (
            pd.concat([t.events.etype for t in timelines.values()])
            .value_counts(normalize=True).round(4).to_dict()
        ),
        "stays_with_prior_admission": int(sum(
            (t.events.etype == "prior_admission").any() for t in timelines.values()
        )),
    }
    return timelines, metrics
