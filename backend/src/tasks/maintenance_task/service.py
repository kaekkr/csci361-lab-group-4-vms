from src.database.repositories import MaintenanceTaskRepository
from src.database.models import MaintenanceTask
from src.database.schemas import MaintenanceTaskUpdate

from datetime import datetime
from typing import Iterator

class MaintenanceTaskService:
    def __init__(self, maintenance_task_repository: MaintenanceTaskRepository) -> None:
        self._repository = maintenance_task_repository

    def get_maintenance_tasks(self) -> Iterator[MaintenanceTask]:
        return self._repository.get_all()

    def get_maintenance_task_by_id(self, maintenance_task_id: int) -> MaintenanceTask:
        return self._repository.get_by_id(maintenance_task_id)

    def get_maintenance_tasks_by_person_id(self, maintenance_person_id: int) -> Iterator[MaintenanceTask]:
        return self._repository.get_by_person_id(maintenance_person_id)

    def create_maintenance_task(self, maintenance_person_id: int, date: datetime, isCompleted: bool, cummulative_cost: int) -> MaintenanceTask:
        return self._repository.add(maintenance_person_id, date, isCompleted, cummulative_cost)

    def update_maintenance_task(self, maintenance_task_id: int, maintenance_task: MaintenanceTaskUpdate) -> MaintenanceTask:
        existing_maintenance_task = self.get_maintenance_task_by_id(maintenance_task_id)
        task_data = maintenance_task.model_dump(exclude_none=True)
        for key, value in task_data.items():
            setattr(existing_maintenance_task, key, value)
        return self._repository.update(maintenance_task=existing_maintenance_task)

    def delete_maintenance_task_by_id(self, maintenance_task_id: int) -> None:
        self._repository.delete_by_id(maintenance_task_id)
