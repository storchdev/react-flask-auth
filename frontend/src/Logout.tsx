import React, { useEffect } from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from './UseAuth';

const Logout: React.FC = () => {
  const { logout } = useAuth(); // Use the logout function from AuthContext

  useEffect(() => {
    const performLogout = async () => {
      await logout(); // Call logout to update context state
    };

    performLogout();
  }, [logout]);

  return <Navigate to="/login" replace />;
};

export default Logout;
