import React from 'react';

const HomePage: React.FC = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 className="text-4xl font-bold mb-4">Welcome to SecranAI</h1>
            <p className="text-lg text-center mb-8">
                Your one-stop solution for cloud secret management and risk analysis.
            </p>
            <a href="/login" className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                Get Started
            </a>
        </div>
    );
};

export default HomePage;