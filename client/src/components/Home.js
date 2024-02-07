import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";


function Home(){
    const [doctors, setDoctors] = useState([]);


    useEffect(() => {
        fetch("/doctors")
          .then((r) => r.json())
          .then(setDoctors);
      }, []);
      return (
        <section>
          <h2>All Doctors</h2>
          <ul>
            {doctors.map((doctor) => (
              <li key={doctor.id}> 
              </li>
            ))}
          </ul>
        </section>
      );
            }

    export default Home;