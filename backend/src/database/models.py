from sqlalchemy import(
    Column, Integer, String, Boolean,
    TIMESTAMP, Text, ARRAY, ForeignKey,
    Table
    )
from sqlalchemy.orm import relationship

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

    drive_tasks = relationship("DriveTask", back_populates="driver")
    fueling_tasks = relationship("FuelingTask", back_populates="driver")


class Vehicle(Base):
    __tablename__ = "vehicle"
    vehicle_id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    license_plate = Column(String(20), unique=True, nullable=False)
    sitting_capacity = Column(Integer, nullable=False)

    fueling_tasks = relationship("FuelingTask", back_populates="vehicle")

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

    fueling_tasks = relationship("FuelingTask", back_populates="fueling_person")


# === tasks ===


class DriveTask(Base):
    __tablename__ = 'drive_task'
    drive_task_id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('driver.driver_id'), nullable=False) # foright key
    date = Column(TIMESTAMP, nullable=False)
    isCompleted = Column(Boolean, nullable=False) # enum complete incomplete
    start_location = Column(String(255), nullable=False)
    end_location = Column(String(255), nullable=False)

    # Define the relationship to the 'Driver' table.
    driver = relationship("Driver", back_populates="drive_tasks")
    
class FuelingTask(Base):
    __tablename__ = 'fueling_task'
    fueling_task_id = Column(Integer, primary_key=True)
    fueling_person_id = Column(
        Integer,
        ForeignKey('fueling_person.fueling_person_id'),
        nullable=True
        ) # foreign key nulllable 
    driver_id = Column(
        Integer,
        ForeignKey('driver.driver_id'),
        nullable=True
        ) # foreign key nulllable
    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id'),
        nullable=False
        )# foreign key
    date = Column(TIMESTAMP, nullable=False)
    isCompleted = Column(Boolean, nullable=False)
    cost = Column(Integer, nullable=False)

    fueling_person = relationship("FuelingPerson", back_populates="fueling_tasks")
    driver = relationship("Driver", back_populates="fueling_tasks")
    vehicle = relationship("Vehicle", back_populates="fueling_tasks")


maintenance_task_job_association = Table(
    'maintenance_task_job_association',
    Base.metadata,
    Column('maintenance_task_id', Integer, ForeignKey('maintenance_task.maintenance_task_id')),
    Column('maintenance_job_id', Integer, ForeignKey('maintenance_job.maintenance_job_id'))
)
class MaintenanceTask(Base):
    __tablename__ = 'maintenance_task'
    maintenance_task_id = Column(Integer, primary_key=True)
    maintenance_person_id = Column(Integer, ForeignKey('maintenance_person.maintenance_person_id'), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    isCompleted = Column(Boolean, nullable=False) # enum complete incomplete
    cummulative_cost = Column(Integer, nullable=False)

    maintenance_person = relationship("MaintenancePerson", back_populates="maintenance_tasks")
    # Create a one-to-many relationship with MaintenanceJob using the association table
    jobs = relationship("MaintenanceJob", secondary=maintenance_task_job_association)


class MaintenanceJob(Base):
    __tablename__ = "maintenance_job"
    maintenance_job_id = Column(Integer, primary_key=True)
    maintenance_task_id = Column(Integer, ForeignKey('maintenance_task.maintenance_task_id'))
    maintenance_person_id = Column(Integer, ForeignKey('maintenance_person.maintenance_person_id'))
    isCompleted = Column(Boolean, nullable=False) # enum complete incomplete
    detail = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    cost = Column(Integer, nullable=False)

    task = relationship("MaintenanceTask", back_populates="jobs")
    maintenance_person = relationship("MaintenancePerson", back_populates="maintenance_jobs")




