"""Safety guardrails (trustworthy AI).

Deterministic rule checks applied by the VerificationAgent and the API before any
recommendation is surfaced (e.g. contraindications, dose bounds, allergy
conflicts, missing human review).
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from acdss.agents.base import AgentOutput


class SafetyViolation(BaseModel):
    """A triggered safety rule."""

    rule: str
    severity: str = Field(description="'info' | 'warning' | 'critical'.")
    detail: str = ""


class SafetyGuard:
    """Applies hard safety rules independent of the LLM."""

    def check(self, outputs: dict[str, AgentOutput]) -> list[SafetyViolation]:
        """Return any safety violations across the agent outputs.

        TODO: implement rules such as
          - allergy vs. recommended drug conflict,
          - contraindication vs. comorbidity,
          - treatment recommended without a supporting differential,
          - unresolved drug-interaction warning marked 'critical'.
        A single 'critical' violation must block the pipeline.
        """
        raise NotImplementedError
