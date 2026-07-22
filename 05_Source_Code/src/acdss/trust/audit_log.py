"""Audit logging (trustworthy AI).

Append-only, structured log of every assessment, agent step, and human decision —
supporting traceability, accountability, and post-hoc review.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from acdss.config import settings


class AuditEvent(BaseModel):
    """One append-only audit entry."""

    timestamp: datetime = Field(default_factory=datetime.utcnow)
    session_id: str
    actor: str = Field(description="Agent name, 'system', or clinician id.")
    action: str
    patient_id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class AuditLog:
    """Writes :class:`AuditEvent` records as JSON lines."""

    def __init__(self, path: str | None = None) -> None:
        self.path = path or settings.audit_log_path

    def record(self, event: AuditEvent) -> None:
        """Append an event to the audit log.

        TODO: serialize to JSON and append to ``self.path`` (create dirs as
        needed). Never log raw PHI; store references/ids only.
        """
        raise NotImplementedError
