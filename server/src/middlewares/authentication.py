from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection
from typing import Tuple, Optional

from src.models.schemas import CurrentUser

from fastapi import Request


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self,
        conn: HTTPConnection
    ) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        print(conn.headers)
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass


class Authentication:
    def __init__(self) -> None:
        pass

    async def __call__(self, request: Request):
        return request.headers.get("x-api-key")
