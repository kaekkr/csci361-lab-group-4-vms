"""Vehicle Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.vehicle.service import VehicleService
from src.database.schemas import Vehicle, VehicleUpdate
from src.database.repositories import NotFoundError

router = APIRouter()


@router.get("/")
@inject
def get_list(
    vehicle_service: VehicleService = Depends(
        Provide[Container.vehicle_service])
):
    return vehicle_service.get_vehicles()


@router.get("/{vehicle_id}")
@inject
def get_by_id(
    vehicle_id: int,
    vehicle_service: VehicleService = Depends(
        Provide[Container.vehicle_service])
):
    try:
        return vehicle_service.get_vehicle_by_id(vehicle_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    vehicle: Vehicle,
    vehicle_service: VehicleService = Depends(
        Provide[Container.vehicle_service])
):
    return vehicle_service.create_vehicle(**vehicle.model_dump())

@router.patch("/{vehicle_id}")
@inject
def update(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    vehicle_service: VehicleService = Depends(
        Provide[Container.vehicle_service])
):
    return vehicle_service.update_vehicle(vehicle_id, vehicle)


@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        vehicle_id: int,
        vehicle_service: VehicleService = Depends(
            Provide[Container.vehicle_service]),
):
    try:
        vehicle_service.delete_vehicle_by_id(vehicle_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
