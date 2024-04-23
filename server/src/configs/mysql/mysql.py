from pydantic_settings import BaseSettings


class MySQLConfig(BaseSettings):
    DATABASE: str = "summerizIT"
    USER: str = "user"
    HOST: str = "localhost"
    PASSWORD: str = "password"
    ROOTPASSWORD: str = "root"
    PORT: int = 3306
    DRIVER: str = "mysqlconnector"
    DEBUG: bool = True

    URI: str = f"mysql+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
