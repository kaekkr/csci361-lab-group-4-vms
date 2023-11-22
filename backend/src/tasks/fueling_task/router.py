
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.database.schemas import FuelingTask, FuelingTaskUpdate
from src.database.repositories import NotFoundError
from src.tasks.fueling_task.service import FuelingTaskService

router = APIRouter()

@router.get("/")
@inject
def get_fueling_tasks(
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    return fueling_task_service.get_fueling_tasks()

@router.get("/{fueling_task_id}")
@inject
def get_fueling_task_by_id(
    fueling_task_id: int,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    try:
        return fueling_task_service.get_fueling_task_by_id(fueling_task_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/by_driver/{driver_id}")
@inject
def get_fueling_tasks_by_driver_id(
    driver_id: int,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    return fueling_task_service.get_fueling_tasks_by_driver_id(driver_id)

@router.get("/by_fueling_person/{fueling_person_id}")
@inject
def get_fueling_tasks_by_fueling_person_id(
    fueling_person_id: int,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    return fueling_task_service.get_fueling_tasks_by_fueling_person_id(fueling_person_id)

@router.get("/by_vehicle/{vehicle_id}")
@inject
def get_fueling_tasks_by_vehicle_id(
    vehicle_id: int,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    return fueling_task_service.get_fueling_tasks_by_vehicle_id(vehicle_id)

@router.post("/", response_model=FuelingTask)
@inject
def create_fueling_task(
    fueling_task: FuelingTask,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    return fueling_task_service.create_fueling_task(**fueling_task.dict())

@router.patch("/{fueling_task_id}", response_model=FuelingTask)
@inject
def update_fueling_task(
    fueling_task_id: int,
    fueling_task: FuelingTaskUpdate,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    return fueling_task_service.update_fueling_task(fueling_task_id, fueling_task)

@router.delete("/{fueling_task_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove_fueling_task_by_id(
    fueling_task_id: int,
    fueling_task_service: FuelingTaskService = Depends(
        Provide[Container.fueling_task_service])
):
    try:
        fueling_task_service.delete_fueling_task_by_id(fueling_task_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)