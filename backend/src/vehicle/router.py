"""Vehicle Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.vehicle.service import VehicleService

router = APIRouter()

@router.get("/")
@inject
def get_list(
  vehicle_service: VehicleService = Depends(Provide[Container.vehicle_service])
):
  return vehicle_service.get_vehicles()


