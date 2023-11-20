"""Maintaince Person Service module."""

from typing import Iterator

from src.database.models import MaintenancePerson
from src.database.repositories import MaintenancePersonRepository
from src.database.schemas import MaintaincePersonUpdate


class MaintaincePersonService:

    def __init__(self, maintaince_person_repository: MaintenancePersonRepository) -> None:
        self._repository: MaintenancePersonRepository = maintaince_person_repository

    def get_maintaince_persons(self) -> Iterator[MaintenancePerson]:
        return self._repository.get_all()

    def get_maintaince_person_by_id(self, maintaince_person_id: int) -> MaintenancePerson:
        return self._repository.get_by_id(maintaince_person_id)

    def get_maintaince_person_by_email(self, maintaince_person_email: int) -> MaintenancePerson:
        return self._repository.get_by_email(maintaince_person_email)

    def create_maintaince_person(self, name: str, surname: str, address: str, phone_number: str, email: str, password: str) -> MaintenancePerson:
        return self._repository.add(name, surname, address, phone_number, email, password)
    
    def update_maintaince_person(self, maintaince_person_id: int, maintaince_person: MaintaincePersonUpdate) -> MaintenancePerson:
        db_maintaince_person = self.get_maintaince_person_by_id(maintaince_person_id)
        maintaince_person_data = maintaince_person.model_dump(exclude_none=True)
        for key, value in maintaince_person_data.items():
            setattr(db_maintaince_person, key, value)
        return self._repository.update(maintaince_person=db_maintaince_person)

    def delete_maintaince_person_by_id(self, maintaince_person_id: int) -> None:
        return self._repository.delete_by_id(maintaince_person_id)
