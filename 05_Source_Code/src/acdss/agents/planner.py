"""Planner agent — decomposes an assessment into ordered sub-tasks."""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class PlanStep(AgentOutput):
    """A single planned step (agent + task)."""

    agent: str
    task: str = ""


class PlannerOutput(AgentOutput):
    """The ordered plan."""

    agent: str = "planner"
    steps: list[PlanStep] = Field(default_factory=list)


class PlannerAgent(Agent[AgentInput, PlannerOutput]):
    """Produces the assessment plan the Coordinator executes."""

    name = "planner"

    def run(self, inp: AgentInput) -> PlannerOutput:
        """Decompose the request into ordered steps.

        TODO: prompt the LLM to emit a structured plan constrained to the known
        agent names, then validate it.
        """
        raise NotImplementedError
