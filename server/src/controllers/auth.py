from pydantic import EmailStr

from src.models import Key, User
from src.models.schemas import Token
from src.repositories import KeyRepository, UserRepository
from src.utils import JWTHandler, KeyGenerator, PasswordHandler
from src.utils.exceptions import BadRequestException, UnauthorizedException

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
                token_type='access'
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": user.id, "email": user.email},
                token_type='refresh'
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

        if key_model is None:
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
            raise BadRequestException("Error while login user")

        return Token(
            id=user.id,
            access_token=JWTHandler.encode(
                key=publicKey,
                payload={"user_id": user.id, "email": user.email},
                token_type='access'
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": user.id, "email": user.email},
                token_type='refresh'
            ),
        )

    def refresh(self, id: str, refresh_token: str) -> Token:
        # Find privateKey by id user
        key = self.key_repository.get_by_userId(userId=id)
        if key is None:
            raise UnauthorizedException(message="User not exist")
        # Use privateKey to decode refresh_token
        tokenDecoded = JWTHandler.decode(
            key=key.privateKey,
            token=refresh_token
        )
        # Check decoded token is valid
        if tokenDecoded.get("user_id" != id):
            raise UnauthorizedException(message="Invalid token")
        # refresh_token valid, then generate publicKey, privateKey
        publicKey = KeyGenerator.generate_key()
        privateKey = KeyGenerator.generate_key()

        key_model: Key = self.key_repository.update_one(
            conditions={"userId": id},
            attributes={
                "publicKey": publicKey,
                "privateKey": privateKey,
            },
        )
        user = self.repository.get_one({"id": id})
        if user is None:
            raise UnauthorizedException(message="Error while find user")

        if (
            key_model.userId != id
            or key_model.publicKey != publicKey
            or key_model.privateKey != privateKey
        ):
            raise BadRequestException("Error while login user")

        return Token(
            id=id,
            access_token=JWTHandler.encode(
                key=publicKey,
                payload={"user_id": id, "email": user.email},
                token_type="access",
            ),
            refresh_token=JWTHandler.encode(
                key=privateKey,
                payload={"user_id": id, "email": user.email},
                token_type="refresh",
            ),
        )

    def logout(self, user: User):
        key = self.key_repository.get_one({"userId": user.id})
        return self.key_repository.delete(key)
