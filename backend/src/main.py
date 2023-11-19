"""Application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import defaultAccounts
from .containers import Container
from src.admin.router import router as admin_router
from src.auth.router import router as auth_router


def create_app() -> FastAPI:
    container = Container()

    db = container.db()

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.container = container
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(admin_router, prefix="/admin", tags=["admin"])

    # defaultAccounts.insertToDataBaseDefaultAccounts()

    return app


app = create_app()