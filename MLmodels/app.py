from fastapi import FastAPI
from middlewares import LogMiddleware, setup_cors
from routes import router


app = FastAPI()
app.add_middleware(LogMiddleware)
setup_cors(app)
app.include_router(router)
