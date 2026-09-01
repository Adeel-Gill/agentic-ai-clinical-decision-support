"""Build an :class:`~acdss.llm.base.LLMClient` from configuration.

The whole point of the seam: switching between the offline mock, a local
Ollama model, a free hosted tier, and a paid API is a change of environment
variables, never a change of agent code. Every call site takes a client from
:func:`build_llm_client`.

Cost/data posture per provider is documented in :mod:`acdss.config`.
"""

from __future__ import annotations

from acdss.config import Settings, settings as default_settings
from acdss.llm.base import LLMClient

# Sensible default model per provider when ``model_name`` is left at its default.
_DEFAULT_MODELS: dict[str, str] = {
    "ollama": "qwen2.5:7b",
    "groq": "llama-3.3-70b-versatile",
    "github": "openai/gpt-4o-mini",
    "openai": "gpt-4o-mini",
}
_OPENAI_COMPATIBLE = {"openai", "ollama", "groq", "github", "local"}


def build_llm_client(config: Settings | None = None) -> LLMClient:
    """Return the client selected by ``config`` (defaults to the singleton).

    Raises:
        ValueError: If a hosted provider is selected without an API key, or the
            provider name is unknown. Failing here is deliberate — a run that
            silently falls back to a different model would corrupt an
            evaluation.
    """
    cfg = config or default_settings
    provider = cfg.llm_provider

    if provider == "mock":
        from acdss.llm.mock_client import MockLLMClient

        return MockLLMClient()

    if provider == "anthropic":
        from acdss.llm.anthropic_client import AnthropicClient

        if not cfg.llm_api_key:
            raise ValueError("llm_provider='anthropic' requires llm_api_key")
        return AnthropicClient(model=cfg.model_name, api_key=cfg.llm_api_key)

    if provider in _OPENAI_COMPATIBLE:
        from acdss.llm.openai_compatible import BASE_URLS, OpenAICompatibleClient

        base_url = cfg.llm_base_url or BASE_URLS.get(provider, "")
        if not base_url:
            raise ValueError(f"llm_provider={provider!r} requires llm_base_url")
        # Local backends need no key; hosted ones do.
        if provider in {"groq", "github", "openai"} and not cfg.llm_api_key:
            raise ValueError(f"llm_provider={provider!r} requires llm_api_key")
        model = cfg.model_name
        if model.startswith("claude-"):  # the anthropic default, unset for this provider
            model = _DEFAULT_MODELS.get(provider, model)
        return OpenAICompatibleClient(
            base_url=base_url,
            model=model,
            api_key=cfg.llm_api_key or None,
        )

    raise ValueError(f"unknown llm_provider: {provider!r}")
