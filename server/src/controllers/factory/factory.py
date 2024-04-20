from functools import partial

from fastapi import Depends

from src.controllers import AuthController, UserController, KeyController
from src.models import User, Key
from src.repositories import UserRepository, KeyRepository
from src.database import get_session


class Factory:

    user_repository = partial(UserRepository, User)
    key_repository = partial(KeyRepository, Key)

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
