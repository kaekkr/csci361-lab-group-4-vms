from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.tasks.maintenance_task.service import MaintenanceTaskService
from src.database.repositories import NotFoundError
from src.database.schemas import MaintenanceTask, MaintenanceTaskUpdate

router = APIRouter()

@router.get("/")
@inject
def get_list(
    maintenance_task_service: MaintenanceTaskService = Depends(
        Provide[Container.maintenance_task_service])
):
    return maintenance_task_service.get_maintenance_tasks()

@router.get("/{maintenance_task_id}")
@inject
def get_by_id(
    maintenance_task_id: int,
    maintenance_task_service: MaintenanceTaskService = Depends(
        Provide[Container.maintenance_task_service])
):
    try:
        return maintenance_task_service.get_maintenance_task_by_id(maintenance_task_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/by_maintenance_person_id/{maintenance_person_id}")
@inject
def get_by_person_id(
    maintenance_person_id: int,
    maintenance_task_service: MaintenanceTaskService = Depends(
        Provide[Container.maintenance_task_service])
):
    return maintenance_task_service.get_maintenance_tasks_by_person_id(maintenance_person_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    maintenance_task: MaintenanceTask,
    maintenance_task_service: MaintenanceTaskService = Depends(
        Provide[Container.maintenance_task_service])
):
    return maintenance_task_service.create_maintenance_task(**maintenance_task.model_dump())

@router.patch("/{maintenance_task_id}")
@inject
def update(
    maintenance_task_id: int,
    maintenance_task_update: MaintenanceTaskUpdate,
    maintenance_task_service: MaintenanceTaskService = Depends(
        Provide[Container.maintenance_task_service])
):
    return maintenance_task_service.update_maintenance_task(maintenance_task_id, maintenance_task_update)

@router.delete("/{maintenance_task_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
    maintenance_task_id: int,
    maintenance_task_service: MaintenanceTaskService = Depends(
        Provide[Container.maintenance_task_service])
):
    try:
        maintenance_task_service.delete_maintenance_task_by_id(maintenance_task_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
