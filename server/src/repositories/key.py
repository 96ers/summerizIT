from src.models import Key
from src.repositories import BaseRepository


class KeyRepository(BaseRepository[Key]):
    """
    User repository provides all the database operations for the Key model.
    """

    def get_by_userId(self, userId: str) -> Key | None:
        return self.get_one({"userId": userId})
