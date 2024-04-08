"""API v1 router."""

from fastapi import APIRouter

v1_router = APIRouter()


@v1_router.get("")
def home_v1():
    """Home route."""
    return "Welcome to My API v1"
