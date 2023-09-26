from fastapi import FastAPI

from src.api.exception_handler import exception_handlers
from src.api.routers import routers


def init_app() -> FastAPI:
    app = FastAPI(exception_handlers=exception_handlers)

    for router in routers:
        app.include_router(router)

    return app
