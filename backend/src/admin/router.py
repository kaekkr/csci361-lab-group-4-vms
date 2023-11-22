"""Admin Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.admin.service import AdminService
from src.database.schemas import Admin
from src.containers import Container
from src.auth.auth_bearer import JWTBearer
from src.database.repositories import NotFoundError

router = APIRouter()


@router.get("/", dependencies=[Depends(JWTBearer())])
@inject
def get_list(
    admin_service: AdminService = Depends(Provide[Container.admin_service])
):
    return admin_service.get_admins()


@router.get("/{admin_id}", dependencies=[Depends(JWTBearer())])
@inject
def get_by_id(
    admin_id: int,
    admin_service: AdminService = Depends(Provide[Container.admin_service])
):
    try:
        return admin_service.get_admin_by_id(admin_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    admin: Admin,
    admin_service: AdminService = Depends(
        Provide[Container.admin_service])
):
    return admin_service.create_admin(**admin.model_dump())

@router.delete("/{admin_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        admin_id: int,
        admin_service: AdminService = Depends(
            Provide[Container.admin_service]),
):
    try:
        admin_service.delete_admin_by_id(admin_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
