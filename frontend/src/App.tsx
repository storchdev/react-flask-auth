import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Logout from './Logout';
import Register from './Register';
import Home from './Home';
import Navbar from './Navbar';
import ProtectedRoute from './ProtectedRoute';
import { AuthProvider } from './AuthProvider';


const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<ProtectedRoute children={<Home />} />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
