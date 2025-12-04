from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("iris_model.joblib")

app = FastAPI()

# Define Input Schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define Output Schema (optional but good practice)
class PredictionOutput(BaseModel):
    species: str
    probability: float

@app.post("/predict", response_model=PredictionOutput)
def predict_species(iris: IrisInput):
    # 1. Create DataFrame from input
    df = pd.DataFrame([iris.model_dump()])
    
    # 2. Feature Engineering (Must happen exactly like in training!)
    df['petal_area'] = df['petal_length'] * df['petal_width']
    
    # 3. Predict
    prediction = model.predict(df)[0]
    # get probability of the predicted class
    probs = model.predict_proba(df)
    max_prob = float(max(probs[0]))

    return {"species": prediction, "probability": max_prob}