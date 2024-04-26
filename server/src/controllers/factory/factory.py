from functools import partial

from fastapi import Depends

from src.controllers import (
    AuthController,
    KeyController,
    SummaryRequestController,
    SummaryResultController,
    TranslateRequestController,
    TranslationResultController,
    UserController,
)
from src.database import get_session
from src.models import (
    Key,
    SummaryRequest,
    SummaryResult,
    TranslationRequest,
    TranslationResult,
    User,
)
from src.repositories import (
    KeyRepository,
    SummaryRequestRepository,
    SummaryResultRepository,
    TranslationRequestRepository,
    TranslationResultRepository,
    UserRepository,
)


class Factory:

    user_repository = partial(UserRepository, User)
    key_repository = partial(KeyRepository, Key)
    translate_req_repository = partial(
        TranslationRequestRepository, TranslationRequest
    )
    translate_res_repository = partial(
        TranslationResultRepository, TranslationResult
    )

    summary_req_repository = partial(
        SummaryRequestRepository, SummaryRequest
    )
    summary_res_repository = partial(
        SummaryResultRepository, SummaryResult
    )

    def get_user_controller(self, db_session=Depends(get_session)):
        return UserController(
            repository=self.user_repository(db_session=db_session)
        )

    def get_auth_controller(self, db_session=Depends(get_session)):
        return AuthController(
            repository=self.user_repository(db_session=db_session)
        )

    def get_key_controller(self, db_session=Depends(get_session)):
        return KeyController(
            repository=self.key_repository(db_session=db_session)
        )

    def get_tran_req_controller(self, db_session=Depends(get_session)):
        return TranslateRequestController(
            repository=self.translate_req_repository(db_session=db_session)
        )

    def get_tran_res_controller(self, db_session=Depends(get_session)):
        return TranslationResultController(
            repository=self.translate_res_repository(db_session=db_session)
        )

    def get_sum_req_controller(self, db_session=Depends(get_session)):
        return SummaryRequestController(
            repository=self.summary_req_repository(db_session=db_session)
        )

    def get_sum_res_controller(self, db_session=Depends(get_session)):
        return SummaryResultController(
            repository=self.summary_res_repository(db_session=db_session)
        )
