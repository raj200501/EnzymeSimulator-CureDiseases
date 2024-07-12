import React, { useState } from 'react';

function SimulationForm({ onResult }) {
    const [enzyme, setEnzyme] = useState('');
    const [dnaSequence, setDnaSequence] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('/api/simulate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ enzyme, dna_sequence: dnaSequence })
        });
        const data = await response.json();
        onResult(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Enzyme"
                value={enzyme}
                onChange={e => setEnzyme(e.target.value)}
                required
            />
            <input
                type="text"
                placeholder="DNA Sequence"
                value={dnaSequence}
                onChange={e => setDnaSequence(e.target.value)}
                required
            />
            <button type="submit">Simulate</button>
        </form>
    );
}

export default SimulationForm;
