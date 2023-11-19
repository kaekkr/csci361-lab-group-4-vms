"""User Service module."""

from src.database.models import Driver
from src.database.repositories import DriverRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Annotated, Iterator

from src.auth.models import TokenData
from src.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class DriverService:

    def __init__(self, driver_repository: DriverRepository) -> None:
        self._repository: DriverRepository = driver_repository

    def get_drivers(self) -> Iterator[Driver]:
        return self._repository.get_all()

    def get_driver_by_id(self, driver_id: int) -> Driver:
        return self._repository.get_by_id(driver_id)
    
    def get_driver_by_username(self, driver_username: int) -> Driver:
        return self._repository.get_by_username(driver_username)

    def create_driver(self, name: str, surname: str, address: str, phone_number: str, email: str, driving_license_code: str, hashed_password: str) -> Driver:
        return self._repository.add(name, surname, address, phone_number, email, driving_license_code, hashed_password)

    def delete_driver_by_id(self, driver_id: int) -> None:
        return self._repository.delete_by_id(driver_id)
