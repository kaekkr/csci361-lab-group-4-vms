from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, Session
from datetime import datetime

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admin'
    admin_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String(30))

class Driver(Base):
    __tablename__ = 'driver'
    driver_id = Column(Integer, primary_key=True)
    gov_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(50), unique=True)
    driving_license_code = Column(String(20), nullable=False)
    password = Column(String(30))

class Vehicle(Base):
    __tablename__ = "vehicle"
    vehicle_id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    license_plate = Column(String(20), unique=True, nullable=False)
    sitting_capacity = Column(Integer, nullable=False)

class MaintenancePerson(Base):
    __tablename__ = 'maintenance_person'
    maintenance_person_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String(30))

class FuelingPerson(Base):
    __tablename__ = 'fueling_person'
    fueling_person_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String(30))

engine = create_engine('postgresql://postgres:123@localhost:5432/SWE')
Base.metadata.create_all(engine)
session = Session(bind=engine)

admin_data = {
    "name": "John",
    "surname": "Doe",
    "address": "123 Main St",
    "phone_number": "555-1234",
    "email": "john.doe@example.com",
    "password": "adminpass",
}

driver_data = {
    "gov_id": 123456,
    "name": "Jane",
    "surname": "Smith",
    "address": "456 Oak St",
    "phone_number": "555-5678",
    "email": "jane.smith@example.com",
    "driving_license_code": "ABC123",
    "password": "driverpass",
}

vehicle_data = {
    "model": "Sedan",
    "year": 2022,
    "license_plate": "XYZ123",
    "sitting_capacity": 5,
}

maintenance_person_data = {
    "name": "Mike",
    "surname": "Johnson",
    "address": "789 Pine St",
    "phone_number": "555-9876",
    "email": "mike.johnson@example.com",
    "password": "maintenancepass",
}

fueling_person_data = {
    "name": "Alice",
    "surname": "Brown",
    "address": "101 Elm St",
    "phone_number": "555-4321",
    "email": "alice.brown@example.com",
    "password": "fuelingpass",
}

session.add(Admin(**admin_data))
session.add(Driver(**driver_data))
session.add(Vehicle(**vehicle_data))
session.add(MaintenancePerson(**maintenance_person_data))
session.add(FuelingPerson(**fueling_person_data))
session.commit()