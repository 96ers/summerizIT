from typing import List

from src.models import TranslationRequest, TranslationResult
from src.repositories import BaseRepository


class TranslationRequestRepository(BaseRepository[TranslationRequest]):
    def get_by_userId(self, userId: str) -> List[TranslationRequest]:
        return self.get_all({"userId": userId})


class TranslationResultRepository(BaseRepository[TranslationResult]):
    def get_by_requestId(self, requestId: str) -> List[TranslationResult]:
        return self.get_all({"requestId": requestId})
