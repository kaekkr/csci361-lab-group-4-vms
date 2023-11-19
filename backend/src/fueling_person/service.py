"""User Service module."""

from typing import Iterator

from src.database.models import FuelingPerson
from src.database.repositories import FuelingPersonRepository


class FuelingPersonService:

    def __init__(self, fueling_person_repository: FuelingPersonRepository) -> None:
        self._repository: FuelingPersonRepository = fueling_person_repository

    def get_fueling_persons(self) -> Iterator[FuelingPerson]:
        return self._repository.get_all()

    def get_fueling_person_by_id(self, fueling_person_id: int) -> FuelingPerson:
        return self._repository.get_by_id(fueling_person_id)

    def get_fueling_person_by_email(self, fueling_person_email: int) -> FuelingPerson:
        return self._repository.get_by_email(fueling_person_email)

    def create_fueling_person(self, name: str, surname: str, address: str, phone_number: str, email: str, hashed_password: str) -> FuelingPerson:
        return self._repository.add(name, surname, address, phone_number, email, hashed_password)

    def delete_fueling_person_by_id(self, fueling_person_id: int) -> None:
        return self._repository.delete_by_id(fueling_person_id)
