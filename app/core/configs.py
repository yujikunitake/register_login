from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str
    PROJECT_NAME: str
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
