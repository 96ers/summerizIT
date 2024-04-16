from .base import BaseController

from src.repositories import UserRepository
from src.models import User


class UserController(BaseController[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(model=User, repository=UserRepository)
        self.repository = repository

    def get_by_userId(self, userId: str) -> User | None:
        return self.repository.get_one({
            "userId": userId
        })
