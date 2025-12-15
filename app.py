import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("🎓 Student Performance Prediction")
st.write("Based on Portuguese student dataset")

# User inputs
studytime = st.slider("Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Class Failures", 0, 4, 0)
absences = st.number_input("Number of Absences", 0, 100, 5)
g1 = st.slider("First Period Grade (0–20)", 0, 20, 10)
g2 = st.slider("Second Period Grade (0–20)", 0, 20, 10)
