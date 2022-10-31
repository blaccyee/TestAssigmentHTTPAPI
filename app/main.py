"""
The main core of API application
"""

from fastapi import FastAPI
from app.handlers import router


def get_app() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = get_app()
