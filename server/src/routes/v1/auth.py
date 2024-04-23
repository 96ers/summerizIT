from fastapi import APIRouter, Depends

from src.models.schemas import UserRegisterRequest, Token, UserLoginRequest
from src.controllers import AuthController
from src.controllers.factory import Factory

auth_router = APIRouter()


@auth_router.post("/register", status_code=201)
async def register_user(
    user_register_request: UserRegisterRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> Token:
    return auth_controller.register(
        email=user_register_request.email,
        password=user_register_request.password,
        username=user_register_request.username
    )


@auth_router.post("/login")
async def login_user(
    user_login_request: UserLoginRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> Token:
    return auth_controller.login(
        email=user_login_request.email,
        password=user_login_request.password,
    )
