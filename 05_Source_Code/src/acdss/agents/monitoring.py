"""Monitoring agent — vital-sign trend analysis and alerting."""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class MonitoringOutput(AgentOutput):
    """Detected trends and any triggered alerts."""

    agent: str = "monitoring"
    alerts: list[str] = Field(default_factory=list)
    trends: dict[str, str] = Field(default_factory=dict, description="metric -> 'rising'|'falling'|'stable'")


class MonitoringAgent(Agent[AgentInput, MonitoringOutput]):
    """Analyzes the vitals series for deterioration signals (e.g. early-warning scores)."""

    name = "monitoring"

    def run(self, inp: AgentInput) -> MonitoringOutput:
        """Compute trends and raise alerts.

        TODO: derive trends from ``inp.context.patient.vitals``; optionally use an
        early-warning score (e.g. NEWS2) and flag threshold breaches.
        """
        raise NotImplementedError
