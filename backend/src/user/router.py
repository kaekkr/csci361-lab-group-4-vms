from fastapi import APIRouter, Depends
from typing import Annotated

from src.database.schemas import User as UserSchema
from src.user.service import get_current_active_user

router = APIRouter()

@router.get("/users/me/", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_active_user)]
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[UserSchema, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]