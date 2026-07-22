"""Data-retrieval agent — pulls records and evidence via tools.

Bridges the agents to the data/RAG layers through the MCP tools
(``query_ehr``, ``search_guidelines``). Populates the ClinicalContext.
"""

from __future__ import annotations

from pydantic import Field

from acdss.agents.base import Agent, AgentInput, AgentOutput


class DataRetrievalOutput(AgentOutput):
    """Records/evidence fetched for the assessment."""

    agent: str = "data_retrieval"
    retrieved_sources: list[str] = Field(default_factory=list)


class DataRetrievalAgent(Agent[AgentInput, DataRetrievalOutput]):
    """Fetches EHR data and guideline evidence via MCP tools."""

    name = "data_retrieval"

    def run(self, inp: AgentInput) -> DataRetrievalOutput:
        """Retrieve records and evidence.

        TODO: call the MCP ``query_ehr`` and ``search_guidelines`` tools, then
        merge results into ``inp.context`` for downstream agents.
        """
        raise NotImplementedError
