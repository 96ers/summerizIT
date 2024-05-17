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

    def get_uri(self):
        return f"mysql+{self.DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"
