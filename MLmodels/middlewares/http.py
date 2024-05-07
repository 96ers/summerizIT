import time
import sys
from pathlib import Path
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from utils.logger import Logger

sys.path.append(str(Path(__file__).parent.parent))

LOGGER = Logger(__file__, log_file="http.log")


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        log_message = (
            f"{request.client.host} - {request.method} {request.url.path} "
            f"{request.scope['http_version']} {response.status_code} "
            f"{process_time: .2f}s"
        )
        LOGGER.log.info(log_message)
        return response
