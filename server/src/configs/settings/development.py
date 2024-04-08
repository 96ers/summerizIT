from src.configs.settings.base import BackendBaseSettings
from src.configs.settings.environment import Environment


class BackendDevSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Dev Environment"
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT