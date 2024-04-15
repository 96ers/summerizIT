from sqlalchemy import Select
from sqlalchemy.orm import joinedload

from src.models import Key
from src.repositories import BaseRepository


class KeyRepository(BaseRepository[Key]):
    """
    User repository provides all the database operations for the Key model.
    """
    def get_by_userId(
        self, userId: str, join_: set[str] | None = None
    ) -> Key | None:
        query = self._query(join_)
        query = query.filter(Key.userId == userId)

        if join_ is not None:
            return self._all_unique(query)
        return self._one_or_none(query)
