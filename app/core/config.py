"""Application configuration settings using Pydantic."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "E-Commerce API"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    secret_key: str = "changeme"
    access_token_expire_minutes: int = 30
    refresh_token_expire_minutes: int = 60 * 24 * 7

    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/ecommerce"
    redis_url: str = "redis://localhost:6379/0"

    algorithm: str = "HS256"
    bcrypt_rounds: int = 12

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
