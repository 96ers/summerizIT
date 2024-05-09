# from fastapi.requests import Request
# from fastapi.responses import Response
# from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
# from starlette_admin.exceptions import FormValidationError, LoginFailed
# from sqlalchemy import select

# from database.session import SessionLocal
# from models import User


# class MyAuthProvider(AuthProvider):
#     async def login(
#         self,
#         username: str,
#         password: str,
#         remember_me: bool,
#         request: Request,
#         response: Response
#     ) -> Response:
#         if len(username) < 5:
#             raise FormValidationError(
#                 {"username": "Ensure username has at least 05 characters"}
#             )
#         user = None
