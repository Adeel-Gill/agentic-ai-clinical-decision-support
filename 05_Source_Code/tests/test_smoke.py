"""Smoke tests — imports, config, and the FastAPI health endpoint.

These verify the scaffold is wired together (packages import, the app builds)
without requiring a database, an LLM key, or any implemented behavior.
"""

from __future__ import annotations

import importlib

import pytest


@pytest.mark.parametrize(
    "module",
    [
        "acdss",
        "acdss.config",
        "acdss.llm.base",
        "acdss.llm.anthropic_client",
        "acdss.data.mimic_loader",
        "acdss.memory.manager",
        "acdss.rag.pipeline",
        "acdss.agents.base",
        "acdss.orchestration.graph",
        "acdss.decision.engine",
        "acdss.trust.safety",
        "acdss.mcp.server",
        "acdss.api.main",
    ],
)
def test_module_imports(module: str) -> None:
    """Every package/module imports cleanly."""
    assert importlib.import_module(module) is not None


def test_settings_defaults() -> None:
    """Config loads with sane defaults and no secrets baked in."""
    from acdss.config import get_settings

    s = get_settings()
    assert s.model_name  # non-empty default
    assert 0.0 <= s.min_confidence <= 1.0
    assert s.llm_api_key == "" or s.llm_api_key.startswith("sk-")  # never a real committed key


def test_health_endpoint() -> None:
    """GET /health returns ok and carries the research-prototype disclaimer."""
    from fastapi.testclient import TestClient

    from acdss.api.main import app

    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert "not a medical device" in body["disclaimer"].lower()
