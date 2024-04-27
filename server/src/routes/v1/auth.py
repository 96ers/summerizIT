from fastapi import APIRouter, Depends, status

from src.controllers import AuthController
from src.controllers.factory import Factory
from src.models.schemas import (
    Token,
    UserLoginRequest,
    UserRegisterRequest,
    RefreshToken,
)
from src.models import User
from src.middlewares.dependencies import authorization

auth_router = APIRouter()


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=Token,
)
async def register_user(
    user_register_request: UserRegisterRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> Token:
    return auth_controller.register(
        email=user_register_request.email,
        password=user_register_request.password,
        username=user_register_request.username,
    )


@auth_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=Token
)
async def login_user(
    user_login_request: UserLoginRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> Token:
    return auth_controller.login(
        email=user_login_request.email,
        password=user_login_request.password,
    )


@auth_router.post(
    "/refresh",
    status_code=status.HTTP_200_OK,
    response_model=Token
)
async def refresh_token(
    refresh_token: RefreshToken,
    auth_controller: AuthController = Depends(Factory().get_auth_controller)
) -> Token:
    return auth_controller.refresh(
        refresh_token.id,
        refresh_token.refresh_token
    )


@auth_router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(authorization)],
)
async def logout(
    user: User = Depends(authorization),
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    auth_controller.logout(user)
    return {
        "message": "Logout Success"
    }
