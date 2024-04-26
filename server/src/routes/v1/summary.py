from fastapi import APIRouter, Depends, status

from src.controllers import SummaryRequestController, SummaryResultController
from src.controllers.factory import Factory
from src.middlewares.dependencies import authorization
from src.models import SummaryRequest, SummaryResult, User
from src.models.schemas import SummaryInput, SummaryOutput
from src.utils.exceptions import InternalServerError

summary_router = APIRouter()


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
    summarized_text = sum_req.text
    # Create new instance summary result
    try:
        sum_res: SummaryResult = sum_res_controller.create(
            {"requestId": sum_req.id, "text": summarized_text}
        )
    except Exception as e:
        raise InternalServerError from e
    return {"summarized_text": sum_res.text}
