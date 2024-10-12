import axios from 'axios';

// Set up your base URL depending on where your Flask API is hosted
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5555';

export const getHeroes = async () => {
    const response = await axios.get(`${API_URL}/heroes`);
    return response.data;
};

export const getPowers = async () => {
    const response = await axios.get(`${API_URL}/powers`);
    return response.data;
};

export const getHeroPowers = async () => {
    const response = await axios.get(`${API_URL}/hero_powers`);
    return response.data;
};
