import { useEffect, useState } from "react";

const Patient = ( ) => {
    const [patients, setPatients] = useState([])

    useEffect(() => {
        fetch('/patients')
        .then(response => response.json())
        .then(patientsData => setPatients(patientsData))
    }, [])

    const patientList = patients.map(Patient= (<PatientData key={patient.id} patientInfo ={patient}/>))
    return(
        <div>
            { patientList}
        </div>
    )
}

export default Patient;