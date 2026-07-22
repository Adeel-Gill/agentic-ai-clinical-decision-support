"""Provider-agnostic LLM interface.

The rest of the system depends only on :class:`LLMClient`; concrete providers
(Anthropic, OpenAI, a local model, ...) implement it. This keeps the LLM
swappable behind a single seam.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Literal

from pydantic import BaseModel, Field

Role = Literal["system", "user", "assistant"]


class LLMMessage(BaseModel):
    """A single chat message."""

    role: Role
    content: str


class LLMResponse(BaseModel):
    """Normalized response returned by every provider implementation."""

    text: str
    model: str
    stop_reason: str | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None
    raw: dict[str, Any] = Field(default_factory=dict, description="Provider-specific payload.")


class LLMClient(ABC):
    """Abstract chat-completion client.

    Implementations must be side-effect-free at construction time beyond
    reading configuration and building the underlying SDK client.
    """

    @abstractmethod
    def complete(
        self,
        messages: list[LLMMessage],
        *,
        system: str | None = None,
        max_tokens: int | None = None,
        thinking: bool = True,
        tools: list[dict[str, Any]] | None = None,
    ) -> LLMResponse:
        """Return a completion for ``messages``.

        Args:
            messages: Ordered conversation turns (first must be ``user``).
            system: Optional system prompt.
            max_tokens: Output cap; falls back to the configured default.
            thinking: Enable adaptive reasoning when the provider supports it.
            tools: Optional tool definitions for function calling.

        Raises:
            NotImplementedError: Until a provider implements it.
        """
        raise NotImplementedError

    @abstractmethod
    def complete_json(
        self,
        messages: list[LLMMessage],
        *,
        schema: dict[str, Any],
        system: str | None = None,
    ) -> dict[str, Any]:
        """Return a completion constrained to ``schema`` (structured output)."""
        raise NotImplementedError
