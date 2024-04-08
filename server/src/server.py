"""
This module is the entry point of the FastAPI application.
It creates the FastAPI server and initializes the routers.
"""

from fastapi import FastAPI

from .configs.server import EnvironmentType, server_config
from .routes import router


def init_routers(server_: FastAPI) -> None:
    """Initialize the routers."""
    server_.include_router(router, prefix="/api")


def create_server() -> FastAPI:
    """Create the FastAPI server."""
    server_ = FastAPI(
        title=server_config.TITLE,
        description="FastAPI",
        version="1.0.0",
        docs_url=(
            None
            if server_config.ENVIRONMENT == EnvironmentType.PRODUCTION.value
            else "/docs"
        ),
        redoc_url=(
            None
            if server_config.ENVIRONMENT == EnvironmentType.PRODUCTION.value
            else "/redoc"
        ),
    )
    init_routers(server_)
    return server_


server = create_server()
