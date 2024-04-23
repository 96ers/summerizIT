from fastapi import APIRouter, Depends, status

from src.middlewares.dependencies import authorization
from src.models import User
from src.models.schemas import UserResponse

user_router = APIRouter()


@user_router.post(
    "/me",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(authorization)],
)
async def get_me(user: User = Depends(authorization)) -> UserResponse:
    return user
