const PatientData = ( {patientInfo}) => {
    return (
        <div>
                <h3>{patientsInfo.name}</h3>
                <h5>{patientsInfo.age}</h5>
                <p>{patientsInfo.illness}</p>
               < Link to ={`/Doctors/${doctor.id}`}>{doctor.name}</Link> 
        </div>
    )
}