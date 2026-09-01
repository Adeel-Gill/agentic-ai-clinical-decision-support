"""Tests for the LLM seam: deterministic mock, provider factory, HTTP shaping.

No network is touched. The OpenAI-compatible client is exercised by
substituting its transport (``_post``), which verifies request construction and
response normalization without a running backend.
"""

from __future__ import annotations

import pytest

from acdss.config import Settings
from acdss.llm.base import LLMMessage
from acdss.llm.factory import build_llm_client
from acdss.llm.mock_client import MOCK_MODEL, MockLLMClient, estimate_tokens
from acdss.llm.openai_compatible import BASE_URLS, OpenAICompatibleClient

MSG = [LLMMessage(role="user", content="Summarize the patient's recent labs.")]


# --- mock client ---------------------------------------------------------
def test_mock_is_deterministic() -> None:
    a, b = MockLLMClient(), MockLLMClient()
    assert a.complete(MSG).text == b.complete(MSG).text


def test_mock_reports_model_and_token_estimates() -> None:
    client = MockLLMClient()
    resp = client.complete(MSG, system="You are a test.")
    assert resp.model == MOCK_MODEL
    assert resp.input_tokens and resp.output_tokens
    assert client.total_input_tokens == resp.input_tokens


def test_mock_canned_text_response() -> None:
    client = MockLLMClient({"recent labs": "lactate 4.1 mmol/L, rising"})
    assert client.complete(MSG).text == "lactate 4.1 mmol/L, rising"


def test_mock_distinct_prompts_give_distinct_replies() -> None:
    client = MockLLMClient()
    other = [LLMMessage(role="user", content="Assess deterioration risk.")]
    assert client.complete(MSG).text != client.complete(other).text


def test_mock_json_synthesizes_minimal_schema_instance() -> None:
    schema = {
        "type": "object",
        "required": ["diagnosis", "confidence", "evidence"],
        "properties": {
            "diagnosis": {"type": "string"},
            "confidence": {"type": "number"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "unused": {"type": "string"},
        },
    }
    out = MockLLMClient().complete_json(MSG, schema=schema)
    assert set(out) == {"diagnosis", "confidence", "evidence"}  # required only
    assert isinstance(out["confidence"], float)
    assert isinstance(out["evidence"], list) and out["evidence"]


def test_mock_json_honors_enum_and_canned_object() -> None:
    schema = {
        "type": "object",
        "required": ["disposition"],
        "properties": {"disposition": {"type": "string", "enum": ["pass", "block"]}},
    }
    assert MockLLMClient().complete_json(MSG, schema=schema)["disposition"] == "pass"

    client = MockLLMClient({"recent labs": {"disposition": "block"}})
    assert client.complete_json(MSG, schema=schema)["disposition"] == "block"


def test_mock_records_calls_for_token_accounting() -> None:
    client = MockLLMClient()
    client.complete(MSG)
    client.complete_json(MSG, schema={"type": "object", "properties": {}})
    assert [c["kind"] for c in client.calls] == ["complete", "complete_json"]
    assert client.total_output_tokens > 0


def test_estimate_tokens_monotonic_and_positive() -> None:
    assert estimate_tokens("") == 1
    assert estimate_tokens("a" * 400) > estimate_tokens("a" * 40)


# --- factory -------------------------------------------------------------
def test_factory_returns_mock_by_default() -> None:
    assert isinstance(build_llm_client(Settings(llm_provider="mock")), MockLLMClient)


def test_factory_builds_local_ollama_without_key() -> None:
    client = build_llm_client(Settings(llm_provider="ollama"))
    assert isinstance(client, OpenAICompatibleClient)
    assert client.base_url == BASE_URLS["ollama"]
    assert not client.model.startswith("claude-")  # anthropic default not leaked


def test_factory_requires_key_for_hosted_providers() -> None:
    for provider in ("groq", "github", "openai", "anthropic"):
        with pytest.raises(ValueError, match="llm_api_key"):
            build_llm_client(Settings(llm_provider=provider, llm_api_key=""))


def test_factory_rejects_unknown_provider() -> None:
    cfg = Settings(llm_provider="mock")
    object.__setattr__(cfg, "llm_provider", "nope")
    with pytest.raises(ValueError, match="unknown llm_provider"):
        build_llm_client(cfg)


def test_factory_respects_explicit_base_url_and_model() -> None:
    cfg = Settings(
        llm_provider="local",
        llm_base_url="http://127.0.0.1:1234/v1",
        model_name="phi-4",
    )
    client = build_llm_client(cfg)
    assert client.base_url == "http://127.0.0.1:1234/v1"
    assert client.model == "phi-4"


# --- OpenAI-compatible request/response shaping --------------------------
def _stub(monkeypatch: pytest.MonkeyPatch, client: OpenAICompatibleClient) -> list[dict]:
    """Capture payloads instead of sending them; return the capture list."""
    seen: list[dict] = []

    def fake_post(path: str, payload: dict) -> dict:
        seen.append({"path": path, **payload})
        return {
            "model": "stub-model",
            "choices": [{"message": {"content": '{"ok": true}'}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 11, "completion_tokens": 7},
        }

    monkeypatch.setattr(client, "_post", fake_post)
    return seen


def test_openai_compatible_complete_shapes_request(monkeypatch: pytest.MonkeyPatch) -> None:
    client = OpenAICompatibleClient("ollama", "qwen2.5:7b")
    seen = _stub(monkeypatch, client)
    resp = client.complete(MSG, system="sys", max_tokens=256)

    sent = seen[0]
    assert sent["path"] == "chat/completions"
    assert sent["temperature"] == 0  # reproducibility
    assert sent["max_tokens"] == 256
    assert sent["messages"][0] == {"role": "system", "content": "sys"}
    assert resp.model == "stub-model"
    assert (resp.input_tokens, resp.output_tokens) == (11, 7)
    assert client.last_usage == {"input_tokens": 11, "output_tokens": 7}


def test_openai_compatible_json_requests_json_object(monkeypatch: pytest.MonkeyPatch) -> None:
    client = OpenAICompatibleClient("groq", "llama-3.3-70b-versatile", api_key="k")
    seen = _stub(monkeypatch, client)
    schema = {"type": "object", "properties": {"ok": {"type": "boolean"}}}

    assert client.complete_json(MSG, schema=schema) == {"ok": True}
    sent = seen[0]
    assert sent["response_format"] == {"type": "json_object"}
    assert "JSON Schema" in sent["messages"][0]["content"]  # schema restated


def test_openai_compatible_json_survives_fences_and_garbage(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = OpenAICompatibleClient("ollama", "qwen2.5:7b")

    def reply(text: str) -> dict:
        return {
            "model": "m",
            "choices": [{"message": {"content": text}, "finish_reason": "stop"}],
            "usage": {},
        }

    monkeypatch.setattr(client, "_post", lambda p, d: reply('```json\n{"a": 1}\n```'))
    assert client.complete_json(MSG, schema={"type": "object"}) == {"a": 1}

    monkeypatch.setattr(client, "_post", lambda p, d: reply("I cannot comply."))
    out = client.complete_json(MSG, schema={"type": "object"})
    assert out["_unparsed"] == "I cannot comply."  # never raises mid-run


def test_openai_compatible_preset_and_trailing_slash() -> None:
    assert OpenAICompatibleClient("groq", "m").base_url == BASE_URLS["groq"]
    assert OpenAICompatibleClient("http://x/v1/", "m").base_url == "http://x/v1"
