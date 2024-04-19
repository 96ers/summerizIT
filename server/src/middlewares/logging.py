import time
import logging
import json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from typing import Callable
from uuid import uuid4
from starlette.concurrency import iterate_in_threadpool
from fastapi import FastAPI


logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: FastAPI,
        *,
        logger: logging.Logger
    ) -> None:
        self._logger = logger
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable
    ) -> Response:
        # Set request id
        request_id: str = str(uuid4())
        start_time = time.time()

        # Request body
        request_json = await request.json()

        # Process the request
        response = await call_next(request)

        # Response body
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        response_body = response_body[0].decode()

        # Calculate response time
        process_time = time.time() - start_time
        log_data = {
            "request_id": request_id,
            "request": {
                "client": {
                    "host": request.client.host,
                    "port": request.client.port,
                },
                "method": request.method,
                "url": str(request.url),
                "headers": dict(request.headers),
                "body": request_json,
            },
            "response": {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": response_body,
            },
            "process_time": process_time,
        }
        self._logger.info(json.dumps(log_data))
        return response
