"""OpenAI-compatible implementation of :class:`~acdss.llm.base.LLMClient`.

One client covers every backend that speaks the OpenAI chat-completions API,
which is how the prototype reaches **zero-cost inference**:

======================  ================================================  =========
Backend                 ``base_url``                                      Key?
======================  ================================================  =========
Ollama (local)          ``http://localhost:11434/v1``                     no
Groq (free tier)        ``https://api.groq.com/openai/v1``                yes (free)
GitHub Models           ``https://models.github.ai/inference``            yes (PAT)
vLLM / LM Studio        host-dependent                                    usually no
OpenAI                  ``https://api.openai.com/v1``                     yes (paid)
======================  ================================================  =========

Only the standard library is used for transport, so a local Ollama run needs no
extra packages.

⚠️ **Data-use warning.** Credentialed MIMIC-IV content must not be sent to a
third-party endpoint whose terms permit training on or retaining inputs. Free
consumer tiers frequently do. For credentialed data prefer a **local** backend
(no egress) or a provider under an agreement that forbids training on inputs —
see ``03_Dataset/PhysioNet_Access_Checklist.md`` and ``.ai/RULES.md`` R8.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any

from acdss.llm.base import LLMClient, LLMMessage, LLMResponse

# Convenience presets for the free backends.
BASE_URLS: dict[str, str] = {
    "ollama": "http://localhost:11434/v1",
    "groq": "https://api.groq.com/openai/v1",
    "github": "https://models.github.ai/inference",
    "openai": "https://api.openai.com/v1",
}


class OpenAICompatibleClient(LLMClient):
    """Chat-completions client for any OpenAI-compatible endpoint.

    Args:
        base_url: API root, e.g. ``http://localhost:11434/v1``. A bare preset
            name from :data:`BASE_URLS` (``"ollama"``, ``"groq"``, ...) is also
            accepted.
        model: Model id as the backend names it (e.g. ``"qwen2.5:7b"``,
            ``"llama-3.3-70b-versatile"``).
        api_key: Bearer token; omit for local backends that need none.
        timeout: Per-request timeout in seconds. Local CPU inference is slow —
            the default is generous on purpose.
        max_retries: Retries for transient transport/5xx failures, with linear
            backoff.
    """

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str | None = None,
        *,
        timeout: float = 600.0,
        max_retries: int = 2,
    ) -> None:
        self.base_url = BASE_URLS.get(base_url, base_url).rstrip("/")
        self.model = model
        self._api_key = api_key or None
        self.timeout = timeout
        self.max_retries = max_retries
        self.last_usage: dict[str, int] = {}

    # -- transport -------------------------------------------------------
    def _post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        """POST ``payload`` as JSON to ``path`` and return the parsed reply."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        body = json.dumps(payload).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"

        last_error: Exception | None = None
        for attempt in range(self.max_retries + 1):
            request = urllib.request.Request(url, data=body, headers=headers, method="POST")
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:  # 4xx are not retryable
                detail = exc.read().decode("utf-8", errors="replace")[:500]
                if exc.code < 500:
                    raise RuntimeError(f"{exc.code} from {url}: {detail}") from exc
                last_error = RuntimeError(f"{exc.code} from {url}: {detail}")
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last_error = exc
            if attempt < self.max_retries:
                time.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"request to {url} failed after retries: {last_error}")

    @staticmethod
    def _payload_messages(
        messages: list[LLMMessage], system: str | None
    ) -> list[dict[str, str]]:
        out = [{"role": "system", "content": system}] if system else []
        out += [{"role": m.role, "content": m.content} for m in messages]
        return out

    def _normalize(self, data: dict[str, Any]) -> LLMResponse:
        choice = (data.get("choices") or [{}])[0]
        text = ((choice.get("message") or {}).get("content")) or ""
        usage = data.get("usage") or {}
        self.last_usage = {
            "input_tokens": int(usage.get("prompt_tokens") or 0),
            "output_tokens": int(usage.get("completion_tokens") or 0),
        }
        return LLMResponse(
            text=text,
            model=str(data.get("model") or self.model),
            stop_reason=choice.get("finish_reason"),
            input_tokens=usage.get("prompt_tokens"),
            output_tokens=usage.get("completion_tokens"),
            raw=data,
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
        """Call ``/chat/completions`` and normalize the reply.

        ``thinking`` is accepted for interface parity and ignored: reasoning
        behavior on these backends is a property of the chosen model, not a
        request flag. Temperature is pinned to 0 for run-to-run stability.
        """
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": self._payload_messages(messages, system),
            "temperature": 0,
        }
        if max_tokens:
            payload["max_tokens"] = max_tokens
        if tools:
            payload["tools"] = tools
        return self._normalize(self._post("chat/completions", payload))

    def complete_json(
        self,
        messages: list[LLMMessage],
        *,
        schema: dict[str, Any],
        system: str | None = None,
    ) -> dict[str, Any]:
        """Request JSON output and parse it.

        Strategy: ask for ``response_format={"type": "json_object"}`` (widely
        supported, including Ollama and Groq) and restate the schema in the
        system prompt, since strict server-side schema enforcement is not
        universal. If the reply is not valid JSON, the raw text is returned
        under ``_unparsed`` rather than raising — the caller decides whether a
        malformed response is a failure, which keeps a whole evaluation run
        from dying on one bad generation.
        """
        instruction = (
            "Respond with a single JSON object and nothing else. It must satisfy "
            f"this JSON Schema:\n{json.dumps(schema)}"
        )
        merged_system = f"{system}\n\n{instruction}" if system else instruction
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": self._payload_messages(messages, merged_system),
            "temperature": 0,
            "response_format": {"type": "json_object"},
        }
        response = self._normalize(self._post("chat/completions", payload))
        text = response.text.strip()
        # Tolerate ```json fences from smaller models.
        if text.startswith("```"):
            text = text.strip("`")
            text = text[4:].strip() if text.lower().startswith("json") else text.strip()
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            return {"_unparsed": response.text}
        return parsed if isinstance(parsed, dict) else {"value": parsed}
