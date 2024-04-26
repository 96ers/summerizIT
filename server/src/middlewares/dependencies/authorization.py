from fastapi import Depends, Header

from src.controllers import KeyController, UserController
from src.controllers.factory import Factory
from src.models import User
from src.utils import JWTHandler
from src.utils.exceptions import UnauthorizedException


async def authorization(
    user_id: str = Header(
        alias="user-id",
    ),
    authorization: str = Header(
        alias="authorization",
    ),
    key_controller: KeyController = Depends(Factory().get_key_controller),
    user_controller: UserController = Depends(Factory().get_user_controller),
) -> User:
    key = key_controller.get_by_userId(userId=user_id)
    if key is None:
        raise UnauthorizedException(message="Invalid authorization")
    tokenDecoded = JWTHandler.decode(key=key.publicKey, token=authorization)
    # print(tokenDecoded)
    if tokenDecoded.get("user_id") != user_id:
        raise UnauthorizedException(message="Invalid authorization")
    user = user_controller.get_by_id(id=user_id)
    if user is None:
        raise UnauthorizedException(message="Invalid authorization")
    return user
