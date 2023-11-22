"""Drive Task Service module."""

from typing import  Iterator

from src.database.models import DriveTask
from src.database.repositories import DriveTaskRepository
from src.database.schemas import DriveTaskUpdate
from datetime import datetime
from typing import Iterator


class DriveTaskService:

    def __init__(self, drive_task_repository: DriveTaskRepository) -> None:
        self._repository: DriveTaskRepository = drive_task_repository

    def get_drive_tasks(self) -> Iterator[DriveTask]:
        return self._repository.get_all()

    def get_drive_task_by_id(self, drive_task_id: int) -> DriveTask:
        return self._repository.get_by_id(drive_task_id)

    def create_drive_task(
            self,
            driver_id: int,
            date: datetime,
            isCompleted: bool,
            start_location: str,
            end_location: str
    ) -> DriveTask:
        return self._repository.add(driver_id, date, isCompleted, start_location, end_location)

    def get_drive_tasks_by_driver_id(self, driver_id: int) -> Iterator[DriveTask]:
        return self._repository.get_by_driver_id(driver_id)

    def update_drive_task(self, drive_task_id: int, drive_task_update: DriveTaskUpdate) -> DriveTask:
        db_drive_task = self.get_drive_task_by_id(drive_task_id)
        update_data = drive_task_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_drive_task, key, value)
        return self._repository.update(drive_task=db_drive_task)

    def delete_drive_task_by_id(self, drive_task_id: int) -> None:
        return self._repository.delete_by_id(drive_task_id)
