from .database import Database

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