"""Fueling Person Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.fueling_person.service import FuelingPersonService
from src.database.repositories import NotFoundError
from src.database.schemas import FuelingPerson, FuelingPersonUpdate

router = APIRouter()


@router.get("/")
@inject
def get_list(
    fueling_person_service: FuelingPersonService = Depends(
        Provide[Container.fueling_person_service])
):
    return fueling_person_service.get_fueling_persons()


@router.get("/{fueling_person_id}")
@inject
def get_by_id(
    fueling_person_id: int,
    fueling_person_service: FuelingPersonService = Depends(
        Provide[Container.fueling_person_service])
):
    try:
        return fueling_person_service.get_fueling_person_by_id(fueling_person_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    fueling_person: FuelingPerson,
    fueling_person_service: FuelingPersonService = Depends(
        Provide[Container.fueling_person_service])
):
    return fueling_person_service.create_fueling_person(**fueling_person.model_dump())

@router.patch("/{fueling_person_id}")
@inject
def update(
    fueling_person_id: int,
    fueling_person: FuelingPersonUpdate,
    fueling_person_service: FuelingPersonService = Depends(
        Provide[Container.fueling_person_service])
):
    return fueling_person_service.update_fueling_person(fueling_person_id, fueling_person)


@router.delete("/{fueling_person_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        fueling_person_id: int,
        fueling_person_service: FuelingPersonService = Depends(
            Provide[Container.fueling_person_service]),
):
    try:
        fueling_person_service.delete_fueling_person_by_id(fueling_person_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
