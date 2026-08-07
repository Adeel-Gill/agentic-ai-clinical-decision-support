"""Rule-based verification gate + evidence-linked audit trail (pilot version).

The gate receives an alert (stay_id, risk score) and passes it to the
clinician queue only when the patient's own timeline, retrieved at decision
time, contains at least `min_signals` DISTINCT deterioration-relevant
signals (e.g. tachycardia + elevated lactate) recorded within the last
`evidence_window_hours` before the decision. Requiring distinct recent
signals rather than raw abnormal counts is what makes the gate informative:
an ICU record almost always contains some abnormal value in 48 h, but a
concordant multi-signal picture close to decision time is rarer.

Every decision is logged with resolvable provenance references, and the
trail's resolvability is measured afterwards rather than assumed — the
pilot analogue of the framework's audit-trail-faithfulness metric.
"""
from __future__ import annotations

import pandas as pd

from .retrieval import retrieve
from .timeline import Timeline


def _evidence(tl: Timeline, at_hours: float, evidence_window_hours: float, k: int) -> pd.DataFrame:
    qt = tl.intime + pd.Timedelta(hours=at_hours)
    ev = retrieve(tl, qt, k=k, lookback_hours=evidence_window_hours, intent="abnormal")
    return ev[ev.etype.isin(["vital", "lab"])]


def run_gate(timelines: dict[int, Timeline], alerts: pd.DataFrame,
             at_hours: float = 24.0, min_signals: int = 3,
             evidence_window_hours: float = 6.0, k: int = 50) -> tuple[pd.DataFrame, list[dict], dict]:
    """Apply the gate to every alert. Returns (decisions, audit_trail, metrics)."""
    decisions, trail = [], []
    for row in alerts[alerts.alert].itertuples():
        tl = timelines[row.stay_id]
        evidence = _evidence(tl, at_hours, evidence_window_hours, k)
        n_signals = int(evidence.label.nunique())
        passed = n_signals >= min_signals
        refs = [
            {"source": e.source, "source_row": int(e.source_row),
             "t": str(e.t), "label": e.label,
             "value": None if pd.isna(e.value) else float(e.value)}
            for e in evidence.itertuples()
        ]
        decisions.append({"stay_id": row.stay_id, "y": int(row.y), "risk": float(row.risk),
                          "passed": passed, "n_signals": n_signals})
        trail.append({"stay_id": int(row.stay_id), "decision": "pass" if passed else "block",
                      "n_distinct_signals": n_signals, "evidence": refs})
    dec = pd.DataFrame(decisions)

    metrics = {}
    if len(dec):
        tp, fp = dec[dec.y == 1], dec[dec.y == 0]
        metrics = {
            "min_signals": min_signals,
            "evidence_window_hours": evidence_window_hours,
            "alerts_total": int(len(dec)),
            "passed_total": int(dec.passed.sum()),
            "blocked_total": int((~dec.passed).sum()),
            "pass_rate_true_alerts": round(float(tp.passed.mean()), 4) if len(tp) else None,
            "pass_rate_false_alerts": round(float(fp.passed.mean()), 4) if len(fp) else None,
            "median_signals_true_alerts": float(tp.n_signals.median()) if len(tp) else None,
            "median_signals_false_alerts": float(fp.n_signals.median()) if len(fp) else None,
        }
    return dec, trail, metrics


def gate_operating_curve(timelines: dict[int, Timeline], alerts: pd.DataFrame,
                         at_hours: float = 24.0, evidence_window_hours: float = 6.0,
                         max_signals: int = 6) -> list[dict]:
    """Pass rates for true vs false alerts as the evidence requirement tightens."""
    curve = []
    for m in range(1, max_signals + 1):
        _, _, metrics = run_gate(timelines, alerts, at_hours=at_hours,
                                 min_signals=m, evidence_window_hours=evidence_window_hours)
        curve.append({"min_signals": m,
                      "pass_rate_true_alerts": metrics.get("pass_rate_true_alerts"),
                      "pass_rate_false_alerts": metrics.get("pass_rate_false_alerts"),
                      "blocked_total": metrics.get("blocked_total")})
    return curve


def audit_trail_resolvability(trail: list[dict], timelines: dict[int, Timeline]) -> dict:
    """Re-resolve every logged evidence reference against the timelines.

    A reference resolves when (source, source_row) exists in the stay's
    timeline with the same timestamp and label. Measured, not assumed.
    """
    total, resolved = 0, 0
    for entry in trail:
        ev = timelines[entry["stay_id"]].events
        for ref in entry["evidence"]:
            total += 1
            hit = ev[(ev.source == ref["source"]) & (ev.source_row == ref["source_row"])]
            if len(hit) == 1 and str(hit.iloc[0].t) == ref["t"] and hit.iloc[0].label == ref["label"]:
                resolved += 1
    return {
        "evidence_references_total": total,
        "evidence_references_resolved": resolved,
        "trail_resolvability": round(resolved / total, 4) if total else None,
    }
