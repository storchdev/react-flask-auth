import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { AuthContext, AuthContextType } from './AuthContext';

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initializeAuth = async () => {
      await checkAuth();
      setLoading(false);
    };

    initializeAuth();
  }, []);

  const checkAuth = async () => {
    try {
      await axios.get('/api/auth-check');
      setIsAuthenticated(true);
    } catch {
      setIsAuthenticated(false);
    }
  };

  const login = async (username: string, password: string) => {
    try {
      await axios.post('/api/login', { username, password });
      await checkAuth();
    } catch {
      throw new Error('Login failed');
    }
  };

  const logout = async () => {
    await axios.post('/api/logout');
    setIsAuthenticated(false);
  };

  const contextValue: AuthContextType = {
    isAuthenticated,
    loading,
    login,
    logout,
    checkAuth,
  };

  return <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>;
};
