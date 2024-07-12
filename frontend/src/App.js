import React from 'react';
import SimulationForm from './components/SimulationForm';
import SimulationResult from './components/SimulationResult';
import Graph from './components/Graph';
import './styles.css';

function App() {
    const [result, setResult] = React.useState(null);

    const handleResult = (data) => {
        setResult(data);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Enzyme Simulator</h1>
                <SimulationForm onResult={handleResult} />
                {result && <SimulationResult result={result} />}
                {result && <Graph data={result} />}
            </header>
        </div>
    );
}

export default App;
