"""Agent base class and shared I/O contracts.

Every agent is a typed transform ``AgentInput -> AgentOutput`` with access to an
LLM client, memory, and (optionally) tools. Concrete agents narrow the input and
output models via generics.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from acdss.llm.base import LLMClient
from acdss.memory.clinical_context import ClinicalContext


class AgentInput(BaseModel):
    """Base input passed to an agent's ``run``."""

    context: ClinicalContext
    request: str = Field(default="", description="Free-text task or question for the agent.")


class AgentOutput(BaseModel):
    """Base output returned by an agent."""

    agent: str
    summary: str = ""
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    rationale: str = ""


I = TypeVar("I", bound=AgentInput)
O = TypeVar("O", bound=AgentOutput)


class Agent(ABC, Generic[I, O]):
    """Abstract agent.

    Subclasses set :attr:`name` and implement :meth:`run`. The LLM client is
    injected so the provider stays swappable and agents remain unit-testable.
    """

    name: str = "agent"

    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm

    @abstractmethod
    def run(self, inp: I) -> O:
        """Execute the agent's task and return a typed output."""
        raise NotImplementedError

    def _system_prompt(self) -> str:
        """Return the agent's system prompt.

        TODO: override per agent with role, constraints, and the standing
        instruction that outputs are decision-support only, never autonomous
        clinical actions.
        """
        return (
            f"You are the {self.name} agent in a clinical decision-support system. "
            "You provide decision support for a licensed clinician; you never take "
            "autonomous clinical action. Ground claims in the provided context."
        )
