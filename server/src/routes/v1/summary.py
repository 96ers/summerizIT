from typing import List
import httpx

from fastapi import APIRouter, Depends, status

from src.controllers import SummaryRequestController, SummaryResultController
from src.controllers.factory import Factory
from src.middlewares.dependencies import authorization
from src.models import SummaryRequest, SummaryResult, User
from src.models.schemas import SummaryInput, SummaryOutput, SummaryHistory
from src.utils.exceptions import InternalServerError

summary_router = APIRouter()

API_URL = "http://localhost:8001"

@summary_router.post(
    "/summary",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(authorization)],
)
async def summary(
    input: SummaryInput,
    user: User = Depends(authorization),
    sum_req_controller: SummaryRequestController = Depends(
        Factory().get_sum_req_controller
    ),
    sum_res_controller: SummaryResultController = Depends(
        Factory().get_sum_res_controller
    ),
) -> SummaryOutput:
    # Create new instance summary request
    try:
        sum_req: SummaryRequest = sum_req_controller.create(
            {
                "userId": user.id,
                "text": input.source_text,
            }
        )
    except Exception as e:
        raise InternalServerError from e

    # Call service summary here
    try:
        async with httpx.AsyncClient() as client:
            body = {
                "text": sum_req.text, 
                "length": 10
            }
            if input.model.lower() == "bart":
                api_path = f"{API_URL}/summary/bart"
            else:
                api_path = f"{API_URL}/summary/gpt"
            response = await client.post(api_path, json=body)
            print(response)
            if response.status_code != status.HTTP_200_OK:
                sum_req_controller.delete(sum_req)
                raise InternalServerError(
                    "Failed to get translation from external service"
                )
            response = response.json()
            summarized_text = response["summarization"]
    except Exception as e:
        print(e)
        summarized_text = sum_req.text + input.model
    # Create new instance summary result
    try:
        sum_res: SummaryResult = sum_res_controller.create(
            {"requestId": sum_req.id, "text": summarized_text}
        )
    except Exception as e:
        sum_req_controller.delete(sum_req)
        raise InternalServerError from e
    return {"summarized_text": sum_res.text}


@summary_router.get(
    "/summary",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(authorization)],
)
async def get_summary(
    user: User = Depends(authorization),
    sum_req_controller: SummaryRequestController = Depends(
        Factory().get_sum_req_controller
    ),
    sum_res_controller: SummaryResultController = Depends(
        Factory().get_sum_res_controller
    ),
) -> List[SummaryHistory]:
    sum_requests = sum_req_controller.get_all({"userId": user.id})
    response: List[SummaryHistory] = []
    for req in sum_requests:
        res = {
            "id": req.id,
            "source_text": req.text,
            "time": req.createdAt,
            "summarized_text": sum_res_controller.get_one(
                {"requestId": req.id}
            ).text,
        }
        response.append(res)
    return response


@summary_router.post(
    "/summary-free",
    status_code=status.HTTP_200_OK,
)
async def summary(
    input: SummaryInput,
) -> SummaryOutput:
    # Call service summary here
    print(input)
    try:
        async with httpx.AsyncClient() as client:
            body = {"text": input.source_text, "length": 5}
            if input.model.lower() == "bart":
                api_path = f"{API_URL}/summary/bart"
            else:
                api_path = f"{API_URL}/summary/gpt"
            response = await client.post(api_path, json=body)
            print(response)
            if response.status_code != status.HTTP_200_OK:
                raise InternalServerError(
                    "Failed to get translation from external service"
                )
            response = response.json()
            summarized_text = response["summarization"]
    except Exception as e:
        print(e)
        summarized_text = input.source_text + input.model
    return {"summarized_text": summarized_text}
