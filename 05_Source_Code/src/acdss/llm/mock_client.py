"""Deterministic mock implementation of :class:`~acdss.llm.base.LLMClient`.

Purpose. Agent logic, orchestration, verification, and audit behavior can be
developed and unit-tested without a network call, an API key, or a cent of
spend. Because the responses are deterministic, tests assert on exact values
and the same inputs always produce the same run — the property the thesis's
reproducibility claims depend on.

What this is NOT. A mock run is evidence that the *plumbing* works, never
evidence about clinical or model behavior. Anything measured against this
client must be reported as an implementation check, not a result
(``.ai/RULES.md`` R2).

Two response sources, in priority order:

1. **Registered canned responses** — an exact-substring trigger mapped to the
   text (or JSON object) to return. Tests use these to drive specific paths.
2. **Deterministic synthesis** — a stable digest of the request produces a
   fixed, obviously-synthetic reply, so unregistered calls never crash a run
   and are recognizable in transcripts.

Token counts are estimated (``len(text) // 4``) so that per-case token
accounting — the input to any paid-provider cost estimate — can be exercised
before real inference is ever run.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

from acdss.llm.base import LLMClient, LLMMessage, LLMResponse

MOCK_MODEL = "mock-deterministic-1"
_MOCK_MARKER = "[MOCK]"


def estimate_tokens(text: str) -> int:
    """Return a coarse token estimate for ``text`` (~4 characters per token).

    Deliberately provider-agnostic and cheap. Used for relative cost
    projections only; a real tokenizer is required before quoting a price.
    """
    return max(1, len(text) // 4)


def _schema_example(schema: dict[str, Any], _depth: int = 0) -> Any:
    """Build a minimal instance satisfying a (subset of) JSON Schema.

    Supports the shapes the agents actually use: object/array/string/number/
    integer/boolean/null, ``enum``, and ``const``. Unknown constructs degrade
    to ``None`` rather than raising, so a schema change cannot break a test
    run silently mid-flight.
    """
    if _depth > 8:  # guard against recursive schemas
        return None
    if "const" in schema:
        return schema["const"]
    if "enum" in schema and schema["enum"]:
        return schema["enum"][0]

    typ = schema.get("type")
    if isinstance(typ, list):  # union type: take the first concrete branch
        typ = next((t for t in typ if t != "null"), "null")

    if typ == "object":
        props: dict[str, Any] = schema.get("properties", {}) or {}
        required = schema.get("required")
        keys = required if required else list(props)
        return {k: _schema_example(props.get(k, {}), _depth + 1) for k in keys}
    if typ == "array":
        item_schema = schema.get("items") or {}
        return [_schema_example(item_schema, _depth + 1)]
    if typ == "string":
        return _MOCK_MARKER
    if typ == "integer":
        return 0
    if typ == "number":
        return 0.0
    if typ == "boolean":
        return False
    if typ == "null":
        return None
    # No usable type information.
    return None


class MockLLMClient(LLMClient):
    """Deterministic, offline ``LLMClient``.

    Args:
        canned: Optional mapping of trigger substring -> response. A ``str``
            value is returned by :meth:`complete`; a ``dict`` value is returned
            by :meth:`complete_json`. The first trigger found in the rendered
            prompt wins, so register the most specific trigger first.

    Attributes:
        calls: Every call recorded as a dict with ``kind``, ``system``,
            ``messages``, and token estimates — the basis for per-case token
            accounting and for asserting that an agent asked what it should.
    """

    def __init__(self, canned: dict[str, str | dict[str, Any]] | None = None) -> None:
        self.canned: dict[str, str | dict[str, Any]] = dict(canned or {})
        self.calls: list[dict[str, Any]] = []

    # -- helpers ---------------------------------------------------------
    def register(self, trigger: str, response: str | dict[str, Any]) -> None:
        """Register (or replace) a canned ``response`` for ``trigger``."""
        self.canned[trigger] = response

    @property
    def total_input_tokens(self) -> int:
        """Estimated input tokens across every recorded call."""
        return sum(c["input_tokens"] for c in self.calls)

    @property
    def total_output_tokens(self) -> int:
        """Estimated output tokens across every recorded call."""
        return sum(c["output_tokens"] for c in self.calls)

    @staticmethod
    def _render(messages: list[LLMMessage], system: str | None) -> str:
        parts = [f"system: {system}"] if system else []
        parts += [f"{m.role}: {m.content}" for m in messages]
        return "\n".join(parts)

    def _match(self, prompt: str) -> str | dict[str, Any] | None:
        for trigger, response in self.canned.items():
            if trigger in prompt:
                return response
        return None

    @staticmethod
    def _digest(prompt: str) -> str:
        return hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:12]

    def _record(self, kind: str, prompt: str, output: str) -> None:
        self.calls.append(
            {
                "kind": kind,
                "prompt": prompt,
                "input_tokens": estimate_tokens(prompt),
                "output_tokens": estimate_tokens(output),
            }
        )

    # -- LLMClient -------------------------------------------------------
    def complete(
        self,
        messages: list[LLMMessage],
        *,
        system: str | None = None,
        max_tokens: int | None = None,
        thinking: bool = True,
        tools: list[dict[str, Any]] | None = None,
    ) -> LLMResponse:
        """Return a canned or deterministically synthesized completion."""
        prompt = self._render(messages, system)
        match = self._match(prompt)
        if isinstance(match, dict):
            text = json.dumps(match, sort_keys=True)
        elif isinstance(match, str):
            text = match
        else:
            text = f"{_MOCK_MARKER} deterministic reply {self._digest(prompt)}"
        self._record("complete", prompt, text)
        return LLMResponse(
            text=text,
            model=MOCK_MODEL,
            stop_reason="end_turn",
            input_tokens=estimate_tokens(prompt),
            output_tokens=estimate_tokens(text),
            raw={"mock": True},
        )

    def complete_json(
        self,
        messages: list[LLMMessage],
        *,
        schema: dict[str, Any],
        system: str | None = None,
    ) -> dict[str, Any]:
        """Return a canned object, else a minimal instance of ``schema``.

        The result is always a ``dict``, so agents that expect structured
        output can be exercised end-to-end offline.
        """
        prompt = self._render(messages, system)
        match = self._match(prompt)
        if isinstance(match, dict):
            obj = match
        elif isinstance(match, str):
            try:
                parsed = json.loads(match)
                obj = parsed if isinstance(parsed, dict) else {"value": parsed}
            except json.JSONDecodeError:
                obj = {"value": match}
        else:
            example = _schema_example(schema)
            obj = example if isinstance(example, dict) else {"value": example}
        self._record("complete_json", prompt, json.dumps(obj, sort_keys=True))
        return obj
