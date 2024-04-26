from pydantic_settings import BaseSettings


class JWTConfig(BaseSettings):
    ALGORITHM: str = "HS256"
    EXPIREMINUTESACCESS: int = 3 * 24 * 60
    EXPIREMINUTESREFRESH: int = 7 * 24 * 60
    KEYLENGTH: int = 32
