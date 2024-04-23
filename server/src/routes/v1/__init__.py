"""API v1 router."""

from fastapi import APIRouter

from .auth import auth_router

v1_router = APIRouter()

v1_router.include_router(auth_router, tags=["auth"])


@v1_router.get("")
def home_v1():
    """Home route."""
    return "Welcome to My API v1"
