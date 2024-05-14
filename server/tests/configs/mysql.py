from src.configs import config


class TestMySQLConfig(config.mysql):
    DATABASE: str = "test_db"
    PORT: int = 3303
