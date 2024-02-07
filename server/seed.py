#!/usr/bin/env python3

from app import db
from models import Patient, Hospital, Doctor, doctor_patients
import random
from sqlalchemy import func

with db.app.app_context():
    # Delete existing data
    db.session.query(doctor_patients).delete()
    Patient.query.delete()
    Hospital.query.delete()
    Doctor.query.delete()

    # Hospitals
    hospitals_data = [
        {"name": "General Hospital", "location": "City Center"},
        {"name": "Grace Hospital", "location": "Suburb Area"},
        {"name": "Unity Medical Center", "location": "Downtown"}
    ]

    for hospital_info in hospitals_data:
        hospital = Hospital(**hospital_info)
        db.session.add(hospital)

    # Doctors
    for _ in range(10):  # Add 10 doctors
        doctor_info = {
            "name": f"Dr. {random.choice(['Smith', 'Johnson', 'Davis', 'Williams', 'Brown'])}",
            "id_number": random.randint(10000, 99999),
            "speciality": random.choice(['Cardiology', 'Orthopedics', 'Neurology', 'Pediatrics'])
        }
        doctor = Doctor(**doctor_info)
        db.session.add(doctor)

    db.session.commit()

    # Patients
    for _ in range(40):  # Add 40 patients
        patient_info = {
            "name": f"{random.choice(['John', 'Jane', 'Sam', 'Emily', 'Michael'])} {random.choice(['Doe', 'Smith', 'Johnson', 'Williams'])}",
            "age": random.randint(18, 70),
            "illness": random.choice(['Fever', 'Broken Leg', 'Migraine', 'Flu', 'Allergies'])
        }
        patient = Patient(**patient_info)
        db.session.add(patient)

    db.session.commit()

    # Assigning Patients to Doctors and Auto-populating doctor_patients table
    for doctor in Doctor.query.all():
        for _ in range(random.randint(1, 5)):  # Randomly assign 1 to 5 patients to each doctor
            patient = Patient.query.order_by(func.random()).first()
            doctor.patients.append(patient)

    db.session.commit()
