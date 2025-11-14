from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore


BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    URL: str = "sqlite+aiosqlite:///./shop.db"
    ECHO: bool = True


class Settings(BaseSettings):
    """
    Application settings.
    """

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=".env",
        env_nested_delimiter="__",
        arbitrary_types_allowed=True,
    )
    db: DBSettings = DBSettings()

    # Application
    APP_NAME: str = "FastAPI Shop"
    DEBUG: bool = True
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # Static
    STATIC_DIR: str = "static"
    IMAGES_DIR: str = "static/images"


settings = Settings()
