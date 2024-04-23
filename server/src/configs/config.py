from pydantic_settings import BaseSettings, SettingsConfigDict
from .server import ServerConfig
from .mysql import MySQLConfig
from .jwt import JWTConfig


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="_",
        extra="allow"
    )
    server: ServerConfig
    mysql: MySQLConfig
    jwt: JWTConfig


config: Config = Config()
