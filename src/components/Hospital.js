import React, { useEffect, useState } from "react";
import fetchData from "./fetchData";

const Hospital = () => {
    const [hospitals, setHospitals] = useState([]);

    useEffect(() => {
        fetchData('hospital')
            .then(data => setHospitals(data))
            .catch(error => console.error('Error fetching hospitals:', error));
    }, []);

    return (
        <div>
            <h2>All Hospitals</h2>
            <ul>
                {hospitals.map(hospital => (
                    <li key={hospital.id}>
                        <p>Name: {hospital.name}</p>
                        <p>Location: {hospital.location}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Hospital;