"""Coordinator agent — routing and control.

Decides which agents to invoke and in what order for a given assessment, and
carries the shared plan. In the LangGraph wiring this maps to the entry/router
node.
"""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class CoordinatorInput(AgentInput):
    """Input for the coordinator."""


class CoordinatorOutput(AgentOutput):
    """Routing decision: the ordered agents to run next."""

    agent: str = "coordinator"
    next_agents: list[str] = Field(default_factory=list)


class CoordinatorAgent(Agent[CoordinatorInput, CoordinatorOutput]):
    """Routes the workflow across the specialist agents."""

    name = "coordinator"

    def run(self, inp: CoordinatorInput) -> CoordinatorOutput:
        """Decide the next agents to execute.

        TODO: inspect the context/plan and return the ordered agent list
        (typically: data_retrieval → monitoring → diagnosis → risk → treatment
        → explanation → verification).
        """
        raise NotImplementedError
