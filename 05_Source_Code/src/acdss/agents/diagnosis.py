"""Diagnosis agent — differential diagnosis grounded in retrieved evidence."""

from __future__ import annotations

from pydantic import BaseModel, Field

from acdss.agents.base import Agent, AgentInput, AgentOutput
from acdss.rag.pipeline import RagPipeline


class DifferentialItem(BaseModel):
    """One candidate diagnosis with a likelihood and supporting evidence."""

    condition: str
    likelihood: float = Field(ge=0.0, le=1.0)
    evidence: list[str] = Field(default_factory=list)
    icd10: str | None = None


class DiagnosisOutput(AgentOutput):
    """Ranked differential diagnosis."""

    agent: str = "diagnosis"
    differential: list[DifferentialItem] = Field(default_factory=list)


class DiagnosisAgent(Agent[AgentInput, DiagnosisOutput]):
    """Generates a ranked differential using the RAG pipeline for grounding."""

    name = "diagnosis"

    def __init__(self, llm, rag: RagPipeline | None = None) -> None:  # type: ignore[no-untyped-def]
        super().__init__(llm)
        self.rag = rag or RagPipeline()

    def run(self, inp: AgentInput) -> DiagnosisOutput:
        """Produce a ranked differential.

        TODO: build a query from the context, retrieve guideline evidence via
        ``self.rag.query``, then prompt the LLM for a structured differential.
        """
        raise NotImplementedError
