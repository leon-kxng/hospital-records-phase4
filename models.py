from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for many-to-many relationship between Doctor and Patient
doctor_patients = db.Table(
    'doctor_patients',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctor.id'), primary_key=True),
    db.Column('patient_id', db.Integer, db.ForeignKey('patient.id'), primary_key=True)
)

# Define Doctor model
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    id_number = db.Column(db.Integer, nullable=False)
    speciality = db.Column(db.String(50), nullable=False)

    # Establishing one-to-many relationship
    patients = db.relationship('Patient', secondary=doctor_patients, back_populates='doctors')

# Define Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    illness = db.Column(db.String(50), nullable=False)

    # Establishing one-to-many relationship
    doctors = db.relationship('Doctor', secondary=doctor_patients, back_populates='patients')

# Define Hospital model
class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
