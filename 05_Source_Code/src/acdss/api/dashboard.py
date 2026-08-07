"""Dashboard API for the React clinician platform (research prototype).

⚠️ RESEARCH PROTOTYPE — NOT A MEDICAL DEVICE. Synthetic data only.

Endpoints (all under /api/dashboard):
  GET  /beds                          unit overview bed cards
  GET  /queue                         verified alerts awaiting review
  GET  /patients/{pid}/timeline       longitudinal timeline lanes + retrieved evidence
  GET  /patients/{pid}/recommendation current recommendation with claim-level evidence
  GET  /alerts                        verified + blocked alerts, gate operating curve
  GET  /audit                         audit-trail entries (append-only; POST /review appends)
  GET  /agents                        orchestration status + health metrics (real pilot numbers)
  POST /review/{rec_id}               clinician decision (approve/modify/reject + reason)
"""
from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import demo_data as D

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

# gate operating curve from the pilot (falls back to pilot report values)
_FALLBACK_CURVE = [
    {"min_signals": 1, "pass_rate_true_alerts": 0.5714, "pass_rate_false_alerts": 0.9048},
    {"min_signals": 2, "pass_rate_true_alerts": 0.5714, "pass_rate_false_alerts": 0.6667},
    {"min_signals": 3, "pass_rate_true_alerts": 0.5714, "pass_rate_false_alerts": 0.4762},
    {"min_signals": 4, "pass_rate_true_alerts": 0.4286, "pass_rate_false_alerts": 0.1429},
    {"min_signals": 5, "pass_rate_true_alerts": 0.4286, "pass_rate_false_alerts": 0.0952},
    {"min_signals": 6, "pass_rate_true_alerts": 0.1429, "pass_rate_false_alerts": 0.0476},
]


@router.get("/beds")
def beds() -> list[dict]:
    return D.BEDS


@router.get("/queue")
def queue() -> list[dict]:
    return D.QUEUE


@router.get("/patients/{pid}/timeline")
def timeline(pid: str) -> dict:
    tl = D.TIMELINE.get(pid)
    if tl is None:
        raise HTTPException(404, f"No timeline for {pid} (synthetic demo has P-1043 only)")
    return tl


@router.get("/patients/{pid}/recommendation")
def recommendation(pid: str) -> dict:
    rec = D.RECOMMENDATION.get(pid)
    if rec is None:
        raise HTTPException(404, f"No recommendation for {pid}")
    return rec


@router.get("/alerts")
def alerts() -> dict:
    pilot = D.pilot_metrics()
    curve = (pilot or {}).get("verification_gate_operating_curve") or _FALLBACK_CURVE
    return {"verified": D.ALERTS["verified"], "blocked": D.ALERTS["blocked"],
            "operating_curve": curve, "current_threshold": 3}


@router.get("/audit")
def audit() -> list[dict]:
    return D.AUDIT


@router.get("/agents")
def agents() -> dict:
    pilot = D.pilot_metrics() or {}
    retrieval = pilot.get("retrieval", {})
    gate = pilot.get("verification_gate", {})
    trail = pilot.get("audit_trail", {})
    health = {
        "retrieval_latency_ms": retrieval.get("latency_ms", {}).get("median"),
        "gate_pass_rate": (round(gate["passed_total"] / gate["alerts_total"], 2)
                            if gate.get("alerts_total") else None),
        "trail_resolvability": trail.get("trail_resolvability"),
        "quarantined": 0,
        "source": "pilot_metrics.json" if pilot else "fallback",
    }
    return {"agents": D.AGENTS, "log": D.AGENT_LOG, "health": health}


class ReviewDecision(BaseModel):
    decision: str = Field(pattern="^(approve|modify|reject)$")
    reason: str = ""
    clinician: str = "demo-clinician"


@router.post("/review/{rec_id}")
def review(rec_id: str, body: ReviewDecision) -> dict:
    if body.decision in ("modify", "reject") and not body.reason.strip():
        raise HTTPException(422, "Reason is required for modify/reject")
    entry = {
        "ts": datetime.now(timezone.utc).strftime("%H:%M:%S"),
        "patient": rec_id.split("-")[0] if rec_id else "?",
        "status": f"clinician-{body.decision}",
        "title": f"Clinician decision recorded for {rec_id}",
        "recommendation": rec_id,
        "verification": "n/a (human decision event)",
        "references": [],
        "resolvability": True,
        "decision": f"{body.decision.capitalize()} by {body.clinician}. Reason: {body.reason or '—'}",
    }
    D.AUDIT.insert(0, entry)  # in-memory only; a real deployment writes an append-only store
    return {"recorded": True, "audit_entry": entry}
