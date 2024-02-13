import React, { useEffect, useState } from "react";
import fetchData from "./fetchData";

const Patient = () => {
    const [patients, setPatients] = useState([]);
    const [newPatientName, setNewPatientName] = useState("");
    const [newPatientAge, setNewPatientAge] = useState("");
    const [newPatientIllness, setNewPatientIllness] = useState("");
    const [newPatientDoctorName, setNewPatientDoctorName] = useState("");

    useEffect(() => {
        fetchData('patient')
            .then(data => setPatients(data))
            .catch(error => console.error('Error fetching patients:', error));
    }, []);

    const addPatient = () => {
        if (newPatientName && newPatientAge && newPatientIllness && newPatientDoctorName) {
            const newPatient = {
                id: patients.length + 1, 
                name: newPatientName,
                age: newPatientAge,
                illness: newPatientIllness,
                doctorName: newPatientDoctorName
            };
            setPatients([...patients, newPatient]);
            setNewPatientName("");
            setNewPatientAge("");
            setNewPatientIllness("");
            setNewPatientDoctorName("");
        }
    };

    const deletePatient = (id) => {
        const updatedPatients = patients.filter(patient => patient.id !== id);
        setPatients(updatedPatients);
    };

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
                        <button onClick={() => deletePatient(patient.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <h2>Add Patient</h2>
            <input type="text" value={newPatientName} onChange={(e) => setNewPatientName(e.target.value)} placeholder="Name" />
            <input type="number" value={newPatientAge} onChange={(e) => setNewPatientAge(e.target.value)} placeholder="Age" />
            <input type="text" value={newPatientIllness} onChange={(e) => setNewPatientIllness(e.target.value)} placeholder="Illness" />
            <input type="text" value={newPatientDoctorName} onChange={(e) => setNewPatientDoctorName(e.target.value)} placeholder="Doctor Name" />
            <button onClick={addPatient}>Add Patient</button>
        </div>
    );
};

export default Patient;
