"""MemoryManager — coordinates the memory subsystem (Layer 2).

Single entry point the agents use to read/write memory. Fuses short-term,
long-term, and vector memory into a :class:`~acdss.memory.clinical_context.ClinicalContext`.
Also acts as the *MemoryManager agent* referenced in the framework.
"""

from __future__ import annotations

from acdss.data.mimic_loader import PatientRecord
from acdss.memory.clinical_context import ClinicalContext
from acdss.memory.long_term import LongTermMemory, MemoryRecord
from acdss.memory.short_term import ShortTermMemory
from acdss.memory.vector_store import VectorStore


class MemoryManager:
    """Facade over short-term, long-term, and vector memory."""

    def __init__(
        self,
        session_id: str,
        short_term: ShortTermMemory | None = None,
        long_term: LongTermMemory | None = None,
        vector_store: VectorStore | None = None,
    ) -> None:
        self.short_term = short_term or ShortTermMemory(session_id)
        self.long_term = long_term or LongTermMemory()
        self.vector_store = vector_store or VectorStore()

    def build_context(self, patient: PatientRecord, query: str | None = None) -> ClinicalContext:
        """Assemble a :class:`ClinicalContext` for ``patient``.

        Outline:
          1. Summarize prior long-term records for the patient.
          2. If ``query`` given, embed it and pull relevant evidence from the vector store.
          3. Compose vitals/labs/problem-list with the retrieved evidence.
        """
        # TODO: implement fusion of the three stores.
        raise NotImplementedError

    def remember(self, record: MemoryRecord) -> None:
        """Persist an assessment/feedback/outcome to long-term memory."""
        self.long_term.write(record)
