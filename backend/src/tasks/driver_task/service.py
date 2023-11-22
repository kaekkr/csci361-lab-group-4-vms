"""Admin Service module."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Annotated, Iterator

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
            is_completed: bool, 
            start_location: str, 
            end_location: str
    ) -> DriveTask:
        drive_task = DriveTask(
            driver_id=driver_id,
            date=date,
            isCompleted=is_completed,
            start_location=start_location,
            end_location=end_location
        )
        return self._repository.add(drive_task)
    
    def get_drive_tasks_by_driver_id(self, driver_id: int) -> Iterator[DriveTask]:
        return self._repository.get_by_driver_id(driver_id=driver_id)
    
    def update_drive_task(self, drive_task_id: int, drive_task_update: DriveTaskUpdate) -> DriveTask:
        db_drive_task = self.get_drive_task_by_id(drive_task_id)
        update_data = drive_task_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_drive_task, key, value)
        return self._repository.update(drive_task=db_drive_task)

    def delete_drive_task_by_id(self, drive_task_id: int) -> None:
        return self._repository.delete_by_id(drive_task_id)
