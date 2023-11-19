"""Admin Endpoints module."""

from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.admin.service import AdminService
from src.database.models import Admin
from src.containers import Container
from src.auth.auth_bearer import JWTBearer

router = APIRouter()


@router.get("/", dependencies=[Depends(JWTBearer())])
@inject
def get_list(
    admin_service: AdminService = Depends(Provide[Container.admin_service])
):
    return admin_service.get_admins()


# @router.get("register/driver")
# def register_driver(

# ):
