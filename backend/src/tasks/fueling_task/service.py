from sqlalchemy.orm import Session
from src.database.models import FuelingTask
from src.database.schemas import FuelingTaskUpdate
from src.database.repositories import FuelingTaskRepository

from typing import Iterator
from datetime import datetime

class FuelingTaskService:
    def __init__(self, fueling_task_repository: FuelingTaskRepository) -> None:
        self._repository = fueling_task_repository

    def get_fueling_tasks(self) -> Iterator[FuelingTask]:
        return self._repository.get_all()

    def get_fueling_task_by_id(self, fueling_task_id: int) -> FuelingTask:
        return self._repository.get_by_id(fueling_task_id)
    
    def get_fueling_tasks_by_driver_id(self, driver_id: int) -> Iterator[FuelingTask]:
        return self._repository.get_by_driver_id(driver_id)

    def get_fueling_tasks_by_fueling_person_id(self, fueling_person_id: int) -> Iterator[FuelingTask]:
        return self._repository.get_by_fueling_person_id(fueling_person_id)

    def get_fueling_tasks_by_vehicle_id(self, vehicle_id: int) -> Iterator[FuelingTask]:
        return self._repository.get_by_vehicle_id(vehicle_id)

    def create_fueling_task(self, fueling_person_id: int, driver_id: int, vehicle_id: int, date: datetime, is_completed: bool, cost: int) -> FuelingTask:
        return self._repository.add(fueling_person_id, driver_id, vehicle_id, date, is_completed, cost)

    def update_fueling_task(self, fueling_task_id: int, fueling_task: FuelingTaskUpdate) -> FuelingTask:
        existing_fueling_task = self.get_fueling_task_by_id(fueling_task_id)
        fueling_data = fueling_task.model_dump(exclude_none=True)
        for key, value in fueling_data.items():
            setattr(existing_fueling_task, key, value)
        return self._repository.update(fueling_task=existing_fueling_task)

    def delete_fueling_task_by_id(self, fueling_task_id: int) -> None:
        self._repository.delete_by_id(fueling_task_id)
