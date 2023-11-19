"""User Service module."""

from src.database.models import MaintenancePerson
from src.database.repositories import MaintenancePersonRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Annotated, Iterator
from uuid import uuid4

from src.auth.models import TokenData
from src.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class MaintaincePersonService:

    def __init__(self, maintaince_person_repository: MaintenancePersonRepository) -> None:
        self._repository: MaintenancePersonRepository = maintaince_person_repository

    def get_maintaince_person(self) -> Iterator[MaintenancePerson]:
        return self._repository.get_all()

    def get_maintaince_person_by_id(self, maintaince_person_id: int) -> MaintenancePerson:
        return self._repository.get_by_id(maintaince_person_id)

    def get_maintaince_person_by_email(self, maintaince_person_email: int) -> MaintenancePerson:
        return self._repository.get_by_email(maintaince_person_email)

    def create_maintaince_person(self, name: str, surname: str, address: str, phone_number: str, email: str, hashed_password: str) -> MaintenancePerson:
        return self._repository.add(name, surname, address, phone_number, email, hashed_password)

    def delete_maintaince_person_by_id(self, maintaince_person_id: int) -> None:
        return self._repository.delete_by_id(maintaince_person_id)
