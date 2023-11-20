"""Fueling Person Service module."""

from typing import Iterator

from src.database.models import FuelingPerson
from src.database.repositories import FuelingPersonRepository
from src.database.schemas import FuelingPersonUpdate


class FuelingPersonService:

    def __init__(self, fueling_person_repository: FuelingPersonRepository) -> None:
        self._repository: FuelingPersonRepository = fueling_person_repository

    def get_fueling_persons(self) -> Iterator[FuelingPerson]:
        return self._repository.get_all()

    def get_fueling_person_by_id(self, fueling_person_id: int) -> FuelingPerson:
        return self._repository.get_by_id(fueling_person_id)

    def get_fueling_person_by_email(self, fueling_person_email: int) -> FuelingPerson:
        return self._repository.get_by_email(fueling_person_email)

    def create_fueling_person(self, name: str, surname: str, address: str, phone_number: str, email: str, password: str) -> FuelingPerson:
        return self._repository.add(name, surname, address, phone_number, email, password)

    def update_fueling_person(self, fueling_person_id: int, fueling_person: FuelingPersonUpdate) -> FuelingPerson:
        db_fueling_person = self.get_fueling_person_by_id(fueling_person_id)
        fueling_person_data = fueling_person.model_dump(exclude_none=True)
        for key, value in fueling_person_data.items():
            setattr(db_fueling_person, key, value)
        return self._repository.update(fueling_person=db_fueling_person)

    def delete_fueling_person_by_id(self, fueling_person_id: int) -> None:
        return self._repository.delete_by_id(fueling_person_id)
