import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const getSecrets = async () => {
    const response = await apiClient.get('/secrets');
    return response.data;
};

export const login = async (credentials) => {
    const response = await apiClient.post('/login', credentials);
    return response.data;
};

export const connectCloud = async (provider, token) => {
    const response = await apiClient.post(`/connect/${provider}`, { token });
    return response.data;
};