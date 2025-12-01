from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASS = os.getenv("POSTGRES_PASSWORD")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.getenv("POSTGRES_PORT")

    @staticmethod
    def URL_DB():
        return f"postgresql+asyncpg://{Settings.DB_USER}:{Settings.DB_PASS}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"


settings = Settings()
