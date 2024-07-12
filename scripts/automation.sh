#!/bin/bash

# Run data processing script
cd ../data_processing
python process_data.py

# Train machine learning model
cd ../machine_learning
python model_training.py

# Start backend server
cd ../backend
source venv/bin/activate
python app.py &
