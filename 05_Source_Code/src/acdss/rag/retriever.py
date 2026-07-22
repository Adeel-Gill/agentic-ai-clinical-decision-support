"""Dense retriever (Layer 3 — RAG)."""

from __future__ import annotations

from acdss.config import settings
from acdss.memory.vector_store import VectorHit, VectorStore


class Retriever:
    """Embed a query and fetch nearest-neighbour chunks from the vector store."""

    def __init__(self, vector_store: VectorStore | None = None, embed_model: str | None = None) -> None:
        self.vector_store = vector_store or VectorStore()
        self.embed_model = embed_model or settings.embedding_model
        self._embedder = None  # TODO: lazy embedding model (share with Ingestor).

    def retrieve(self, query: str, top_k: int = 10) -> list[VectorHit]:
        """Return the ``top_k`` candidate chunks for ``query``.

        TODO: embed the query, then delegate to ``vector_store.query``.
        """
        raise NotImplementedError
