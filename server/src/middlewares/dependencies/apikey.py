from fastapi import Security
from fastapi.security import APIKeyHeader

from src.configs import config
from src.utils.exceptions import UnauthorizedException


async def validate_api_key(
    key: str = Security(APIKeyHeader(name="x-api-key", auto_error=False)),
) -> None:
    if not key or key != config.server.APIKEY:
        raise UnauthorizedException(message="Invalid API Key")
