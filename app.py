import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Title
st.title("Adult Income Prediction")

st.write("Predict whether income is >50K or <=50K")

# =========================
# INPUTS
# =========================

age = st.slider("Age", 18, 90, 30)

workclass = st.selectbox(
    "Workclass",
    [
        'Private',
        'Self-emp-not-inc',
        'Local-gov',
        'State-gov',
        'Federal-gov'
    ]
)

fnlwgt = st.number_input("fnlwgt", value=100000)

education = st.selectbox(
    "Education",
    [
        'Bachelors',
        'HS-grad',
        'Masters',
        'Some-college'
    ]
)

educational_num = st.slider(
    "Educational Number",
    1,
    16,
    10
)

marital_status = st.selectbox(
    "Marital Status",
    [
        'Never-married',
        'Married-civ-spouse',
        'Divorced'
    ]
)

occupation = st.selectbox(
    "Occupation",
    [
        'Tech-support',
        'Craft-repair',
        'Sales',
        'Exec-managerial'
    ]
)

relationship = st.selectbox(
    "Relationship",
    [
        'Not-in-family',
        'Husband',
        'Wife'
    ]
)

race = st.selectbox(
    "Race",
    [
        'White',
        'Black',
        'Asian-Pac-Islander'
    ]
)

gender = st.selectbox(
    "Gender",
    [
        'Male',
        'Female'
    ]
)

capital_gain = st.number_input(
    "Capital Gain",
    value=0
)

capital_loss = st.number_input(
    "Capital Loss",
    value=0
)

hours_per_week = st.slider(
    "Hours per Week",
    1,
    100,
    40
)

native_country = st.selectbox(
    "Native Country",
    [
        'United-States',
        'India',
        'Pakistan'
    ]
)

# =========================
# PREDICTION
# =========================

if st.button("Predict"):

    input_data = pd.DataFrame({

        'age': [age],
        'workclass': [workclass],
        'fnlwgt': [fnlwgt],
        'education': [education],
        'educational-num': [educational_num],
        'marital-status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'gender': [gender],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'hours-per-week': [hours_per_week],
        'native-country': [native_country]

    })

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")