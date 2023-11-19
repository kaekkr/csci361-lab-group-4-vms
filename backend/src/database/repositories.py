"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from .models import Admin, Driver, Vehicle, MaintenancePerson, FuelingPerson

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"


class AdminRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Admin]:
        with self.session_factory() as session:
            return session.query(Admin).all()

    def get_by_username(self, username: str) -> Admin:
        with self.session_factory() as session:
            user = session.query(Admin).filter(
                Admin.email == username).first()
            if not user:
                raise UserNotFoundError(username)
            return user

    def get_by_id(self, admin_id: int) -> Admin:
        with self.session_factory() as session:
            user = session.query(Admin).filter(Admin.id == admin_id).first()
            if not user:
                raise UserNotFoundError(admin_id)
            return user

    def add(
            self,
            name: str,
            surname: str,
            address: str,
            phone_number: str,
            email: str,
            password: str
            ) -> Admin:
        with self.session_factory() as session:
            user = Admin(
                name,
                surname,
                address,
                phone_number,
                email,
                password = pwd_context.hash(password)
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    # def delete_by_id(self, user_id: int) -> None:
    #     with self.session_factory() as session:
    #         entity: User = session.query(User).filter(
    #             User.id == user_id).first()
    #         if not entity:
    #             raise UserNotFoundError(user_id)
    #         session.delete(entity)
    #         session.commit()


class DriverRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Driver]:
        with self.session_factory() as session:
            return session.query(Driver).all()

    def get_by_id(self, driver_id: int) -> Driver:
        with self.session_factory() as session:
            driver = session.query(Driver).filter(
                Driver.id == driver_id).first()
            if not driver:
                raise UserNotFoundError(driver_id)
            return driver
        
    def get_by_email(self, driver_email: str) -> Driver:
        with self.session_factory() as session:
            driver = session.query(Driver).filter(
                Driver.email == driver_email).first()
            if not driver:
                raise UserNotFoundError(driver_email)
            return driver

    def add(self, name: str, surname: str, address: str, phone_number: str, email: str, driving_license_code: str, hashed_password: str) -> Driver:
        with self.session_factory() as session:
            driver = Driver(name, surname, address, phone_number,
                            email, driving_license_code, hashed_password)
            session.add(driver)
            session.commit()
            session.refresh(driver)
            return driver

    def delete_by_id(self, driver_id: int) -> None:
        with self.session_factory() as session:
            entity: Driver = session.query(Driver).filter(
                Driver.id == driver_id).first()
            if not entity:
                raise UserNotFoundError(driver_id)
            session.delete(entity)
            session.commit()


class VehicleRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Vehicle]:
        with self.session_factory() as session:
            return session.query(Vehicle).all()

    def get_by_id(self, vehicle_id: int) -> Vehicle:
        with self.session_factory() as session:
            driver = session.query(Vehicle).filter(
                Vehicle.id == vehicle_id).first()
            if not driver:
                raise UserNotFoundError(vehicle_id)
            return driver

    def add(self, model: str, year: int, license_plate: str, sitting_capacity: int) -> Vehicle:
        with self.session_factory() as session:
            vehicle = Vehicle(model, year, license_plate, sitting_capacity)
            session.add(vehicle)
            session.commit()
            session.refresh(vehicle)
            return vehicle

    def delete_by_id(self, vehicle_id: int) -> None:
        with self.session_factory() as session:
            entity: Vehicle = session.query(Vehicle).filter(
                Vehicle.id == vehicle_id).first()
            if not entity:
                raise UserNotFoundError(vehicle_id)
            session.delete(entity)
            session.commit()


class MaintenancePersonRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[MaintenancePerson]:
        with self.session_factory() as session:
            return session.query(MaintenancePerson).all()

    def get_by_id(self, maintenance_person_id: int) -> MaintenancePerson:
        with self.session_factory() as session:
            maintenance_person = session.query(MaintenancePerson).filter(
                MaintenancePerson.id == maintenance_person_id).first()
            if not maintenance_person:
                raise UserNotFoundError(maintenance_person_id)
            return maintenance_person
        
    def get_by_email(self, maintaince_person_email: str) -> MaintenancePerson:
        with self.session_factory() as session:
            maintaince_person = session.query(MaintenancePerson).filter(
                MaintenancePerson.email == maintaince_person_email).first()
            if not maintaince_person:
                raise UserNotFoundError(maintaince_person_email)
            return maintaince_person

    def add(self, name: str, surname: str, address: str, phone_number: str, email: str, hashed_password: str) -> MaintenancePerson:
        with self.session_factory() as session:
            maintenance_person = MaintenancePerson(name, surname, address, phone_number,
                                                   email, hashed_password)
            session.add(maintenance_person)
            session.commit()
            session.refresh(maintenance_person)
            return maintenance_person

    def delete_by_id(self, maintenance_person_id: int) -> None:
        with self.session_factory() as session:
            entity: MaintenancePerson = session.query(Vehicle).filter(
                MaintenancePerson.id == maintenance_person_id).first()
            if not entity:
                raise UserNotFoundError(maintenance_person_id)
            session.delete(entity)
            session.commit()


class FuelingPersonRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[FuelingPerson]:
        with self.session_factory() as session:
            return session.query(FuelingPerson).all()

    def get_by_id(self, fueling_person_id: int) -> FuelingPerson:
        with self.session_factory() as session:
            fueling_person = session.query(FuelingPerson).filter(
                FuelingPerson.id == fueling_person_id).first()
            if not fueling_person:
                raise UserNotFoundError(fueling_person_id)
            return fueling_person
        
    def get_by_email(self, fueling_person_email: str) -> FuelingPerson:
        with self.session_factory() as session:
            fueling_person = session.query(FuelingPerson).filter(
                FuelingPerson.email == fueling_person_email).first()
            if not fueling_person:
                raise UserNotFoundError(fueling_person_email)
            return fueling_person

    def add(self, name: str, surname: str, address: str, phone_number: str, email: str, hashed_password: str) -> MaintenancePerson:
        with self.session_factory() as session:
            fueling_person = FuelingPerson(name, surname, address, phone_number,
                                           email, hashed_password)
            session.add(fueling_person)
            session.commit()
            session.refresh(fueling_person)
            return fueling_person

    def delete_by_id(self, fueling_person_id: int) -> None:
        with self.session_factory() as session:
            entity: FuelingPerson = session.query(Vehicle).filter(
                FuelingPerson.id == fueling_person_id).first()
            if not entity:
                raise UserNotFoundError(fueling_person_id)
            session.delete(entity)
            session.commit()
