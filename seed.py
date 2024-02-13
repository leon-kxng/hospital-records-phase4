from app import app, db
from models import db, Patient, Hospital, Doctor
import random 
from sqlalchemy import func 


# # Initialize Flask app and SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# db.init_app(app)


with app.app_context():
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
        doctors_data = [
            {"name": "Dr. Smith", "id_number": random.randint(10000, 99999), "speciality": "Cardiology"},
            {"name": "Dr. Johnson", "id_number": random.randint(10000, 99999), "speciality": "Orthopedics"},
            {"name": "Dr. Davis", "id_number": random.randint(10000, 99999), "speciality": "Neurology"},
            {"name": "Dr. Williams", "id_number": random.randint(10000, 99999), "speciality": "Pediatrics"},
            {"name": "Dr. Brown", "id_number": random.randint(10000, 99999), "speciality": "Cardiology"},
            {"name": "Dr. Miller", "id_number": random.randint(10000, 99999), "speciality": "Orthopedics"},
            {"name": "Dr. Wilson", "id_number": random.randint(10000, 99999), "speciality": "Neurology"},
            {"name": "Dr. Anderson", "id_number": random.randint(10000, 99999), "speciality": "Pediatrics"},
            {"name": "Dr. Taylor", "id_number": random.randint(10000, 99999), "speciality": "Cardiology"},
            {"name": "Dr. Moore", "id_number": random.randint(10000, 99999), "speciality": "Orthopedics"}
        ]

        for doctor_info in doctors_data:
            doctor = Doctor(**doctor_info)
            db.session.add(doctor)

        db.session.commit()

        # Patients (Minimum 40 patients with full names)
        patients_data = [
            {"name": "Elijah Davis", "age": 28, "illness": "Sore Throat"},
            {"name": "Grace Johnson", "age": 34, "illness": "Concussion"},
            {"name": "Henry Smith", "age": 42, "illness": "Common Cold"},
            {"name": "Aria Anderson", "age": 29, "illness": "Stomach Flu"},
            {"name": "Sebastian Moore", "age": 38, "illness": "Sprained Ankle"},
            {"name": "Aaliyah Wilson", "age": 46, "illness": "Migraine"},
            {"name": "Jackson Taylor", "age": 31, "illness": "Allergies"},
            {"name": "Amelia Brown", "age": 37, "illness": "Back Pain"},
            {"name": "Benjamin Miller", "age": 26, "illness": "Cough"},
            {"name": "Lily Williams", "age": 44, "illness": "Fever"},
            {"name": "Grayson Davis", "age": 33, "illness": "Broken Leg"},
            {"name": "Zoe Johnson", "age": 41, "illness": "Headache"},
            {"name": "Christopher Smith", "age": 30, "illness": "Flu"},
            {"name": "Penelope Anderson", "age": 35, "illness": "Sprained Wrist"},
            {"name": "Andrew Moore", "age": 39, "illness": "Stomachache"},
            {"name": "Gabriella Wilson", "age": 47, "illness": "Broken Arm"},
            {"name": "Carter Taylor", "age": 32, "illness": "Sore Throat"},
            {"name": "Madison Brown", "age": 40, "illness": "Concussion"},
            {"name": "Nathan Miller", "age": 27, "illness": "Common Cold"},
            {"name": "Evelyn Williams", "age": 43, "illness": "Stomach Flu"},
            {"name": "Owen Davis", "age": 29, "illness": "Sprained Ankle"},
            {"name": "Avery Johnson", "age": 36, "illness": "Migraine"},
            {"name": "Abigail Smith", "age": 45, "illness": "Allergies"},
            {"name": "Lincoln Anderson", "age": 31, "illness": "Back Pain"},
            {"name": "Hazel Moore", "age": 37, "illness": "Cough"},
            {"name": "Matthew Wilson", "age": 26, "illness": "Fever"},
            {"name": "Aubrey Taylor", "age": 44, "illness": "Broken Leg"},
            {"name": "Leo Brown", "age": 33, "illness": "Headache"},
            {"name": "Stella Miller", "age": 41, "illness": "Flu"},
            {"name": "Lucas Williams", "age": 30, "illness": "Sprained Wrist"},
            {"name": "Chloe Davis", "age": 38, "illness": "Stomachache"},
            {"name": "Ethan Johnson", "age": 46, "illness": "Broken Arm"},
            {"name": "Layla Smith", "age": 32, "illness": "Sore Throat"},
            {"name": "Isaac Anderson", "age": 40, "illness": "Concussion"},
            {"name": "Nova Moore", "age": 27, "illness": "Common Cold"},
            {"name": "Mia Wilson", "age": 43, "illness": "Stomach Flu"},
            {"name": "Liam Taylor", "age": 29, "illness": "Sprained Ankle"}
        ]

        for patient_info in patients_data:
            patient = Patient(**patient_info)
            db.session.add(patient)

        db.session.commit()

# Create an application context
with app.app_context():
    # Assigning Patients to Doctors and Auto-populating the doctor_patients table
    for doctor in Doctor.query.all():
        # Get the list of patient IDs already assigned to this doctor
        assigned_patient_ids = [patient.id for patient in doctor.patients]

        # Filter unassigned patients for this doctor
        unassigned_patients = Patient.query.filter(~Patient.id.in_(assigned_patient_ids)).all()

        # Ensure at least one patient is assigned to each doctor
        if not unassigned_patients:
            break

        # Assign a random number of patients to each doctor (between 1 and the remaining unassigned patients)
        num_assigned_patients = random.randint(1, min(5, len(unassigned_patients)))
        
        print(f"Assigning {num_assigned_patients} patients to {doctor.name}")
        
        # Assign patients to the doctor
        assigned_patients = random.sample(unassigned_patients, num_assigned_patients)
        for patient in assigned_patients:
            print(f"Assigned patient {patient.name} to {doctor.name}")
            # Ensure a patient can only have one doctor
            if not patient.doctors:
                doctor.patients.append(patient)

        # Commit changes to the database
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()  # Ensure that the database tables are created
            # seed_data()  # Execute the seed data logic
            db.session.commit()  # Commit the changes to the database
            print('Database seeded successfully!')
        except Exception as e:
            print(f'Error seeding database: {str(e)}')
