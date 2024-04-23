from pydantic_settings import BaseSettings


class ServerConfig(BaseSettings):
    TITLE: str = "FastAPI backend"
    PORT: int = 8000
    DEBUG: bool = True
    RELOAD: bool = True
