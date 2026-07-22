"""Verification agent — safety and consistency gate.

Runs before any recommendation is surfaced. Checks internal consistency across
agent outputs, applies safety rules, and can veto (block) the pipeline.
"""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class VerificationInput(AgentInput):
    """The set of upstream outputs to verify."""

    upstream: dict[str, AgentOutput] = Field(default_factory=dict)


class VerificationOutput(AgentOutput):
    """Verdict of the safety/consistency gate."""

    agent: str = "verification"
    passed: bool = False
    violations: list[str] = Field(default_factory=list)
    requires_human_review: bool = True


class VerificationAgent(Agent[VerificationInput, VerificationOutput]):
    """Gates the workflow on safety and cross-agent consistency."""

    name = "verification"

    def run(self, inp: VerificationInput) -> VerificationOutput:
        """Verify upstream outputs.

        TODO: apply safety rules (see acdss.trust.safety), check that the
        treatment is consistent with the differential and interaction warnings,
        and set ``passed`` / ``requires_human_review`` accordingly.
        """
        raise NotImplementedError
