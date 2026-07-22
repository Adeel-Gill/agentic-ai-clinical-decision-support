"""Short-term (working) memory.

Per-session scratchpad holding the current conversation/assessment turns and
intermediate agent outputs. Volatile — discarded when the session ends.
"""

from __future__ import annotations

from typing import Any


class ShortTermMemory:
    """In-process, bounded, session-scoped key/value + turn buffer."""

    def __init__(self, session_id: str, max_turns: int = 50) -> None:
        self.session_id = session_id
        self.max_turns = max_turns
        self._turns: list[dict[str, Any]] = []
        self._scratch: dict[str, Any] = {}

    def append_turn(self, role: str, content: str) -> None:
        """Append a conversation turn, evicting oldest beyond ``max_turns``."""
        # TODO: append and truncate to the rolling window.
        raise NotImplementedError

    def recent(self, n: int = 10) -> list[dict[str, Any]]:
        """Return the last ``n`` turns."""
        raise NotImplementedError

    def set(self, key: str, value: Any) -> None:
        """Store an intermediate value for the current session."""
        self._scratch[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a stored intermediate value."""
        return self._scratch.get(key, default)

    def clear(self) -> None:
        """Drop all session state."""
        self._turns.clear()
        self._scratch.clear()
