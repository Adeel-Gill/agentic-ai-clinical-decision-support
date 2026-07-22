"""Explanation agent — clinician-facing rationale.

Synthesizes the other agents' outputs into a transparent, citation-backed
explanation supporting the recommendation (interpretability requirement).
"""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class ExplanationInput(AgentInput):
    """Explanation input: the upstream agent outputs to synthesize."""

    upstream: dict[str, AgentOutput] = Field(default_factory=dict)


class ExplanationOutput(AgentOutput):
    """Human-readable rationale with citations."""

    agent: str = "explanation"
    narrative: str = ""
    citations: list[str] = Field(default_factory=list)


class ExplanationAgent(Agent[ExplanationInput, ExplanationOutput]):
    """Turns structured findings into a reviewable narrative."""

    name = "explanation"

    def run(self, inp: ExplanationInput) -> ExplanationOutput:
        """Compose the rationale.

        TODO: prompt the LLM to weave diagnosis/risk/treatment findings into a
        concise narrative, preserving citations to the retrieved evidence.
        """
        raise NotImplementedError
