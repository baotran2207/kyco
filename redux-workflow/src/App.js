import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './features/User/Login';
import Signup from './features/User/Signup';
import Dashboard from './features/User/Dashboard';
import { PrivateRoute } from './helpers/PrivateRoute';

console.log(process.env.REACT_APP_API_URL);
function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          {/* <Route exact component={Login} path="/login" />
          <Route exact component={Signup} path="/signup" /> */}
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          {/* <Route exact element={<PrivateRoute />}>
            <Route exact path="/" element={<Dashboard />} />
          </Route> */}
        </Routes>
      </Router>
    </div>
  );
}

export default App;
