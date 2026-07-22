"""Vector store over pgvector (Layer 2 — Memory / semantic index).

Stores embeddings of clinical guideline chunks and prior-case summaries for
similarity retrieval by the RAG pipeline and the Diagnosis agent.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from acdss.config import settings


class VectorHit(BaseModel):
    """A single similarity-search result."""

    id: str
    text: str
    score: float
    metadata: dict[str, Any] = {}


class VectorStore:
    """pgvector-backed similarity index."""

    def __init__(self, db_url: str | None = None, dim: int | None = None) -> None:
        self.db_url = db_url or settings.db_url
        self.dim = dim or settings.embedding_dim
        self._conn = None  # TODO: lazy psycopg connection with pgvector registered.

    def ensure_schema(self) -> None:
        """Create the extension/table/index if missing.

        TODO:
          CREATE EXTENSION IF NOT EXISTS vector;
          CREATE TABLE IF NOT EXISTS embeddings (
            id text PRIMARY KEY, text text, metadata jsonb,
            embedding vector(:dim));
          CREATE INDEX ... USING hnsw (embedding vector_cosine_ops);
        """
        raise NotImplementedError

    def upsert(self, id: str, text: str, embedding: list[float], metadata: dict[str, Any]) -> None:
        """Insert or update one embedded chunk."""
        raise NotImplementedError

    def query(self, embedding: list[float], top_k: int = 5) -> list[VectorHit]:
        """Return the ``top_k`` nearest neighbours by cosine similarity."""
        raise NotImplementedError
