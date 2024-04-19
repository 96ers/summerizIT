"""API v1 router."""

from fastapi import APIRouter, Depends

from .auth import auth_router
from src.middlewares.dependencies import validate_api_key

v1_router = APIRouter()

v1_router.include_router(
    auth_router,
    tags=["auth"],
    dependencies=[
        Depends(validate_api_key),
    ],
)


@v1_router.get("")
def home_v1():
    """Home route."""
    return "Welcome to My API v1"
