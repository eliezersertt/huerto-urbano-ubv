from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Huerto Urbano API"
    environment: str = "development"
    debug: bool = True

    # PostgreSQL connection string (Supabase). Example:
    # postgresql+psycopg://user:password@host:5432/database
    database_url: str = ""

    cors_origins: list[str] = ["http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
