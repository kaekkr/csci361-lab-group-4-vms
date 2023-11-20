from pydantic import BaseModel


class Vehicle(BaseModel):
    model: str
    year: int
    license_plate: str
    sitting_capacity: int


class Admin(BaseModel):
    name: str
    surname: str
    address: str
    phone_number: str
    email: str
    password: str


class Driver(BaseModel):
    name: str
    surname: str
    address: str
    phone_number: str
    email: str
    driving_license_code: str
    password: str


class FuelingPerson(BaseModel):
    name: str
    surname: str
    address: str
    phone_number: str
    email: str
    password: str

class MaintaincePerson(BaseModel):
    name: str
    surname: str
    address: str
    phone_number: str
    email: str
    password: str