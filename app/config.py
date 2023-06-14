from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
	counter1: int = 0

	class Config:
		env_file = ".env"


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    return Settings()
