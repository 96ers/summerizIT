"""Configurations for the server."""

from enum import Enum

from pydantic_settings import BaseSettings

from . import get_env


class EnvironmentType(Enum):
    """Enumeration for the environment type."""

    DEVELOPMENT = "dev"
    PRODUCTION = "prod"
    TEST = "test"


class ServerConfig(BaseSettings):
    """Server configurations."""

    ENVIRONMENT: str = EnvironmentType(get_env("ENV"))
    DEBUG: bool = False
    TITLE: str = get_env("TITLE")
    PORT: int = get_env("PORT")


server_config: ServerConfig = ServerConfig()
