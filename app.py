import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")