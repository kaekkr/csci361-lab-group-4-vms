"""Driver Service module."""

from typing import Iterator

from src.database.models import Driver
from src.database.repositories import DriverRepository


class DriverService:

    def __init__(self, driver_repository: DriverRepository) -> None:
        self._repository: DriverRepository = driver_repository

    def get_drivers(self) -> Iterator[Driver]:
        return self._repository.get_all()

    def get_driver_by_id(self, driver_id: int) -> Driver:
        return self._repository.get_by_id(driver_id)

    def get_driver_by_email(self, driver_email: int) -> Driver:
        return self._repository.get_by_email(driver_email)

    def create_driver(self, name: str, surname: str, address: str, phone_number: str, email: str, driving_license_code: str, password: str) -> Driver:
        return self._repository.add(name, surname, address, phone_number, email, driving_license_code, password)    

    def delete_driver_by_id(self, driver_id: int) -> None:
        return self._repository.delete_by_id(driver_id)
