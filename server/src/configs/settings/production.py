from src.configs.settings.base import BackendBaseSettings
from src.configs.settings.environment import Environment


class BackendProdSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Product Environment."
    ENVIRONMENT: Environment = Environment.PRODUCTION