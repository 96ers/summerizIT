from passlib.context import CryptContext


class PasswordHandler:
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash(password: str):
        return PasswordHandler.context.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return PasswordHandler.context.verify(plain_password, hashed_password)
