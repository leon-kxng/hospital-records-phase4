from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Doctor(db.Model):
    __tablename__ ='doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_number = db.Column(db.Integer)
    speciality = db.Column(db.String)
    
    hospital_ = db.relationship('Hospital', backref ='doctor')

    
    def __repr__(self): 
        return f'<hero {self.name} , {self.speciality}>'   
  
class patient(db.Model):
      __tablename__='patients'


      id = db.Column(db.Integer,primary_key = True)
      name = db.Column(db.String)
      age = db.Column(db.Integer)
      illness = db.Column(db.String)
    
      hospital_ =db.relationship('Hospital', backref ='patient')
         
      def __repr__(self) :
           return f' <Power {self.name},{self.illness}>'
    
class Hospital(db.Model):
     __tablename__='hospitals'

    
     id = db.Column(db.Integer, primary_key=True)
     name= db.Column(db.String)
     location = db.Column(db.String)
     doctor_id = db.Column(db.Integer ,db.ForeignKey('doctors.id'))
     patient_id =db.Column(db.Integer, db.ForeignKey('patients.id'))


                                            
               

