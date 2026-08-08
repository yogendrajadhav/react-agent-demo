from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # LLM Settings
    LLM_MODEL: str = "gemma4:31b-cloud"
    LLM_BASE_URL: str = "http://localhost:11434"

    # Server Settings
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8010

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
