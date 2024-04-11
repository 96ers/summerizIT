"""
This module is the entry point of the FastAPI application.
It creates the FastAPI server and initializes the routers.
"""

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from src.configs import config
from src.routes import router
from src.models import Base
from src.database import engine

from typing import List


def init_routers(server_: FastAPI) -> None:
    """Initialize the routers."""
    server_.include_router(router, prefix="/api")


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
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
    )
    init_routers(server_)
    return server_


server = create_server()
