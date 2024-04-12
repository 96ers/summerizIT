from pydantic import EmailStr

from .base import BaseController

from src.models import User
from src.repositories import UserRepository
from src.utils.exceptions import BadRequestException

from src.utils import PasswordHandler


class AuthController(BaseController[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(model=User, repository=UserRepository)
        self.repository = repository

    def register(self, email: EmailStr, password: str, username: str):

        # Check if user exists with email
        user = self.repository.get_by_email(email)
        if user:
            raise BadRequestException("User already exists with this email")

        # Check if user exists with username
        user = self.repository.get_by_username(username)

        # Hash password
        password = PasswordHandler.hash(password=password)

        return self.repository.create({
            "email": email,
            "password": password,
            "username": username
        })
