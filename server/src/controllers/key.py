from src.models import Key
from src.repositories import KeyRepository

from .base import BaseController


class KeyController(BaseController[Key]):
    def __init__(self, repository: KeyRepository):
        super().__init__(model=Key, repository=KeyRepository)
        self.repository = repository

    def get_by_userId(self, userId: str) -> Key | None:
        return self.repository.get_one({"userId": userId})
