from pydantic import BaseModel
from typing import Optional


class Vehicle(BaseModel):
    model: str
    year: int
    license_plate: str
    sitting_capacity: int

class VehicleUpdate(BaseModel):
    model: Optional[str]
    year: Optional[int]
    license_plate: Optional[str]
    sitting_capacity: Optional[int]

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


class DriverUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    driving_license_code: Optional[str] = None
    password: Optional[str] = None


class FuelingPerson(BaseModel):
    name: str
    surname: str
    address: str
    phone_number: str
    email: str
    password: str


class FuelingPersonUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class MaintaincePerson(BaseModel):
    name: str
    surname: str
    address: str
    phone_number: str
    email: str
    password: str


class MaintaincePersonUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
