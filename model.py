import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv("student-por.csv")

# Create target column
data['pass'] = np.where(data['G3'] >= 10, 1, 0)

# Select important features
X = data[['studytime', 'failures', 'absences', 'G1', 'G2']]
y = data['pass']

