from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Wine Quality Prediction API", version="1.0")

# Load model artifact
model = joblib.load("wine_model.pkl")

class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.post("/predict")
def predict_quality(features: WineFeatures):
    data = np.array([[v for v in features.model_dump().values()]])
    prediction = model.predict(data)
    return {"predicted_quality": float(prediction[0])}
