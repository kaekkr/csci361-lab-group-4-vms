from sqlalchemy import Column, Integer, String

from src.database.database import Base


class Admin(Base):
    __tablename__ = 'admin'
    admin_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String)


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
    password = Column(String)


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
    password = Column(String)


class FuelingPerson(Base):
    __tablename__ = 'fueling_person'
    fueling_person_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String(255))
