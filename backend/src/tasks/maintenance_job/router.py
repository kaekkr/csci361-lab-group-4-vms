from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.tasks.maintenance_job.service import MaintenanceJobService
from src.database.repositories import NotFoundError
from src.database.schemas import MaintenanceJob, MaintenanceJobUpdate

router = APIRouter()

@router.get("/")
@inject
def get_list(
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    return maintenance_job_service.get_maintenance_jobs()

@router.get("/{maintenance_job_id}")
@inject
def get_by_id(
    maintenance_job_id: int,
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    try:
        return maintenance_job_service.get_maintenance_job_by_id(maintenance_job_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/by_task/{maintenance_task_id}")
@inject
def get_by_maintenance_task_id(
    maintenance_task_id: int,
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    return maintenance_job_service.get_maintenance_jobs_by_maintenance_task_id(maintenance_task_id)

@router.get("/by_person/{maintenance_person_id}")
@inject
def get_by_maintenance_person_id(
    maintenance_person_id: int,
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    return maintenance_job_service.get_maintenance_jobs_by_maintenance_person_id(maintenance_person_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    maintenance_job: MaintenanceJob,
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    return maintenance_job_service.create_maintenance_job(**maintenance_job.model_dump())

@router.patch("/{maintenance_job_id}")
@inject
def update(
    maintenance_job_id: int,
    maintenance_job_update: MaintenanceJobUpdate,
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    return maintenance_job_service.update_maintenance_job(maintenance_job_id, maintenance_job_update)

@router.delete("/{maintenance_job_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
    maintenance_job_id: int,
    maintenance_job_service: MaintenanceJobService = Depends(
        Provide[Container.maintenance_job_service])
):
    try:
        maintenance_job_service.delete_maintenance_job_by_id(maintenance_job_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
