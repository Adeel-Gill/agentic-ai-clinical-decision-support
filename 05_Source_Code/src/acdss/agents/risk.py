"""Risk-prediction agent — deterioration / mortality / readmission risk."""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class RiskOutput(AgentOutput):
    """Predicted risk scores by outcome."""

    agent: str = "risk"
    scores: dict[str, float] = Field(
        default_factory=dict, description="outcome -> probability in [0,1] (e.g. 'deterioration_24h')."
    )
    drivers: list[str] = Field(default_factory=list, description="Top contributing features.")


class RiskPredictionAgent(Agent[AgentInput, RiskOutput]):
    """Estimates risk from the patient record.

    May combine a trained model with LLM reasoning; keeps the model behind this
    seam so it can be swapped (logistic regression, gradient boosting, ...).
    """

    name = "risk"

    def run(self, inp: AgentInput) -> RiskOutput:
        """Compute risk scores and their drivers.

        TODO: featurize the record, score with the risk model, and surface the
        top drivers (e.g. SHAP-style attributions) for the Explanation agent.
        """
        raise NotImplementedError
