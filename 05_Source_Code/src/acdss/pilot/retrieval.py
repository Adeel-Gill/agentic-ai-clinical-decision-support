"""Timestamp-aware retrieval over patient timelines (memory-layer 'retrieval' operation).

Retrieval never returns an event recorded after the query time, so the
evidence set reflects what was knowable at decision time. Scoring combines
recency, abnormality, and event-type weights; every returned item carries its
provenance reference.
"""
from __future__ import annotations

import math
import time

import pandas as pd

from .timeline import Timeline

TYPE_WEIGHT = {"vital": 1.0, "lab": 1.0, "med": 0.6, "prior_admission": 0.8}

# Deterioration-relevant abnormality rules (SIRS/qSOFA-adjacent thresholds).
ABNORMAL_RULES = {
    "heart_rate": lambda v: v is not None and v > 100,
    "sbp_ni": lambda v: v is not None and v < 90,
    "map_arterial": lambda v: v is not None and v < 65,
    "resp_rate": lambda v: v is not None and v > 22,
    "temp_c": lambda v: v is not None and (v > 38.0 or v < 36.0),
    "temp_f": lambda v: v is not None and (v > 100.4 or v < 96.8),
    "spo2": lambda v: v is not None and v < 92,
    "wbc": lambda v: v is not None and (v > 12 or v < 4),
    "lactate": lambda v: v is not None and v > 2.0,
    "creatinine": lambda v: v is not None and v > 1.5,
    "bilirubin_total": lambda v: v is not None and v > 2.0,
    "platelets": lambda v: v is not None and v < 100,
}


def is_deterioration_evidence(etype: str, label: str, value, lab_flag) -> bool:
    """True when the observation supports a deterioration signal."""
    rule = ABNORMAL_RULES.get(label)
    if rule is not None:
        try:
            return rule(float(value)) if value is not None and not pd.isna(value) else False
        except (TypeError, ValueError):
            return False
    if etype == "lab":
        return bool(lab_flag)
    return False


def retrieve(tl: Timeline, query_time: pd.Timestamp, k: int = 10,
             lookback_hours: float = 48.0, intent: str = "current_state") -> pd.DataFrame:
    """Top-k evidence for a decision at `query_time`.

    intent='current_state'  -> recency-weighted snapshot of vitals/labs/meds
    intent='abnormal'       -> only deterioration-relevant abnormal observations
    """
    ev = tl.events
    in_window = (query_time - ev.t) <= pd.Timedelta(hours=lookback_hours)
    window = ev[(ev.t <= query_time) & (in_window | (ev.etype == "prior_admission"))].copy()
    if window.empty:
        return window

    age_h = (query_time - window.t).dt.total_seconds() / 3600.0
    recency = age_h.map(lambda h: math.exp(-h / 12.0))
    abnormal = window.apply(
        lambda r: is_deterioration_evidence(r.etype, r.label, r.value, r.abnormal), axis=1)
    window["deterioration_evidence"] = abnormal
    window["score"] = (recency
                       * window.etype.map(TYPE_WEIGHT).fillna(0.5)
                       * (1.5 if intent == "abnormal" else 1.0) ** abnormal.astype(int))
    if intent == "abnormal":
        window = window[abnormal]
    return window.sort_values("score", ascending=False).head(k)


def retrieval_metrics(timelines: dict[int, Timeline], at_hours: float = 24.0, k: int = 10) -> dict:
    """Feasibility metrics for retrieval at a fixed decision point."""
    latencies, coverage, abnormal_precision = [], 0, []
    for tl in timelines.values():
        qt = tl.intime + pd.Timedelta(hours=at_hours)
        t0 = time.perf_counter()
        res = retrieve(tl, qt, k=k, intent="current_state")
        latencies.append((time.perf_counter() - t0) * 1000)
        if len(res) >= k:
            coverage += 1
        res_ab = retrieve(tl, qt, k=k, intent="abnormal")
        if len(res_ab):
            abnormal_precision.append(res_ab.label.nunique())
    lat = pd.Series(latencies)
    distinct = pd.Series(abnormal_precision)
    return {
        "query_time_hours_after_icu_admission": at_hours,
        "k": k,
        "latency_ms": {"median": round(float(lat.median()), 2),
                        "p95": round(float(lat.quantile(0.95)), 2)},
        "coverage_full_k": round(coverage / len(timelines), 4),
        "stays_with_any_abnormal_evidence": len(abnormal_precision),
        "distinct_abnormal_signals_per_stay": {
            "median": float(distinct.median()) if len(distinct) else None,
            "p25": float(distinct.quantile(0.25)) if len(distinct) else None,
            "p75": float(distinct.quantile(0.75)) if len(distinct) else None,
        },
    }
