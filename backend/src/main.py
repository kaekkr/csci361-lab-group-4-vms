"""Application module."""

from fastapi import FastAPI

from .containers import Container
from src.user.router import router as user_router
from src.auth.router import router as auth_router


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(user_router, prefix="/user", tags=["user"])
    return app


app = create_app()