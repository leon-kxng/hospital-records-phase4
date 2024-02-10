import React from 'react';
import { BrowserRouterRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Header from "./Header";
import Doctor from "./Doctor";
import Patient from "./Patient";
import Hospital from "./Hospital";

function App() {
  return (
    <Router>
      <div className='App'>
          <Routes>
            <Route path="/" element= {<Hospital />} />
            <Route path="/doctor" element= {<Home />} />
            <Route path="/patient" element={<Home/>} />
            <Route path="/header" elemnt={<Home/>}/>

          </Routes>
      </div>
    </Router>
        
  );
}

export default App;
