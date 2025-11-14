from pydantic_settings import BaseSettings  # type: ignore


class Settings(BaseSettings):
    """
    Application settings.
    """

    # Application
    APP_NAME: str = "FastAPI Shop"
    DEBUG: bool = True
    DB_URL: str = "sqlite:///./shop.db"
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # Static
    STATIC_DIR: str = "static"
    IMAGES_DIR: str = "static/images"

    class Config:
        env_file: str = ".env"


settings = Settings()
