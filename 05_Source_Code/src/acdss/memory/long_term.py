"""Long-term (persistent) memory.

Durable store of prior assessments, clinician feedback, and per-patient history
that should survive across sessions. Backed by Postgres.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from acdss.config import settings


class MemoryRecord(BaseModel):
    """A persisted memory entry."""

    patient_id: str
    kind: str = Field(description="e.g. 'assessment', 'feedback', 'outcome'.")
    payload: dict[str, Any]
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LongTermMemory:
    """Persistent memory backed by a relational table."""

    def __init__(self, db_url: str | None = None) -> None:
        self.db_url = db_url or settings.db_url
        self._conn = None  # TODO: lazy psycopg connection.

    def write(self, record: MemoryRecord) -> None:
        """Persist a memory record. TODO: INSERT into acdss_memory."""
        raise NotImplementedError

    def history(self, patient_id: str, kind: str | None = None) -> list[MemoryRecord]:
        """Return prior records for a patient, optionally filtered by kind."""
        raise NotImplementedError
