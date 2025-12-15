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

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully")
