"""Maintaince Person Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.maintaince_person.service import MaintaincePersonService
from src.database.repositories import NotFoundError
from src.database.schemas import MaintaincePerson, MaintaincePersonUpdate

router = APIRouter()


@router.get("/")
@inject
def get_list(
    maintaince_person_service: MaintaincePersonService = Depends(
        Provide[Container.maintaince_person_service])
):
    return maintaince_person_service.get_maintaince_persons()


@router.get("/{maintaince_person_id}")
@inject
def get_by_id(
    maintaince_person_id: int,
    maintaince_person_service: MaintaincePersonService = Depends(
        Provide[Container.maintaince_person_service])
):
    try:
        return maintaince_person_service.get_maintaince_person_by_id(maintaince_person_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    maintaince_person: MaintaincePerson,
    maintaince_person_service: MaintaincePersonService = Depends(
        Provide[Container.maintaince_person_service])
):
    return maintaince_person_service.create_maintaince_person(**maintaince_person.model_dump())


@router.patch("/{maintaince_person_id}")
@inject
def update(
    maintaince_person_id: int,
    maintaince_person: MaintaincePersonUpdate,
    maintaince_person_service: MaintaincePersonService = Depends(
        Provide[Container.maintaince_person_service])
):
    return maintaince_person_service.update_maintaince_person(maintaince_person_id, maintaince_person)


@router.delete("/{maintaince_person_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        maintaince_person_id: int,
        maintaince_person_service: MaintaincePersonService = Depends(
            Provide[Container.maintaince_person_service]),
):
    try:
        maintaince_person_service.delete_maintaince_person_by_id(
            maintaince_person_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
