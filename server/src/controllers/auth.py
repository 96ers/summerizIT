from pydantic import EmailStr

from src.models import Key, User
from src.models.schemas import Token
from src.repositories import KeyRepository, UserRepository
from src.utils import JWTHandler, KeyGenerator, PasswordHandler
from src.utils.exceptions import BadRequestException

from .base import BaseController


class AuthController(BaseController[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(model=User, repository=UserRepository)
        self.repository = repository
        self.key_repository: KeyRepository = KeyRepository(
            model=Key, db_session=self.repository.session
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

        user = self.repository.create(
            {"email": email, "password": password, "username": username}
        )

        publicKey = KeyGenerator.generate_key()
        privateKey = KeyGenerator.generate_key()

        key_model = self.key_repository.create(
            {
                "userId": user.id,
                "publicKey": publicKey,
                "privateKey": privateKey,
            }
        )

        if (
            key_model.userId != user.id
            or key_model.publicKey != publicKey
            or key_model.privateKey != privateKey
        ):
            raise BadRequestException("Error while register user")

        return Token(
            id=user.id,
            access_token=JWTHandler.encode(
                key=publicKey,
                payload={"user_id": user.id, "email": user.email},
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": user.id, "email": user.email},
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

        key_model: Key = self.key_repository.update_one(
            conditions={"userId": user.id},
            attributes={
                "publicKey": publicKey,
                "privateKey": privateKey,
            },
        )

        if (
            key_model.userId != user.id
            or key_model.publicKey != publicKey
            or key_model.privateKey != privateKey
        ):
            raise BadRequestException("Error while login user")

        return Token(
            id=user.id,
            access_token=JWTHandler.encode(
                key=publicKey,
                payload={"user_id": user.id, "email": user.email},
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": user.id, "email": user.email},
            ),
        )
