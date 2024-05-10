from fastapi.requests import Request
from fastapi.responses import Response
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed
from sqlalchemy.orm import Session

from src.database import engine
from src.models import User, UserRole


class MyAuthProvider(AuthProvider):
    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response
    ) -> Response:
        if len(username) < 5:
            raise FormValidationError(
                {"username": "Ensure username has at least 05 characters"}
            )
        session: Session = request.state.session
        user = session.query(User).filter(
            User.username == username,
            User.password == password
        ).first()
        if not user:
            raise LoginFailed("User doesn't exist!!!")

        if user.role != UserRole.ADMIN:
            raise LoginFailed("You don't have permission to do that!")

        request.session.update({"username": username})
        return response

    async def is_authenticated(self, request: Request) -> bool:
        username = request.session.get("username", None)
        if username is None:
            return False

        with Session(engine) as session:
            user = session.query(User).filter(
                User.username == username
            ).first()
        if user is None:
            return False

        request.state.user = user
        return True

    def get_admin_config(self, request: Request) -> AdminConfig | None:
        user = request.state.user
        # Update app title according to current_user
        custom_app_title = "Hello " + user.username + "!"
        return AdminConfig(
            app_title=custom_app_title
        )

    def get_admin_user(self, request: Request) -> AdminUser | None:
        user = request.state.user
        return AdminUser(username=user.username)

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response
