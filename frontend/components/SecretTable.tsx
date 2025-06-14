import React from 'react';

const SecretTable = ({ secrets }) => {
    return (
        <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                    <tr>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Value</th>
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {secrets.map((secret) => (
                        <tr key={secret.id}>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{secret.name}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{secret.type}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{secret.value}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default SecretTable;