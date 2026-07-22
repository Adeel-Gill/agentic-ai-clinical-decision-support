"""Guideline ingestion (Layer 3 — RAG).

Chunks and embeds a clinical-guidelines corpus into the pgvector store so it can
be retrieved as grounding evidence.
"""

from __future__ import annotations

from pathlib import Path

from acdss.config import settings
from acdss.memory.vector_store import VectorStore


class Ingestor:
    """Chunk → embed → upsert a document corpus into the vector store."""

    def __init__(self, vector_store: VectorStore | None = None, embed_model: str | None = None) -> None:
        self.vector_store = vector_store or VectorStore()
        self.embed_model = embed_model or settings.embedding_model
        self._embedder = None  # TODO: lazy sentence-transformers model.

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of texts. TODO: SentenceTransformer(self.embed_model).encode."""
        raise NotImplementedError

    def chunk(self, text: str, chunk_size: int = 800, overlap: int = 120) -> list[str]:
        """Split ``text`` into overlapping chunks. TODO: token- or sentence-aware split."""
        raise NotImplementedError

    def ingest_path(self, path: str | Path | None = None) -> int:
        """Ingest every document under ``path`` (defaults to configured corpus).

        Returns the number of chunks written. TODO: walk files, chunk, embed, upsert.
        """
        raise NotImplementedError
