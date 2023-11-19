"""Driver Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.driver.service import DriverService

router = APIRouter()

@router.get("/")
@inject
def get_list(
  driver_service: DriverService = Depends(Provide[Container.driver_service])
):
  return driver_service.get_drivers()


