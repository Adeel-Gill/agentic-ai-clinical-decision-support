"""Run the full pilot and write aggregate metrics (no patient-level data).

Usage:
    python -m acdss.pilot.run_pilot --data <mimic-iv-demo root> --out <results dir>
"""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

from .baseline import run_baseline
from .gate import audit_trail_resolvability, run_gate
from .timeline import build_timelines


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="Extracted mimic-iv-clinical-database-demo-2.2 folder")
    ap.add_argument("--out", required=True, help="Directory for aggregate metrics output")
    ap.add_argument("--at-hours", type=float, default=24.0)
    ap.add_argument("--min-evidence", type=int, default=2)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    print("[1/4] building timelines ...")
    timelines, m_timeline = build_timelines(args.data)

    print("[2/4] retrieval feasibility ...")
    from .retrieval import retrieval_metrics
    m_retrieval = retrieval_metrics(timelines, at_hours=args.at_hours)

    print("[3/4] early-warning baseline ...")
    alerts, m_baseline = run_baseline(timelines)

    print("[4/4] verification gate + audit trail ...")
    decisions, trail, m_gate = run_gate(timelines, alerts,
                                        at_hours=args.at_hours, min_signals=args.min_evidence)
    m_trail = audit_trail_resolvability(trail, timelines)
    from .gate import gate_operating_curve
    m_curve = gate_operating_curve(timelines, alerts, at_hours=args.at_hours)

    results = {
        "dataset": "MIMIC-IV Clinical Database Demo v2.2 (PhysioNet, open license)",
        "note": "Pilot feasibility study; 100-patient demo cohort; no performance claims.",
        "environment": {"python": platform.python_version()},
        "timeline_construction": m_timeline,
        "retrieval": m_retrieval,
        "early_warning_baseline": m_baseline,
        "verification_gate": m_gate,
        "verification_gate_operating_curve": m_curve,
        "audit_trail": m_trail,
    }
    (out / "pilot_metrics.json").write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))
    print(f"\nwritten: {out / 'pilot_metrics.json'}")


if __name__ == "__main__":
    main()
