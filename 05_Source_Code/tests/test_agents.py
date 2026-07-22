"""Agent-contract tests.

Verify the agent I/O contracts and that unimplemented behavior fails loudly
(``NotImplementedError``) rather than silently. Replace the ``raises`` checks
with behavioral assertions as each agent is implemented.
"""

from __future__ import annotations

import pytest

from acdss.agents.base import Agent, AgentInput, AgentOutput
from acdss.agents.diagnosis import DiagnosisAgent, DiagnosisOutput
from acdss.agents.monitoring import MonitoringAgent, MonitoringOutput
from acdss.agents.risk import RiskOutput, RiskPredictionAgent
from acdss.data.mimic_loader import PatientRecord
from acdss.memory.clinical_context import ClinicalContext


class _StubLLM:
    """Minimal stand-in for an LLMClient (no network)."""

    def complete(self, *args, **kwargs):  # pragma: no cover - stub
        raise NotImplementedError

    def complete_json(self, *args, **kwargs):  # pragma: no cover - stub
        raise NotImplementedError


def _ctx() -> ClinicalContext:
    return ClinicalContext(patient=PatientRecord(patient_id="TEST-0001"))


def _input() -> AgentInput:
    return AgentInput(context=_ctx(), request="assess")


def test_agent_is_abstract() -> None:
    """The base Agent cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Agent(_StubLLM())  # type: ignore[abstract]


@pytest.mark.parametrize("agent_cls", [MonitoringAgent, DiagnosisAgent, RiskPredictionAgent])
def test_agents_construct(agent_cls) -> None:
    """Concrete agents construct with an injected LLM and expose a name."""
    agent = agent_cls(_StubLLM())
    assert isinstance(agent.name, str) and agent.name


@pytest.mark.parametrize("agent_cls", [MonitoringAgent, DiagnosisAgent, RiskPredictionAgent])
def test_agents_run_not_yet_implemented(agent_cls) -> None:
    """Scaffold agents raise NotImplementedError until fleshed out."""
    agent = agent_cls(_StubLLM())
    with pytest.raises(NotImplementedError):
        agent.run(_input())


def test_output_models_are_typed() -> None:
    """Output models validate confidence bounds."""
    out = MonitoringOutput(agent="monitoring", confidence=0.5)
    assert 0.0 <= out.confidence <= 1.0
    assert isinstance(out, AgentOutput)
    # Concrete output types are distinct subclasses.
    assert issubclass(DiagnosisOutput, AgentOutput)
    assert issubclass(RiskOutput, AgentOutput)
