import React from 'react';
import { Link } from 'react-router-dom';

const PatientData = ({ patientInfo }) => {
    return (
        <div>
            <h3>{patientInfo.name}</h3>
            <h5>{patientInfo.age}</h5>
            <p>{patientInfo.illness}</p>
            <Link to={`/Doctors/${patientInfo.doctor.id}`}>{patientInfo.doctor.name}</Link>
        </div>
    );
}

export default PatientData;
