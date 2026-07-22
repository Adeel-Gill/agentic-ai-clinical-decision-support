"""Decision engine (Layer 5 — Decision).

Aggregates the *verified* agent outputs into a single clinician-facing
recommendation: diagnosis, risk, treatment, explanation, and a calibrated
aggregate confidence. Abstains when confidence is below the configured floor.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from acdss.agents.base import AgentOutput
from acdss.config import settings


class Decision(BaseModel):
    """The final decision-support output for one assessment."""

    patient_id: str
    diagnosis: list[dict] = Field(default_factory=list)
    risk: dict[str, float] = Field(default_factory=dict)
    treatment: list[dict] = Field(default_factory=list)
    explanation: str = ""
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    abstained: bool = False
    requires_human_review: bool = True
    citations: list[str] = Field(default_factory=list)


class DecisionEngine:
    """Fuses verified agent outputs into a :class:`Decision`."""

    def __init__(self, min_confidence: float | None = None) -> None:
        self.min_confidence = min_confidence if min_confidence is not None else settings.min_confidence

    def aggregate(self, patient_id: str, outputs: dict[str, AgentOutput]) -> Decision:
        """Combine verified agent outputs into a final decision.

        Outline:
          1. Pull diagnosis/risk/treatment/explanation from ``outputs``.
          2. Compute an aggregate confidence (see :meth:`_aggregate_confidence`).
          3. If below ``min_confidence`` → set ``abstained=True``.
          4. Always set ``requires_human_review`` for a research prototype.
        """
        # TODO: implement aggregation and abstention.
        raise NotImplementedError

    def _aggregate_confidence(self, outputs: dict[str, AgentOutput]) -> float:
        """Combine per-agent confidences into one score.

        TODO: e.g. verification-weighted mean; calibrate via acdss.trust.calibration.
        """
        raise NotImplementedError
