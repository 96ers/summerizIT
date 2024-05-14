from typing import List
import httpx

from fastapi import APIRouter, Depends, status

from src.controllers import TranslateRequestController, TranslationResultController
from src.controllers.factory import Factory
from src.middlewares.dependencies import authorization
from src.models import TranslationRequest, TranslationResult, User
from src.models.schemas import TranslateHistory, TranslateInput, TranslateOutput
from src.utils.exceptions import InternalServerError

translate_router = APIRouter()

API_URL = "http://localhost:8001"

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
    try:
        async with httpx.AsyncClient() as client:
            body = {
                "text": tran_req.text,
                "EngToViet": True
            }
            if input.model.lower() == "vinai":
                api_path = f"{API_URL}/translate/vinai"
            else:
                api_path = f"{API_URL}/translate/gpt"
            response = await client.post(api_path, json=body, timeout=None)
            if response.status_code != status.HTTP_200_OK:
                tran_req_controller.delete(tran_req)
                raise InternalServerError("Failed to get translation from external service")
            response = response.json()        
            translated_text = response["translation"]
    except Exception as e:
        translated_text = tran_req.text + input.model
        print(e)

    # Create new instance translation result
    try:
        tran_res: TranslationResult = tran_res_controller.create(
            {"requestId": tran_req.id, "text": translated_text}
        )
    except Exception as e:
        tran_req_controller.delete(tran_req)
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
        tran_res = tran_res_controller.get_one({"requestId": req.id})
        res = {
            "id": req.id,
            "source_text": req.text,
            "time": req.createdAt,
            "translated_text": tran_res.text if tran_res else "",
        }
        response.append(res)
    return response


@translate_router.post(
    "/translate-free",
    status_code=status.HTTP_200_OK,
)
async def translate(
    input: TranslateInput,
) -> TranslateOutput:
    # Call service translate here
    try:
        async with httpx.AsyncClient() as client:
            body = {"text": input.source_text, "EngToViet": True}
            if input.model.lower() == "vinai":
                api_path = f"{API_URL}/translate/vinai"
            else:
                api_path = f"{API_URL}/translate/gpt"
            response = await client.post(api_path, json=body, timeout=None)
            if response.status_code != status.HTTP_200_OK:
                raise InternalServerError(
                    "Failed to get translation from external service"
                )
            response = response.json()
            translated_text = response["translation"]
    except Exception as e:
        translated_text = input.source_text + input.model
        print(e)
    return {"translated_text": translated_text}
