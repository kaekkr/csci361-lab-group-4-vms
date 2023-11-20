"""Admin Service module."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Annotated, Iterator

from src.database.models import Admin
from src.database.repositories import AdminRepository
from src.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AdminService:

    def __init__(self, admin_repository: AdminRepository) -> None:
        self._repository: AdminRepository = admin_repository

    def get_admins(self) -> Iterator[Admin]:
        return self._repository.get_all()

    def get_admin_by_id(self, admin_id: int) -> Admin:
        return self._repository.get_by_id(admin_id)

    def get_admin_by_email(self, email: str) -> Admin:
        return self._repository.get_by_email(email)

    def create_admin(self, name: str,
                     surname: str,
                     address: str,
                     phone_number: str,
                     email: str,
                     password: str) -> Admin:
        return self._repository.add(name, surname, address, phone_number, email, password)

    def delete_admin_by_id(self, vehicle_id: int) -> None:
        return self._repository.delete_by_id(vehicle_id)
