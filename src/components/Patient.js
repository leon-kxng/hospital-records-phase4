import React, { useEffect, useState } from "react";
import fetchData from "./fetchData";

const Patient = () => {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        fetchData('patient')
            .then(data => setPatients(data))
            .catch(error => console.error('Error fetching patients:', error));
    }, []);

    return (
        <div>
            <h2>All Patients</h2>
            <ul>
                {patients.map(patient => (
                    <li key={patient.id}>
                        <p>Name: {patient.name}</p>
                        <p>Age: {patient.age}</p>
                        <p>Illness: {patient.illness}</p>
                        <p>Doctor: {patient.doctorName}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Patient;