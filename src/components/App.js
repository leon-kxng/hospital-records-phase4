import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import '..//App.css';
import Header from "./Header";
import Doctor from "./Doctor";
import Patient from "./Patient";
import Hospital from "./Hospital";

function App() {
  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route path="/" element={<Hospital />} />
          <Route path="/doctor" element={<Doctor />} />
          <Route path="/patient" element={<Patient />} />
          <Route path="/header" element={<Header />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
