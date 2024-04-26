"""API v1 router."""

from fastapi import APIRouter, Depends

from src.middlewares.dependencies import validate_api_key

from .auth import auth_router
from .summary import summary_router
from .translate import translate_router
from .user import user_router

v1_router = APIRouter()

v1_router.include_router(
    auth_router,
    tags=["Auth"],
    dependencies=[
        Depends(validate_api_key),
    ],
)

v1_router.include_router(
    user_router,
    tags=["User"],
    dependencies=[
        Depends(validate_api_key),
    ],
)

v1_router.include_router(
    translate_router,
    tags=["Translation"],
    dependencies=[
        Depends(validate_api_key),
    ],
)

v1_router.include_router(
    summary_router,
    tags=["Summary"],
    dependencies=[
        Depends(validate_api_key),
    ],
)


@v1_router.get("")
def home_v1():
    return {"message": "Welcome to My API v1."}
