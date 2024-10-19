from pydantic_settings import BaseSettings
from pydantic import EmailStr, PostgresDsn, validator
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    API_V1_STR: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_TLS: bool
    MAIL_SSL: bool
    ALLOWED_ORIGINS: List[str]

    class Config:
        env_file = ".env"

# Instantiate the settings
settings = Settings()
