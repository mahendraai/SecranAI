import React, { useEffect, useState } from 'react';
import { SecretTable } from '../components/SecretTable';
import { fetchSecrets } from '../utils/api';

const Dashboard = () => {
    const [secrets, setSecrets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getSecrets = async () => {
            try {
                const data = await fetchSecrets();
                setSecrets(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        getSecrets();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Your Secrets</h1>
            <SecretTable secrets={secrets} />
        </div>
    );
};

export default Dashboard;