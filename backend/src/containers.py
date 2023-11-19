"""Containers module."""

from dependency_injector import containers, providers

from src.database.database import Database
from src.database.repositories import (
    AdminRepository,
    DriverRepository,
    VehicleRepository,
    MaintenancePersonRepository,
    FuelingPersonRepository
)
from src.admin.service import AdminService
from src.auth.service import AuthService
from src.driver.service import DriverService
from src.maintaince_person.service import MaintaincePersonService
from src.fueling_person.service import FuelingPersonService
from src.config import DATABASE_URL


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[".admin.router", ".auth.router", "."])

    db = providers.Singleton(Database, db_url=DATABASE_URL)

    admin_repository = providers.Factory(
        AdminRepository,
        session_factory = db.provided.session
    )

    admin_service = providers.Factory(
        AdminService,
        admin_repository = admin_repository
    )

    driver_repository = providers.Factory(
        DriverRepository,
        session_factory = db.provided.session,
    )

    driver_service = providers.Factory(
        DriverService,
        driver_repository = driver_repository,
    )

    vehicle_repository = providers.Factory(
        VehicleRepository,
        session_factory = db.provided.session,
    )

    maintenance_person_repository = providers.Factory(
        MaintenancePersonRepository,
        session_factory = db.provided.session,
    )

    maintaince_person_service = providers.Factory(
        MaintaincePersonService,
        maintaince_person_repository = maintenance_person_repository,
    )

    fueling_person_repository = providers.Factory(
        FuelingPersonRepository,
        session_factory = db.provided.session,
    )

    fueling_person_service = providers.Factory(
        FuelingPersonService,
        fueling_person_repository = fueling_person_repository,
    )

    auth_service = providers.Factory(
        AuthService,
        admin_service = admin_service,
        driver_service = driver_service,
        maintaince_person_service = maintaince_person_service,
        fueling_person_service = fueling_person_service
    )
