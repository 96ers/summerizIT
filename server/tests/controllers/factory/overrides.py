from src.controllers import UserController, AuthController
from src.models import User
from src.repositories import UserRepository


class ControllerOverides:
    def __init__(self, db_session):
        self.db_session = db_session

    def user_controller(self):
        return UserController(UserRepository(model=User,
                                             db_session=self.db_session))

    def auth_controller(self):
        return AuthController(UserRepository(model=User,
                                             db_session=self.db_session))
