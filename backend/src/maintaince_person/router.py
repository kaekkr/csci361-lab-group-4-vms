"""Maintaince Person Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.maintaince_person.service import MaintaincePersonService

router = APIRouter()

@router.get("/")
@inject
def get_list(
  maintaince_person_service: MaintaincePersonService = Depends(Provide[Container.maintaince_person_service])
):
  return maintaince_person_service.get_maintaince_persons()


