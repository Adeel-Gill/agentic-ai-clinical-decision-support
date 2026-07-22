"""Treatment-recommendation agent — guideline-concordant options.

Checks candidate interventions for drug interactions via the MCP tool before
recommending. Outputs are suggestions for clinician review only.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class TreatmentOption(BaseModel):
    """A candidate intervention with its guideline basis and cautions."""

    intervention: str
    guideline_basis: str = ""
    cautions: list[str] = Field(default_factory=list)
    interaction_warnings: list[str] = Field(default_factory=list)


class TreatmentOutput(AgentOutput):
    """Ranked treatment options."""

    agent: str = "treatment"
    options: list[TreatmentOption] = Field(default_factory=list)


class TreatmentRecommendationAgent(Agent[AgentInput, TreatmentOutput]):
    """Recommends guideline-concordant options and screens interactions."""

    name = "treatment"

    def run(self, inp: AgentInput) -> TreatmentOutput:
        """Produce ranked, interaction-screened treatment options.

        TODO: retrieve guideline evidence, propose options, then call the MCP
        ``drug_interactions`` tool against the patient's medication list and
        annotate warnings.
        """
        raise NotImplementedError
