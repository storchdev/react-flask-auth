import { createContext } from 'react';

// Define the shape of the context
export interface AuthContextType {
  isAuthenticated: boolean;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  checkAuth: () => Promise<void>;
}

// Create the context
export const AuthContext = createContext<AuthContextType | undefined>(undefined);
