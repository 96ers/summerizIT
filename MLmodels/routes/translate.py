from fastapi import APIRouter
from schemas import TranslationRequest
from models.mTet import translate

translate_router = APIRouter()


@translate_router.post("/mTetTranslate")
async def translate_by_mTet(tran_req: TranslationRequest):
    """mTet translation api

    Args:
        tran_req (TranslationRequest): translation request

    Returns:
        json response: {"translation" : str}
    """
    # call the mTet translate method
    translation = translate(tran_req.text, tran_req.isEnglish)
    return {"translation": translation}
