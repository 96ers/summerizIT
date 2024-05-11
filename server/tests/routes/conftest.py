# from typing import Any, Generator

# import pytest
# from fastapi import FastAPI
# from httpx import Client

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# from src.database import get_session  # noqa
# from src.server import create_server  # noqa


# @pytest.fixture(scope="session")
# def app() -> Generator[FastAPI, Any, None]:
#     """_summary_
#     Create a new FastAPI app
#     """
#     app = create_server()
#     yield app


# @pytest.fixture(scope="function")
# def client(app: FastAPI, db_session) -> Generator[Client, Any, None]:
#     """_summary_
#     Create a new FastAPI Client
#     """
#     def _get_session():
#         return db_session

#     app.dependency_overrides[get_session] = _get_session

#     with Client(app=app, base_url="http://test") as client:
#         yield client
