"""Driver Service module."""

from typing import Iterator

from src.database.models import Driver
from src.database.repositories import DriverRepository
from src.database.schemas import DriverUpdate


class DriverService:

    def __init__(self, driver_repository: DriverRepository) -> None:
        self._repository: DriverRepository = driver_repository

    def get_drivers(self) -> Iterator[Driver]:
        return self._repository.get_all()

    def get_driver_by_id(self, driver_id: int) -> Driver:
        return self._repository.get_by_id(driver_id)

    def get_driver_by_email(self, driver_email: int) -> Driver:
        return self._repository.get_by_email(driver_email)

    def create_driver(self, gov_id: int, name: str, surname: str, address: str, phone_number: str, email: str, driving_license_code: str, password: str) -> Driver:
        return self._repository.add(gov_id, name, surname, address, phone_number, email, driving_license_code, password)

    def update_driver(self, driver_id: int, driver: DriverUpdate) -> Driver:
        db_driver = self.get_driver_by_id(driver_id)
        driver_data = driver.model_dump(exclude_none=True)
        for key, value in driver_data.items():
            setattr(db_driver, key, value)
        return self._repository.update(driver=db_driver)

    def delete_driver_by_id(self, driver_id: int) -> None:
        return self._repository.delete_by_id(driver_id)
