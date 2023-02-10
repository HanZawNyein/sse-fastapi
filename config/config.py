from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    LOGFILE: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
