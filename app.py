import streamlit as st
import pandas as pd
import requests

# Title
st.title("💸 Adult Income Prediction")
st.write("Predict whether income is >50K or <=50K")

# =========================================================
# BACKEND API URL (Deploy hone ke baad apni backend URL yahan dalein)
# =========================================================
# Local testing ke liye: "http://127.0.0.1:8000/predict"
API_URL = "http://127.0.0.1:8000/predict" 

# =========================
# INPUTS
# =========================
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 90, 30)
    workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Local-gov', 'State-gov', 'Federal-gov'])
    fnlwgt = st.number_input("fnlwgt", value=100000)
    education = st.selectbox("Education", ['Bachelors', 'HS-grad', 'Masters', 'Some-college'])
    educational_num = st.slider("Educational Number", 1, 16, 10)
    marital_status = st.selectbox("Marital Status", ['Never-married', 'Married-civ-spouse', 'Divorced'])
    occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Sales', 'Exec-managerial'])

with col2:
    relationship = st.selectbox("Relationship", ['Not-in-family', 'Husband', 'Wife'])
    race = st.selectbox("Race", ['White', 'Black', 'Asian-Pac-Islander'])
    gender = st.selectbox("Gender", ['Male', 'Female'])
    capital_gain = st.number_input("Capital Gain", value=0)
    capital_loss = st.number_input("Capital Loss", value=0)
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)
    native_country = st.selectbox("Native Country", ['United-States', 'India', 'Pakistan'])

# =========================
# PREDICTION VIA API
# =========================
if st.button("Predict"):
    # JSON Payload taiyar karein jo FastAPI accept karega
    payload = {
        "age": int(age),
        "workclass": workclass,
        "fnlwgt": int(fnlwgt),
        "education": education,
        "educational_num": int(educational_num),  # Pydantic validation ke mutabiq
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": int(capital_gain),
        "capital_loss": int(capital_loss),
        "hours_per_week": int(hours_per_week),
        "native_country": native_country
    }

    try:
        # FastAPI backend ko request bhejein
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            
            if prediction == ">50K":
                st.success(f"Prediction: The estimated income is {prediction}")
            else:
                st.info(f"Prediction: The estimated income is {prediction}")
        else:
            st.error(f"Backend API Error! Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"Could not connect to FastAPI backend: {e}")