from typing import List

from fastapi import APIRouter, Depends, status

from src.controllers import TranslateRequestController, TranslationResultController
from src.controllers.factory import Factory
from src.middlewares.dependencies import authorization
from src.models import TranslationRequest, TranslationResult, User
from src.models.schemas import TranslateHistory, TranslateInput, TranslateOutput
from src.utils.exceptions import InternalServerError

translate_router = APIRouter()


@translate_router.post(
    "/translate",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(authorization)],
)
async def translate(
    input: TranslateInput,
    user: User = Depends(authorization),
    tran_req_controller: TranslateRequestController = Depends(
        Factory().get_tran_req_controller
    ),
    tran_res_controller: TranslationResultController = Depends(
        Factory().get_tran_res_controller
    ),
) -> TranslateOutput:
    # Create new instance translation request
    try:
        tran_req: TranslationRequest = tran_req_controller.create(
            {
                "userId": user.id,
                "text": input.source_text,
            }
        )
    except Exception as e:
        raise InternalServerError from e

    # Call service translate here
    translated_text = tran_req.text
    # Create new instance translation result
    try:
        tran_res: TranslationResult = tran_res_controller.create(
            {"requestId": tran_req.id, "text": translated_text}
        )
    except Exception as e:
        raise InternalServerError from e
    return {"translated_text": tran_res.text}


@translate_router.get(
    "/translate",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(authorization)]
)
async def get_translation(
    user: User = Depends(authorization),
    tran_req_controller: TranslateRequestController = Depends(
        Factory().get_tran_req_controller
    ),
    tran_res_controller: TranslationResultController = Depends(
        Factory().get_tran_res_controller
    ),
) -> List[TranslateHistory]:
    tran_requests = tran_req_controller.get_all({"userId": user.id})
    response: List[TranslateHistory] = []
    for req in tran_requests:
        res = {
            "id": req.id,
            "source_text": req.text,
            "time": req.createdAt,
            "translated_text": tran_res_controller.get_one(
                {"requestId": req.id}
            ).text,
        }
        response.append(res)
    return response
