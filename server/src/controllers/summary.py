from src.models import SummaryRequest, SummaryResult
from src.repositories import SummaryRequestRepository, SummaryResultRepository

from .base import BaseController


class SummaryRequestController(BaseController[SummaryRequest]):
    def __init__(self, repository: SummaryRequestRepository):
        super().__init__(
            model=SummaryRequest, repository=SummaryRequestRepository
        )
        self.repository = repository


class SummaryResultController(BaseController[SummaryResult]):
    def __init__(self, repository: SummaryResultRepository):
        super().__init__(
            model=SummaryResult, repository=SummaryResultRepository
        )
        self.repository = repository
