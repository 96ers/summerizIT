"""
This module is the entry point of the FastAPI application.
It creates the FastAPI server and initializes the routers.
"""

import logging
from typing import List

from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.configs import config
from src.database import engine
from src.middlewares import LoggingMiddleware
from src.models import Base
from src.routes import router
from src.routes.admin import admin_page
from src.utils.exceptions import CustomException


def init_logger() -> logging.Logger:
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    return logging.getLogger()


def on_auth_error(request: Request, exc: Exception):
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def init_routers(server_: FastAPI) -> None:
    """Initialize the routers."""
    server_.include_router(router, prefix="/api")


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(LoggingMiddleware, logger=init_logger()),
    ]
    return middleware


def create_server() -> FastAPI:
    """Create the FastAPI server."""
    Base.metadata.create_all(bind=engine)  # create all models
    server_ = FastAPI(
        title=config.server.TITLE,
        description="FastAPI",
        version="1.0.0",
        docs_url=None if not config.server.DEBUG else "/docs",
        redoc_url=None if not config.server.DEBUG else "/redoc",
        middleware=make_middleware(),
    )
    admin_page(server_)
    init_routers(server_)
    init_listeners(server_)
    return server_


server = create_server()
