"""RAG pipeline (Layer 3 — Reasoning / RAG).

Composes retrieve → rerank → assemble into a single call the agents use to obtain
grounded, cited evidence. Faithfulness/relevancy can be evaluated with ragas.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from acdss.rag.reranker import Reranker
from acdss.rag.retriever import Retriever


class RetrievedChunk(BaseModel):
    """An evidence chunk with provenance for citation."""

    text: str
    source: str
    score: float


class RagResult(BaseModel):
    """Output of a RAG query: composed context plus its supporting chunks."""

    query: str
    context: str
    chunks: list[RetrievedChunk] = Field(default_factory=list)


class RagPipeline:
    """Retrieve → rerank → compose grounded context."""

    def __init__(self, retriever: Retriever | None = None, reranker: Reranker | None = None) -> None:
        self.retriever = retriever or Retriever()
        self.reranker = reranker or Reranker()

    def query(self, query: str, top_k: int = 10, top_n: int = 5) -> RagResult:
        """Return grounded context for ``query``.

        Outline:
          1. ``retriever.retrieve(query, top_k)``
          2. ``reranker.rerank(query, hits, top_n)``
          3. Concatenate the reranked chunks into a cited context string.
        """
        # TODO: implement the three steps and build RagResult.
        raise NotImplementedError

    def evaluate(self, results: list[RagResult]) -> dict[str, float]:
        """Compute ragas metrics (faithfulness, answer/context relevancy).

        TODO: adapt results into a ragas dataset and run the metric suite.
        """
        raise NotImplementedError
