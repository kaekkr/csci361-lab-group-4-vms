"""Containers module."""

from dependency_injector import containers, providers

from src.database.database import Database
from src.database.repositories import DriverRepository, VehicleRepository, MaintenancePersonRepository, FuelingPersonRepository
from src.auth.service import AuthService
from src.driver.service import DriverService
from src.maintaince_person.service import MaintaincePersonService
from src.fueling_person.service import FuelingPersonService
from src.config import DATABASE_URL


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[".user.router", ".auth.router", "."])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=DATABASE_URL)

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

    maintenance_person_service = providers.Factory(
        MaintaincePersonService,
        maintenance_person_repository = maintenance_person_repository,
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
        driver_service = driver_service,
        maintenance_person_service = maintenance_person_service,
        fueling_person_service = fueling_person_service
    )
