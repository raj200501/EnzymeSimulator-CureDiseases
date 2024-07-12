from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from handlers.simulation_handler import run_simulation
from handlers.data_handler import get_genomic_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/enzyme_simulator.db'
db = SQLAlchemy(app)

@app.route('/api/simulate', methods=['POST'])
def simulate():
    enzyme = request.json.get('enzyme')
    dna_sequence = request.json.get('dna_sequence')
    result = run_simulation(enzyme, dna_sequence)
    return jsonify(result)

@app.route('/api/genomic-data', methods=['GET'])
def genomic_data():
    data = get_genomic_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
