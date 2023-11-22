"""Drive_Task Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.tasks.driver_task.service import DriveTaskService
from src.database.repositories import NotFoundError
from src.database.schemas import DriveTask, DriveTaskUpdate

router = APIRouter()

@router.get("/")
@inject
def get_list(
    drive_task_service: DriveTaskService = Depends(
        Provide[Container.drive_task_service])
):
    return drive_task_service.get_drive_tasks()

@router.get("/{drive_task_id}")
@inject
def get_by_id(
    drive_task_id: int,
    drive_task_service: DriveTaskService = Depends(
        Provide[Container.drive_task_service])
):
    try:
        return drive_task_service.get_drive_task_by_id(drive_task_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
@router.get("/{driver_id}")
@inject
def get_by_id(
    driver_id: int,
    drive_task_service: DriveTaskService = Depends(
        Provide[Container.drive_task_service])
):
    try:
        return drive_task_service.get_drive_tasks_by_driver_id(driver_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    drive_task: DriveTask,
    drive_task_service: DriveTaskService = Depends(
        Provide[Container.drive_task_service])
):
    return drive_task_service.create_drive_task(**drive_task.model_dump())

@router.patch("/{drive_task_id}")
@inject
def update(
    drive_task_id: int,
    drive_task_update: DriveTaskUpdate,
    drive_task_service: DriveTaskService = Depends(
        Provide[Container.drive_task_service])
):
    return drive_task_service.update_drive_task(drive_task_id, drive_task_update)

@router.delete("/{drive_task_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
    drive_task_id: int,
    drive_task_service: DriveTaskService = Depends(
        Provide[Container.drive_task_service])
):
    try:
        drive_task_service.delete_drive_task_by_id(drive_task_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
