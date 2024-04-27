"""API Router."""

from fastapi import APIRouter

from .v1 import v1_router

router = APIRouter()

router.include_router(v1_router, prefix="/v1")


@router.get("", tags=["Welcome"])
def home():
    return {"message": "Welcome to My API"}
