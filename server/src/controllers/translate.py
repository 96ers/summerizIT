from src.models import TranslationRequest, TranslationResult
from src.repositories import (
    TranslationRequestRepository,
    TranslationResultRepository,
)

from .base import BaseController


class TranslateRequestController(BaseController[TranslationRequest]):
    def __init__(self, repository: TranslationRequestRepository):
        super().__init__(
            model=TranslationRequest, repository=TranslationRequestRepository
        )
        self.repository = repository


class TranslationResultController(BaseController[TranslationResult]):
    def __init__(self, repository: TranslationResultRepository):
        super().__init__(
            model=TranslationResult, repository=TranslationResultRepository
        )
        self.repository = repository
