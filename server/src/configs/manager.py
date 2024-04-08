from functools import lru_cache
from typing import Any


import decouple

from src.configs.settings.base import BackendBaseSettings
from src.configs.settings.development import BackendDevSettings
from src.configs.settings.environment import Environment
from src.configs.settings.production import BackendProdSettings
from src.configs.settings.staging import BackendStageSettings


class BackendSettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment
        
    def __call__(self) -> BackendBaseSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return BackendDevSettings()
        elif self.environment == Environment.STAGING.value:
            return BackendStageSettings
        return BackendProdSettings
    
    
@lru_cache
def get_settings() ->BackendBaseSettings:
    return BackendSettingsFactory(environment=decouple.config("ENVIRONMENT", default="DEV", cast=str))()

settings: BackendBaseSettings = get_settings()