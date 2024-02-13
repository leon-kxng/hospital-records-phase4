import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function Home() {
    const [doctors, setDoctors] = useState([]);
    const [newDoctorName, setNewDoctorName] = useState("");
    const [newDoctorSpeciality, setNewDoctorSpeciality] = useState("");

    useEffect(() => {
        fetch("/doctors")
            .then((r) => r.json())
            .then(setDoctors);
    }, []);

    const addDoctor = () => {
        if (newDoctorName && newDoctorSpeciality) {
            const newDoctor = {
                id: doctors.length + 1, 
                name: newDoctorName,
                speciality: newDoctorSpeciality
            };
            setDoctors([...doctors, newDoctor]);
            setNewDoctorName("");
            setNewDoctorSpeciality("");
        }
    };

    const deleteDoctor = (id) => {
        const updatedDoctors = doctors.filter(doctor => doctor.id !== id);
        setDoctors(updatedDoctors);
    };

    return (
        <section>
            <h2>All Doctors</h2>
            <ul>
                {doctors.map((doctor) => (
                    <li key={doctor.id}>
                        <p>{doctor.speciality}</p>
                        <p>{doctor.name}</p>
                        <button onClick={() => deleteDoctor(doctor.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <h2>Add Doctor</h2>
            <input type="text" value={newDoctorName} onChange={(e) => setNewDoctorName(e.target.value)} placeholder="Name" />
            <input type="text" value={newDoctorSpeciality} onChange={(e) => setNewDoctorSpeciality(e.target.value)} placeholder="Speciality" />
            <button onClick={addDoctor}>Add Doctor</button>
        </section>
    );
}

export default Home;
