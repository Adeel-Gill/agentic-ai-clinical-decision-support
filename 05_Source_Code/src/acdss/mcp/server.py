"""MCP server exposing clinical tools to the agents.

Uses the Model Context Protocol to expose a small, auditable tool surface:

  * ``query_ehr``          — fetch structured records from MIMIC-IV (Postgres).
  * ``search_guidelines``  — semantic search over the ingested guideline corpus.
  * ``drug_interactions``  — screen a medication list for interactions.

Run standalone with ``python -m acdss.mcp.server`` (stdio transport).

⚠️ Research prototype. ``drug_interactions`` here is a placeholder, not a
validated clinical interaction checker.
"""

from __future__ import annotations

from typing import Any

# Reference implementation uses the `mcp` package:
#   from mcp.server.fastmcp import FastMCP
#   mcp = FastMCP("acdss")
# The decorated functions below are the intended tool surface.


def query_ehr(patient_id: str, tables: list[str] | None = None) -> dict[str, Any]:
    """Return structured EHR data for a patient.

    Args:
        patient_id: De-identified MIMIC-IV subject id.
        tables: Optional subset (e.g. ``["vitals", "labs", "medications"]``).

    TODO: delegate to :class:`acdss.data.mimic_loader.MimicLoader`.
    """
    raise NotImplementedError


def search_guidelines(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """Semantic search over the guideline corpus.

    TODO: delegate to :class:`acdss.rag.pipeline.RagPipeline` and return
    ``[{"text": ..., "source": ..., "score": ...}, ...]``.
    """
    raise NotImplementedError


def drug_interactions(medications: list[str], candidate: str | None = None) -> list[dict[str, Any]]:
    """Screen ``medications`` (optionally against ``candidate``) for interactions.

    TODO: back with a curated interaction knowledge base or an external API
    (behind a data-use agreement). Return severity-ranked interaction records.
    """
    raise NotImplementedError


def register_tools(mcp: Any) -> None:
    """Register the three tools on a FastMCP instance.

    TODO:
        mcp.tool()(query_ehr)
        mcp.tool()(search_guidelines)
        mcp.tool()(drug_interactions)
    """
    raise NotImplementedError


def main() -> None:
    """Entry point for ``python -m acdss.mcp.server`` / the ``acdss-mcp`` script.

    TODO:
        from mcp.server.fastmcp import FastMCP
        mcp = FastMCP("acdss")
        register_tools(mcp)
        mcp.run()  # stdio transport
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
