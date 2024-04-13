from pydantic import EmailStr

from .base import BaseController

from src.models import User, Key
from src.models.schemas import Token
from src.repositories import UserRepository, KeyRepository
from src.utils.exceptions import BadRequestException
from src.utils import PasswordHandler, KeyGenerator, JWTHandler


class AuthController(BaseController[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(model=User, repository=UserRepository)
        self.repository = repository
        self.key_repository: KeyRepository = KeyRepository(
            model=Key,
            db_session=self.repository.session
        )

    def register(self, email: EmailStr, password: str, username: str) -> Token:

        # Check if user exists with email
        user = self.repository.get_by_email(email)
        if user:
            raise BadRequestException("User already exists with this email")

        # Check if user exists with username
        user = self.repository.get_by_username(username)

        # Hash password
        password = PasswordHandler.hash(password=password)

        user = self.repository.create({
            "email": email,
            "password": password,
            "username": username
        })

        publicKey = KeyGenerator.generate_key()
        privateKey = KeyGenerator.generate_key()

        key_model = self.key_repository.create({
            "userId": user.userId,
            "publicKey": publicKey,
            "privateKey": privateKey,
        })

        if (
            key_model.userId != user.userId
            or key_model.publicKey != publicKey
            or key_model.privateKey != privateKey
        ):
            raise BadRequestException("Error while register user")

        return Token(
            access_token=JWTHandler.encode(
                key=publicKey,
                payload={"user_id": user.userId, "email": user.email},
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": user.userId, "email": user.email},
            ),
        )

    def login(self, email: EmailStr, password: str) -> Token:
        user = self.repository.get_by_email(email)
        if not user:
            raise BadRequestException("Invalid credentials")
        if not PasswordHandler.verify(user.password, password):
            raise BadRequestException("Invalid credentials")

        publicKey = KeyGenerator.generate_key()
        privateKey = KeyGenerator.generate_key()

        key_model = self.key_repository.update_one(
            conditions={
                "userId": user.userId
            },
            attributes={
                "publicKey": publicKey,
                "privateKey": privateKey,
            }
        )

        if (
            key_model.userId != user.userId
            or key_model.publicKey != publicKey
            or key_model.privateKey != privateKey
        ):
            raise BadRequestException("Error while register user")

        return Token(
            access_token=JWTHandler.encode(
                key=publicKey,
                payload={"user_id": user.userId, "email": user.email},
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": user.userId, "email": user.email},
            ),
        )
