import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model and scaler
model = pickle.load(open("heart_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("💓 Heart Disease Prediction App")
st.markdown("Enter the details below to check heart disease risk:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250)
chol = st.number_input("Cholesterol", min_value=100, max_value=600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=250)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Prepare data for prediction
input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol,
                        fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

scaled_data = scaler.transform(input_data)

# Prediction
if st.button("Predict"):
    prediction = model.predict(scaled_data)
    result = "✅ No Heart Disease" if prediction[0] == 0 else "⚠️ Risk of Heart Disease"
    st.subheader(f"Result: {result}")
