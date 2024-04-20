from fastapi import APIRouter, Depends, status

from src.models.schemas import (
    UserRegisterRequest,
    Token,
    UserLoginRequest,
    UserResponse,
)
from src.controllers import AuthController
from src.controllers.factory import Factory
from src.middlewares.dependencies import authorization
from src.models import User

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
        username=user_register_request.username
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


@auth_router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(authorization)],
)
async def get_me(user: User = Depends(authorization)) -> UserResponse:
    return user
