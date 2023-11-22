"""Containers module."""

from dependency_injector import containers, providers

from src.database.database import Database
from src.database.repositories import (
    AdminRepository,
    DriverRepository,
    VehicleRepository,
    MaintenancePersonRepository,
    FuelingPersonRepository,
    DriveTaskRepository,
    FuelingTaskRepository
)
from src.admin.service import AdminService
from src.auth.service import AuthService
from src.driver.service import DriverService
from src.maintaince_person.service import MaintaincePersonService
from src.fueling_person.service import FuelingPersonService
from src.vehicle.service import VehicleService
from src.config import DATABASE_URL
from src.tasks.driver_task.service import DriveTaskService
from src.tasks.fueling_task.service import FuelingTaskService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            ".admin.router", ".auth.router", ".driver.router",
            ".maintaince_person.router", ".fueling_person.router", 
            ".vehicle.router", ".tasks.driver_task.router",
            ".tasks.fueling_task.router" 
            ]
            )

    db = providers.Singleton(Database, db_url=DATABASE_URL)

    admin_repository = providers.Factory(
        AdminRepository,
        session_factory=db.provided.session
    )

    admin_service = providers.Factory(
        AdminService,
        admin_repository=admin_repository
    )

    driver_repository = providers.Factory(
        DriverRepository,
        session_factory=db.provided.session,
    )

    driver_service = providers.Factory(
        DriverService,
        driver_repository=driver_repository,
    )

    vehicle_repository = providers.Factory(
        VehicleRepository,
        session_factory=db.provided.session,
    )

    vehicle_service = providers.Factory(
        VehicleService,
        vehicle_repository=vehicle_repository
    )

    maintenance_person_repository = providers.Factory(
        MaintenancePersonRepository,
        session_factory=db.provided.session,
    )

    maintaince_person_service = providers.Factory(
        MaintaincePersonService,
        maintaince_person_repository=maintenance_person_repository,
    )

    fueling_person_repository = providers.Factory(
        FuelingPersonRepository,
        session_factory=db.provided.session,
    )

    fueling_person_service = providers.Factory(
        FuelingPersonService,
        fueling_person_repository=fueling_person_repository,
    )

    auth_service = providers.Factory(
        AuthService,
        admin_service=admin_service,
        driver_service=driver_service,
        maintaince_person_service=maintaince_person_service,
        fueling_person_service=fueling_person_service
    )

    drive_task_repository = providers.Factory(
        DriveTaskRepository,
        session_factory=db.provided.session,
    )

    drive_task_service = providers.Factory(
        DriveTaskService,
        drive_task_repository=drive_task_repository
    )

    fueling_task_repository = providers.Factory(
        FuelingTaskRepository,
        session_factory=db.provided.session,
    )

    fueling_task_service = providers.Factory(
        FuelingTaskService, 
        fueling_task_repository=fueling_task_repository
    )
