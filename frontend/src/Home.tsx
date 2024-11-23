import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Home: React.FC = () => {
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchMessage = async () => {
      const response = await axios.get('/api/home');
      setMessage(response.data.message);
    };
    fetchMessage();
  }, [navigate]);

  return (
    <div>
      <h2>Home</h2>
      <p>{message}</p>
    </div>
  );
};

export default Home;
