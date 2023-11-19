"""Fueling Person Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.fueling_person.service import FuelingPersonService

router = APIRouter()

@router.get("/")
@inject
def get_list(
  fueling_person_service: FuelingPersonService = Depends(Provide[Container.fueling_person_service])
):
  return fueling_person_service.get_fueling_persons()


