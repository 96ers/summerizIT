from functools import partial

from fastapi import Depends

from src.controllers import AuthController, UserController
from src.models import User
from src.repositories import UserRepository
from src.database import get_session


class Factory:

    user_repository = partial(UserRepository, User)

    def get_user_controller(self, db_session=Depends(get_session)):
        return UserController(
            repository=self.user_repository(db_session=db_session)
        )

    def get_auth_controller(self, db_session=Depends(get_session)):
        return AuthController(
            repository=self.user_repository(db_session=db_session)
        )
