from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI()


model = joblib.load(
r"C:\Users\tange\Downloads\CODTECH\.ipynb_checkpoints\TASK3-END-TO-END DATA SCIENCE PROJECT\models\rul_model.pkl"
)


class EngineData(BaseModel):
    values: list


@app.get("/")
def home():
    return {
        "message":"Predictive Maintenance API"
    }


@app.post("/predict")
def predict(data: EngineData):

    prediction = model.predict(
        [data.values]
    )

    return {
        "Remaining_Life": float(prediction[0])
    }