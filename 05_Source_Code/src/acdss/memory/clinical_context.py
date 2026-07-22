"""Clinical context assembly (Layer 2 — Memory).

Builds the structured, token-budgeted context object handed to the agents for a
given patient: the current record, relevant history, and retrieved evidence.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from acdss.data.mimic_loader import PatientRecord


class ClinicalContext(BaseModel):
    """Everything an agent needs to reason about one patient at one point in time."""

    patient: PatientRecord
    history_summary: str = ""
    retrieved_evidence: list[str] = Field(default_factory=list)
    active_alerts: list[str] = Field(default_factory=list)

    def to_prompt_block(self) -> str:
        """Render the context as a compact text block for an LLM prompt.

        TODO: format demographics, latest vitals/labs, problem list, history
        summary and retrieved evidence within a token budget.
        """
        raise NotImplementedError
