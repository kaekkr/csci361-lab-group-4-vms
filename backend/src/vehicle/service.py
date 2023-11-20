"""Vehicle Service module."""

from typing import Iterator

from src.database.models import Vehicle
from src.database.schemas import VehicleUpdate
from src.database.repositories import VehicleRepository


class VehicleService:

    def __init__(self, vehicle_repository: VehicleRepository) -> None:
        self._repository: VehicleRepository = vehicle_repository

    def get_vehicles(self) -> Iterator[Vehicle]:
        return self._repository.get_all()

    def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle:
        return self._repository.get_by_id(vehicle_id)

    def create_vehicle(self, model: str, year: int, license_plate: str, sitting_capacity: int) -> Vehicle:
        return self._repository.add(model, year, license_plate, sitting_capacity)
    
    def update_vehicle(self, vechile_id: int, vechile: VehicleUpdate) -> Vehicle:
        db_vehicle = self.get_vehicle_by_id(vechile_id)
        vechile_data = vechile.model_dump(exclude_none=True)
        for key, value in vechile_data.items():
            setattr(db_vehicle, key, value)
        return self._repository.update(vehicle=db_vehicle)

    def delete_vehicle_by_id(self, vehicle_id: int) -> None:
        return self._repository.delete_by_id(vehicle_id)
