"""Application configuration.

All settings are read from the environment (or a local ``.env`` file) via
``pydantic-settings``. No secrets are hard-coded. Import the singleton
:data:`settings` or call :func:`get_settings` where a fresh read is needed.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed view over the environment. Mirrors ``.env.example``."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ---- LLM provider ----
    llm_provider: Literal["anthropic", "openai", "local"] = "anthropic"
    llm_api_key: str = Field(default="", description="Provider API key; never commit a real value.")
    model_name: str = "claude-sonnet-5"
    llm_max_tokens: int = 4096
    llm_thinking: Literal["on", "off"] = "on"

    # ---- Data / vector store ----
    db_url: str = "postgresql://acdss:changeme@localhost:5432/acdss"
    vector_db: Literal["pgvector"] = "pgvector"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_dim: int = 384
    mimic_schema: str = "mimiciv"
    guidelines_path: str = "./data/guidelines"

    # ---- API ----
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    require_hitl: bool = True

    # ---- Trust / safety ----
    audit_log_path: str = "./logs/audit.jsonl"
    min_confidence: float = 0.6

    # ---- Misc ----
    log_level: str = "INFO"
    environment: Literal["development", "staging", "production"] = "development"


@lru_cache
def get_settings() -> Settings:
    """Return a cached :class:`Settings` instance."""
    return Settings()


settings = get_settings()
