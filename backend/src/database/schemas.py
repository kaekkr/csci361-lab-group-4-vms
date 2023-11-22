from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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


class DriveTask(BaseModel):# conint is a constrained int that must be >= 0
    driver_id: int
    isCompleted: bool
    date: datetime
    start_location: str  # constr creates a string of a maximum length
    end_location: str

class DriveTaskUpdate(BaseModel):
    driver_id: Optional[int] = None
    date: Optional[datetime] = None
    isCompleted: Optional[bool] = None
    start_location: Optional[str] = None
    end_location: Optional[str] = None


class FuelingTask(BaseModel):
    fueling_person_id: int
    driver_id: Optional[int] = None 
    vehicle_id: Optional[int] = None
    date: datetime
    isCompleted: bool
    cost: int

class FuelingTaskUpdate(BaseModel):
    fueling_person_id: Optional[int] = None
    driver_id: Optional[int] = None 
    vehicle_id: Optional[int] = None
    date: Optional[datetime] = None
    isCompleted: Optional[bool] = None
    cost: Optional[int] = None



