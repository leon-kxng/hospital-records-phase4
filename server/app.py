from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

doctor_patients = db.Table( 
    'doctor_patients',
    db.Column('doctors_id', db.Integer, db.ForeignKey('doctors.id'), primary_key=True),
    db.Column('patients_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True)
)

class Doctor(db.Model):
    __tablename__ ='doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_number = db.Column(db.Integer)
    speciality = db.Column(db.String)
    
    hospital_ = db.relationship('Hospital', backref ='doctor')
    patients = db.relationship('Patient', secondary=doctor_patients, back_populates='doctors')

class Patient(db.Model):
    __tablename__='patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    illness = db.Column(db.String)
    
    hospital_ = db.relationship('Hospital', backref ='patient')
    doctors = db.relationship('Doctor', secondary=doctor_patients, back_populates='patients')

class Hospital(db.Model):
    __tablename__='hospitals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

# Routes

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Hospital Management System!'})

# Get all hospitals
@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    hospitals = Hospital.query.all()
    return jsonify([{'id': hospital.id, 'name': hospital.name, 'location': hospital.location} for hospital in hospitals])

# Get a specific hospital
@app.route('/hospitals/<int:hospital_id>', methods=['GET'])
def get_hospital(hospital_id):
    hospital = Hospital.query.get(hospital_id)

    if not hospital:
        return jsonify({'error': 'Hospital not found'}), 404

    hospital_data = {
        'id': hospital.id,
        'name': hospital.name,
        'location': hospital.location,
        'doctors': [{'id': doctor.id, 'name': doctor.name, 'speciality': doctor.speciality} for doctor in hospital.doctor],
        'patients': [{'id': patient.id, 'name': patient.name, 'age': patient.age, 'illness': patient.illness} for patient in hospital.patient],
        'doctor_patients': [{'doctor_id': relation.doctor_id, 'patient_id': relation.patient_id} for relation in doctor_patients.query.filter(doctor_patients.c.doctor_id == hospital.doctor_id).all()]
    }

    return jsonify(hospital_data)

# Get all doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([{'id': doctor.id, 'name': doctor.name, 'speciality': doctor.speciality} for doctor in doctors])

# Get a specific doctor
@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    try:
        doctor = Doctor.query.get(doctor_id)

        if not doctor:
            return jsonify({'error': 'Doctor not found'}), 404

        doctor_data = {
            'id': doctor.id,
            'name': doctor.name,
            'speciality': doctor.speciality,
            'hospital': {'id': doctor.hospital.id, 'name': doctor.hospital.name, 'location': doctor.hospital.location},
            'patients': [{'id': patient.id, 'name': patient.name, 'age': patient.age, 'illness': patient.illness} for patient in doctor.patients],
            'doctor_patients': [{'doctor_id': relation.doctor_id, 'patient_id': relation.patient_id} for relation in doctor_patients.query.filter(doctor_patients.c.doctor_id == doctor.id).all()]
        }

        return jsonify(doctor_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{'id': patient.id, 'name': patient.name, 'age': patient.age, 'illness': patient.illness} for patient in patients])

# Get a specific patient
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    try:
        patient = Patient.query.get(patient_id)

        if not patient:
            return jsonify({'error': 'Patient not found'}), 404

        patient_data = {
            'id': patient.id,
            'name': patient.name,
            'age': patient.age,
            'illness': patient.illness,
            'hospital': {'id': patient.hospital.id, 'name': patient.hospital.name, 'location': patient.hospital.location},
            'doctors': [{'id': doctor.id, 'name': doctor.name, 'speciality': doctor.speciality} for doctor in patient.doctors],
            'doctor_patients': [{'doctor_id': relation.doctor_id, 'patient_id': relation.patient_id} for relation in doctor_patients.query.filter(doctor_patients.c.patient_id == patient.id).all()]
        }

        return jsonify(patient_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all doctor_patient relationships
@app.route('/doctor_patients', methods=['GET'])
def get_doctor_patients():
    try:
        doctor_patients_data = [{'doctor_id': relation.doctor_id, 'patient_id': relation.patient_id} for relation in doctor_patients.query.all()]
        return jsonify({'doctor_patients': doctor_patients_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific doctor_patient relationship
@app.route('/doctor_patients/<int:doctor_id>/<int:patient_id>', methods=['GET'])
def get_doctor_patient(doctor_id, patient_id):
    try:
        doctor_patient = doctor_patients.query.filter(doctor_patients.c.doctor_id == doctor_id, doctor_patients.c.patient_id == patient_id).first()

        if not doctor_patient:
            return jsonify({'error': 'Doctor-Patient relationship not found'}), 404

        doctor_patient_data = {'doctor_id': doctor_patient.doctor_id, 'patient_id': doctor_patient.patient_id}
        return jsonify(doctor_patient_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5555)
