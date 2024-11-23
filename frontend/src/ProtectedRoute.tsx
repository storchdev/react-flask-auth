import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from './UseAuth';

const ProtectedComponent: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return <>{children}</>;
};

export default ProtectedComponent;
