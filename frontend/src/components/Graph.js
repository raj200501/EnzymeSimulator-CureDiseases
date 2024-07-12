import React from 'react';
import { Line } from 'react-chartjs-2';

function Graph({ data }) {
    const chartData = {
        labels: ['Start', 'Interaction'],
        datasets: [
            {
                label: 'Interaction Strength',
                data: [0, data.interaction_result === 'Positive' ? 100 : 0],
                fill: false,
                backgroundColor: 'rgb(75, 192, 192)',
                borderColor: 'rgba(75, 192, 192, 0.2)',
            },
        ],
    };

    return (
        <div>
            <h2>Interaction Graph</h2>
            <Line data={chartData} />
        </div>
    );
}

export default Graph;
