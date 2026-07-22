"""FastAPI application (Layer 6 — API / UI).

⚠️ RESEARCH PROTOTYPE — NOT A MEDICAL DEVICE.
This service is an academic proof-of-concept for an MS thesis. It is not
validated or approved for clinical use and must never be used to make, inform, or
substitute real diagnostic, monitoring, or treatment decisions. Every output
requires review and sign-off by a qualified licensed clinician. Process
de-identified data only.

Endpoints:
  POST /assess/{patient_id}        run an assessment (returns a Decision)
  GET  /health                     liveness / readiness
  POST /hitl/{assessment_id}/approve   human-in-the-loop sign-off
  POST /hitl/{assessment_id}/modify    clinician modifies the recommendation
  POST /hitl/{assessment_id}/reject    clinician rejects the recommendation
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from acdss.config import settings
from acdss.decision.engine import Decision

DISCLAIMER = (
    "Research prototype, not a medical device. Decision support only; "
    "requires review by a qualified licensed clinician. Not for clinical use."
)

app = FastAPI(
    title="ACDSS — Agentic Clinical Decision Support (research prototype)",
    description=DISCLAIMER,
    version="0.1.0",
)


# --------------------------------------------------------------------------- #
# Schemas
# --------------------------------------------------------------------------- #
class HealthResponse(BaseModel):
    status: str = "ok"
    environment: str = settings.environment
    disclaimer: str = DISCLAIMER


class AssessResponse(BaseModel):
    assessment_id: str
    decision: Decision
    disclaimer: str = DISCLAIMER


class HitlDecision(BaseModel):
    clinician_id: str
    note: str = ""
    modified_recommendation: dict | None = Field(
        default=None, description="Present only on /modify."
    )


# --------------------------------------------------------------------------- #
# Endpoints
# --------------------------------------------------------------------------- #
@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Liveness/readiness probe.

    TODO: extend with DB and LLM connectivity checks for readiness.
    """
    return HealthResponse()


@app.post("/assess/{patient_id}", response_model=AssessResponse)
def assess(patient_id: str) -> AssessResponse:
    """Run an assessment for a de-identified patient id.

    Outline:
      1. Load the patient record (MimicLoader) and build ClinicalContext (MemoryManager).
      2. Compile and invoke the LangGraph (orchestration.build_graph).
      3. On a passing verification gate, aggregate via DecisionEngine.
      4. Record an audit event; persist to long-term memory.
      5. If REQUIRE_HITL, mark ``requires_human_review`` and await a HITL call.
    """
    # TODO: implement the assessment workflow described above.
    raise HTTPException(status_code=501, detail="Not implemented (scaffold).")


@app.post("/hitl/{assessment_id}/approve")
def hitl_approve(assessment_id: str, decision: HitlDecision) -> dict:
    """Record clinician approval of an assessment.

    TODO: mark the assessment approved, audit-log the sign-off, and release the
    recommendation.
    """
    raise HTTPException(status_code=501, detail="Not implemented (scaffold).")


@app.post("/hitl/{assessment_id}/modify")
def hitl_modify(assessment_id: str, decision: HitlDecision) -> dict:
    """Record a clinician-modified recommendation.

    TODO: persist the modification, audit-log it, and store as feedback in
    long-term memory for later analysis.
    """
    raise HTTPException(status_code=501, detail="Not implemented (scaffold).")


@app.post("/hitl/{assessment_id}/reject")
def hitl_reject(assessment_id: str, decision: HitlDecision) -> dict:
    """Record clinician rejection of an assessment.

    TODO: mark rejected, audit-log the reason, and capture as negative feedback.
    """
    raise HTTPException(status_code=501, detail="Not implemented (scaffold).")
