import os
from datetime import datetime, timedelta, timezone
from jose import ExpiredSignatureError, JWTError, jwt

from src.configs import config
from src.utils.exceptions import JWTDecodeError, JWTExpiredError


class KeyGenerator:
    key_length = config.jwt.KEYLENGTH

    @staticmethod
    def generate_key():
        return os.urandom(KeyGenerator.key_length).hex()


class JWTHandler:
    algorithm = config.jwt.ALGORITHM
    expire_minutes = config.jwt.EXPIREMINUTES

    @staticmethod
    def encode(key: str, payload: dict) -> str:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=JWTHandler.expire_minutes
        )
        payload.update({"exp": expire})
        return jwt.encode(
            payload, key=key, algorithm=JWTHandler.algorithm
        )

    @staticmethod
    def decode(key: str, token: str) -> dict:
        try:
            return jwt.decode(
                token=token, key=key, algorithms=JWTHandler.algorithm
            )
        except ExpiredSignatureError as exception:
            raise JWTExpiredError() from exception
        except JWTError as exception:
            raise JWTDecodeError from exception
