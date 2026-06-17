# CODTECH-END-TO-END-DATA-SCIENCE-PROJECT
# Predictive Maintenance Using Machine Learning

## Overview

This project predicts the Remaining Useful Life (RUL) of machines using sensor data and Machine Learning.

The objective is to predict how long a machine can operate before failure and help industries perform preventive maintenance.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Machine Learning
* FastAPI
* Uvicorn
* Joblib

## Project Workflow

1. Data collection and loading
2. Data preprocessing
3. Feature selection
4. Machine learning model training
5. Model evaluation
6. Saving trained model
7. Deploying model using FastAPI
8. Making predictions through API

## System Architecture

```
Sensor Data
     |
     ↓
ML Model
     |
     ↓
FastAPI Backend
     |
     ↓
RUL Prediction
```

## Features

* Predicts Remaining Useful Life of machines
* REST API deployment
* Real-time prediction support
* FastAPI Swagger documentation
* Machine learning model integration

## API Usage

Endpoint:

```
POST /predict
```

Input:

```json
{
 "values":[sensor_values]
}
```

Output:

```json
{
 "Remaining_Life":120.5
}
```

## Project Structure

```
Predictive-Maintenance-RUL-API

│
├── backend/
│   └── app.py
│
├── models/
│   └── rul_model.pkl
│
├── notebook.ipynb
├── requirements.txt
└── README.md
```

## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Start API:

```
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to test predictions.

## Results

The system successfully predicts the remaining useful life of equipment and provides an API interface for real-time usage.

## Author

Tangella Madhumitha
