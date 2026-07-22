"""Cross-encoder reranker (Layer 3 — RAG).

Re-scores the dense-retrieval candidates with a cross-encoder for higher
precision before they are composed into the prompt context.
"""

from __future__ import annotations

from acdss.memory.vector_store import VectorHit


class Reranker:
    """Cross-encoder reranking of retrieved candidates."""

    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2") -> None:
        self.model_name = model_name
        self._model = None  # TODO: lazy CrossEncoder(self.model_name).

    def rerank(self, query: str, hits: list[VectorHit], top_n: int = 5) -> list[VectorHit]:
        """Return the ``top_n`` hits reordered by cross-encoder relevance.

        TODO: score each (query, hit.text) pair, sort desc, truncate to top_n.
        """
        raise NotImplementedError
