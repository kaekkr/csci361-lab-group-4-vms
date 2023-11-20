"""Driver Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.driver.service import DriverService
from src.database.repositories import NotFoundError
from src.database.schemas import Driver, DriverUpdate

router = APIRouter()


@router.get("/")
@inject
def get_list(
    driver_service: DriverService = Depends(Provide[Container.driver_service])
):
    return driver_service.get_drivers()


@router.get("/{driver_id}")
@inject
def get_by_id(
    driver_id: int,
    driver_service: DriverService = Depends(Provide[Container.driver_service])
):
    try:
        return driver_service.get_driver_by_id(driver_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    driver: Driver,
    driver_service: DriverService = Depends(
        Provide[Container.driver_service])
):
    return driver_service.create_driver(**driver.model_dump())


@router.patch("/{driver_id}")
@inject
def update(
    driver_id: int,
    driver: DriverUpdate,
    driver_service: DriverService = Depends(
        Provide[Container.driver_service])
):
    return driver_service.update_driver(driver_id, driver)


@router.delete("/{driver_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        driver_id: int,
        driver_service: DriverService = Depends(
            Provide[Container.driver_service]),
):
    try:
        driver_service.delete_driver_by_id(driver_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
