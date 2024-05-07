from fastapi import APIRouter
from .translate import translate_router

router = APIRouter()
router.include_router(translate_router, tags=["Translate"])
