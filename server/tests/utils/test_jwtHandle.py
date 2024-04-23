import os
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest
from jose import JWTError, jwt

from src.utils.jwtHandler import JWTHandler
from src.utils.exceptions import JWTDecodeError


class MockConfig:
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRED_MINUTES = 10
    KEYLENGTH = 32


class MockKeyGenerator:
    key_length = MockConfig.KEYLENGTH

    @staticmethod
    def mock_generate_key():
        return os.urandom(MockKeyGenerator.key_length).hex()


@pytest.fixture
def mock_config():
    return MockConfig()


@pytest.fixture
def mock_payload():
    return {
        "sub": "123456789",
        "name": "John Doe",
        "iat": 1516239022
    }


@pytest.fixture
def mock_token(mock_payload, mock_config, key):
    expired = datetime.now(timezone.utc) + timedelta(
        minutes=mock_config.JWT_EXPIRED_MINUTES)

    payload = mock_payload.copy()
    payload.update({"exp": expired})

    return jwt.encode(
        payload, key=key, algorithm=mock_config.JWT_ALGORITHM
    )


@pytest.fixture
def mock_handler(mock_config):
    jwt_handler = JWTHandler
    jwt_handler.algorithm = mock_config.JWT_ALGORITHM
    jwt_handler.expire_minutes = mock_config.JWT_EXPIRED_MINUTES

    return jwt_handler


class TestJWTHandler:
    @patch("src.configs.config.jwt", MagicMock(return_value=mock_config))
    def test_encode(self, mock_payload, mock_handler):
        key = MockKeyGenerator()
        token = mock_handler.encode(key, mock_payload)
        assert token is not None
        assert isinstance(token, str)

    @patch("src.configs.config.jwt", MagicMock(return_value=mock_config))
    def test_decode(self, mock_token, mock_payload, mock_handler):
        key = MockKeyGenerator()
        decoded = mock_handler.decode(key, mock_token)
        assert decoded is not None
        assert isinstance(decoded, dict)
        assert decoded.pop("exp") is not None
        assert decoded == mock_payload

    @patch("src.configs.config.jwt", MagicMock(return_value=mock_config))
    def test_decode_error(self, mock_token, mock_handler):
        with pytest.raises(JWTDecodeError):
            with patch.object(jwt, "decode", side_effect=JWTError):
                key = MockKeyGenerator()
                mock_handler.decode(key, mock_token)
