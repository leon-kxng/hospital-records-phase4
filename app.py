from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Doctor, Patient, Hospital
from flask_migrate import Migrate

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
migrate = Migrate(app, db)

# Initialize SQLAlchemy
db.init_app(app)

# Routes

# Home route
@app.route('/')
def home():
    return jsonify({'message': 'Hospital records rule'})

# Doctors routes
@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([{'id': doctor.id, 'name': doctor.name, 'specialty': doctor.speciality} for doctor in doctors])

@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return jsonify({'id': doctor.id, 'name': doctor.name, 'specialty': doctor.speciality})

# Patients routes
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    patient_data = []
    for patient in patients:
        patient_info = {
            'id': patient.id,
            'name': patient.name,
            'age': patient.age,
            'doctors': [{'name': doctor.name, 'specialty': doctor.speciality} for doctor in patient.doctors]
                        if patient.doctors else ["no doctor"]
        }
        patient_data.append(patient_info)
    return jsonify(patient_data)


@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    patient_info = {
        'id': patient.id,
        'name': patient.name,
        'age': patient.age,
        'doctors': [{'name': doctor.name, 'specialty': doctor.speciality} for doctor in patient.doctors]
                    if patient.doctors else ["no doctor"]  # Check if there are doctors for the patient
    }
    return jsonify(patient_info)

# Hospitals routes
@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    hospitals = Hospital.query.all()
    return jsonify([{'id': hospital.id, 'name': hospital.name, 'location': hospital.location} for hospital in hospitals])

@app.route('/hospitals/<int:hospital_id>', methods=['GET'])
def get_hospital(hospital_id):
    hospital = Hospital.query.get_or_404(hospital_id)
    return jsonify({'id': hospital.id, 'name': hospital.name, 'location': hospital.location})

if __name__ == '__main__':
    app.run(port=5555, debug=True)

