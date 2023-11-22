"""Application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import defaultAccounts
from .containers import Container
from src.admin.router import router as admin_router
from src.auth.router import router as auth_router
from src.driver.router import router as driver_router
from src.maintaince_person.router import router as maintaince_person_router
from src.fueling_person.router import router as fueling_person_router
from src.vehicle.router import router as vehicle_router
from src.tasks.driver_task.router import router as drive_task_router


def create_app() -> FastAPI:
    container = Container()
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
    app.include_router(driver_router, prefix="/driver", tags=["driver"])
    app.include_router(fueling_person_router, prefix="/fueling_person", tags=["fueling person"])
    app.include_router(maintaince_person_router, prefix="/maintaince_person", tags=["maintaince person"])
    app.include_router(vehicle_router, prefix="/vehicle", tags=["vehicle"])
    app.include_router(drive_task_router, prefix="/drive_task", tags= ["drive task"])

    # defaultAccounts.insertToDataBaseDefaultAccounts()

    return app


app = create_app()