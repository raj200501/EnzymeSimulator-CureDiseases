# EnzymeSimulator

**EnzymeSimulator** is an innovative platform designed to run simulations of enzyme-DNA interactions to discover potential treatments for various diseases. It integrates existing genomic databases, data science, and machine learning to identify promising enzyme-DNA interactions that could lead to new treatments.

## Features

- Integrates existing genomic databases for comprehensive analysis
- Simulates enzyme-DNA interactions to identify potential treatments
- Advanced analytics and machine learning models
- Interactive and responsive web interface with data visualization
- Scalable and modular architecture

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/EnzymeSimulator.git
    cd EnzymeSimulator
    ```

2. Set up the backend:
    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py
    ```

3. Initialize the database:
    ```bash
    cd backend/database
    python init_db.py
    ```

4. Set up the frontend:
    ```bash
    cd frontend
    npm install
    npm start
    ```

5. Set up the data processing environment:
    ```bash
    cd data_processing
    pip install -r requirements.txt
    python process_data.py
    ```

6. Set up the machine learning environment:
    ```bash
    cd machine_learning
    pip install -r requirements.txt
    python model_training.py
    ```

7. Use Docker for easier setup (optional):
    ```bash
    cd infrastructure
    docker-compose up
    ```

## Usage

- Access the web interface at `http://localhost:3000`
- Backend API available at `http://localhost:5000/api`
- Machine learning models are trained and evaluated via the scripts in `machine_learning`
- Data processing is handled via Python scripts in `data_processing`

## Contributing

We welcome contributions from everyone. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
