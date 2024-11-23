import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './UseAuth';


const Navbar: React.FC = () => {
  const { isAuthenticated } = useAuth();

  return (
    <nav>
      <ul>
        {isAuthenticated && (
          <>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/logout">Logout</Link>
            </li>
          </>
        )}
        {!isAuthenticated && (
          <>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/register">Register</Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
