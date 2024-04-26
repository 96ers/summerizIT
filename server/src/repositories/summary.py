from typing import List

from src.models import SummaryRequest, SummaryResult
from src.repositories import BaseRepository


class SummaryRequestRepository(BaseRepository[SummaryRequest]):
    def get_by_userId(self, userId: str) -> List[SummaryRequest]:
        return self.get_all({"userId": userId})


class SummaryResultRepository(BaseRepository[SummaryResult]):
    def get_by_requestId(self, requestId: str) -> List[SummaryResult]:
        return self.get_all({"requestId": requestId})
