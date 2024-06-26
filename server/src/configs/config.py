from pydantic_settings import BaseSettings, SettingsConfigDict

from .jwt import JWTConfig
from .mysql import MySQLConfig
from .server import ServerConfig
from .administrator import Administrator


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="_", extra="allow"
    )
    server: ServerConfig
    mysql: MySQLConfig
    jwt: JWTConfig
    admin: Administrator


config: Config = Config()
