"""Containers module."""

from dependency_injector import containers, providers

from src.database.database import Database
from src.database.repositories import UserRepository
from src.user.service import UserService
from src.auth.service import AuthService
from src.config import DATABASE_URL


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".user.router", ".auth.router"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=DATABASE_URL)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )

    auth_service = providers.Factory(
        AuthService,
        user_service = user_service
    )