from pydantic_settings import BaseSettings


class Administrator(BaseSettings):
    USERNAME: str = "admin"
    EMAIL: str = "admin@admin.com"
    PASSWORD: str = "password"
