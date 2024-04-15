from pydantic_settings import BaseSettings


class JWTConfig(BaseSettings):
    ALGORITHM: str = "HS256"
    EXPIREMINUTES: int = 60 * 24
    KEYLENGTH: int = 32
