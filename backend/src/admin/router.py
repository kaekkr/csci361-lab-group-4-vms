"""User Endpoints module."""

from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
# from dependency_injector.wiring import inject, Provide

from .service import AdminService
from src.database.models import Admin

router = APIRouter()

@router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[Admin, Depends(AdminService.get_current_active_user)]
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[Admin, Depends(AdminService.get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

# @router.get("register/driver")
# def register_driver(
    
# ):