from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str = ""
    LOG_LEVEL: str

    SMTP_HOST:str
    SMTP_PORT:int
    SMTP_USER:str
    SMTP_PASS:str

    REDIS_HOST: str
    REDIS_PORT: int

    @model_validator(mode="after")
    def build_database_url(self) -> 'Settings':
        self.DATABASE_URL = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return self
    SECRET_KEY: str
    algorithm: str

    class Config:
        env_file = ".env"

    test_DB_HOST: str
    test_DB_PORT: int
    test_DB_USER: str
    test_DB_PASS: str
    test_DB_NAME: str
    test_DATABASE_URL: str = ""

    @model_validator(mode="after")
    def test_build_database_url(self) -> 'Settings':
        self.test_DATABASE_URL = (
            f"postgresql+asyncpg://{self.test_DB_USER}:{self.test_DB_PASS}@{self.test_DB_HOST}:{self.test_DB_PORT}/{self.test_DB_NAME}"
        )
        return self


settings = Settings()

