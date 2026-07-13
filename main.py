from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Adult Income Prediction API")

# Load the pre-trained pipeline (includes preprocessor + classifier)
model = joblib.load("model.pkl")

# Define request body schema matching the adult dataset features
class IncomeFeatures(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    educational_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str

@app.get("/")
def home():
    return {"message": "Income Prediction API is running!"}

@app.post("/predict")
def predict(data: IncomeFeatures):
    # Convert incoming JSON data to DataFrame format expected by the pipeline
    input_data = pd.DataFrame([data.dict()])
    
    # Rename 'educational_num' if your CSV used 'educational-num'
    input_data = input_data.rename(columns={'educational_num': 'educational-num'})
    
    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] if hasattr(model, "predict_proba") else None
    
    result = ">50K" if prediction == 1 else "<=50K"
    
    return {
        "prediction": result,
        "income_code": int(prediction),
        "probability_greater_than_50k": float(probability) if probability is not None else "N/A"
    }