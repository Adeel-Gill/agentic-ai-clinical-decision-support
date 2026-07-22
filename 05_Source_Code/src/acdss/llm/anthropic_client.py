"""Anthropic (Claude) implementation of :class:`~acdss.llm.base.LLMClient`.

Default provider. Uses the official ``anthropic`` SDK. Adaptive thinking is used
for reasoning-heavy agents; requests that may produce long output should stream.

⚠️ Research prototype. Do not send protected health information to any external
API without an appropriate agreement and de-identification.
"""

from __future__ import annotations

from typing import Any

from acdss.config import settings
from acdss.llm.base import LLMClient, LLMMessage, LLMResponse


class AnthropicClient(LLMClient):
    """Claude-backed client.

    The model id and key come from :mod:`acdss.config` by default. The model is
    kept swappable — passing a different ``model`` at construction overrides it.
    """

    def __init__(self, model: str | None = None, api_key: str | None = None) -> None:
        self.model = model or settings.model_name
        self._api_key = api_key or settings.llm_api_key
        # TODO: construct the SDK client lazily.
        #   import anthropic
        #   self._client = anthropic.Anthropic(api_key=self._api_key)
        self._client: Any | None = None

    def complete(
        self,
        messages: list[LLMMessage],
        *,
        system: str | None = None,
        max_tokens: int | None = None,
        thinking: bool = True,
        tools: list[dict[str, Any]] | None = None,
    ) -> LLMResponse:
        """Call ``client.messages.create`` and normalize the response.

        Reference shape (to implement):

            resp = self._client.messages.create(
                model=self.model,
                max_tokens=max_tokens or settings.llm_max_tokens,
                system=system,
                thinking={"type": "adaptive"} if thinking else {"type": "disabled"},
                tools=tools or [],
                messages=[m.model_dump() for m in messages],
            )
            text = next((b.text for b in resp.content if b.type == "text"), "")
            return LLMResponse(
                text=text, model=resp.model, stop_reason=resp.stop_reason,
                input_tokens=resp.usage.input_tokens,
                output_tokens=resp.usage.output_tokens,
            )

        Note: for large ``max_tokens`` use ``client.messages.stream(...)`` +
        ``get_final_message()`` to avoid HTTP timeouts.
        """
        # TODO: implement per the docstring above.
        raise NotImplementedError

    def complete_json(
        self,
        messages: list[LLMMessage],
        *,
        schema: dict[str, Any],
        system: str | None = None,
    ) -> dict[str, Any]:
        """Constrain output to ``schema`` via ``output_config.format``.

        Reference shape:

            resp = self._client.messages.create(
                model=self.model,
                max_tokens=settings.llm_max_tokens,
                system=system,
                output_config={"format": {"type": "json_schema", "schema": schema}},
                messages=[m.model_dump() for m in messages],
            )
            # first text block is guaranteed valid JSON for the schema
        """
        # TODO: implement per the docstring above.
        raise NotImplementedError
