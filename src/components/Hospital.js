import { useEffect, useState } from "react";

const Hospital = ( ) => {
    const [hospitals, sethospitals] = useState([])

    useEffect(() => {
        fetch('/hospitals')
        .then(response => response.json())
        .then(hospitalsData => sethospitals(hospitalsData))
    }, [])


    return (
        <>
         <h2>{hospital.name}</h2>
         <p>{hospital.location}</p>
        </>

    )
}

export default Hospital ;