from src.database.repositories import MaintenanceJobRepository
from src.database.models import MaintenanceJob
from src.database.schemas import MaintenanceJobUpdate
from typing import Iterator

class MaintenanceJobService:
    def __init__(self, maintenance_job_repository: MaintenanceJobRepository) -> None:
        self._repository = maintenance_job_repository

    def get_maintenance_jobs(self) -> Iterator[MaintenanceJob]:
        return self._repository.get_all()

    def get_maintenance_job_by_id(self, maintenance_job_id: int) -> MaintenanceJob:
        return self._repository.get_by_id(maintenance_job_id)

    def get_maintenance_jobs_by_maintenance_task_id(self, maintenance_task_id: int) -> Iterator[MaintenanceJob]:
        return self._repository.get_by_maintenance_task_id(maintenance_task_id)

    def get_maintenance_jobs_by_maintenance_person_id(self, maintenance_person_id: int) -> Iterator[MaintenanceJob]:
        return self._repository.get_by_maintenance_person_id(maintenance_person_id)

    def create_maintenance_job(self, maintenance_task_id: int, maintenance_person_id: int, isCompleted: bool, detail: str, description: str, cost: int) -> MaintenanceJob:
        return self._repository.add(maintenance_task_id, maintenance_person_id, isCompleted, detail, description, cost)

    def update_maintenance_job(self, maintenance_job_id: int, maintenance_job: MaintenanceJobUpdate) -> MaintenanceJob:
        existing_maintenance_job = self.get_maintenance_job_by_id(maintenance_job_id)
        job_data = maintenance_job.model_dump(exclude_none=True)
        for key, value in job_data.items():
            setattr(existing_maintenance_job, key, value)
        return self._repository.update(maintenance_job=existing_maintenance_job)

    def delete_maintenance_job_by_id(self, maintenance_job_id: int) -> None:
        self._repository.delete_by_id(maintenance_job_id)
