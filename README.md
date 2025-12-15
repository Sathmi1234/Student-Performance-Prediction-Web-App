# Student Performance Prediction Web App

This is a simple machine learning–based web application developed as a leisure-time project to explore how data science and web interfaces can be combined to solve real-world problems.
The application predicts whether a student is likely to **pass or fail** based on academic and study-related factors.

---

## Project Overview

The project uses a supervised machine learning approach to analyze student performance data and classify outcomes as **Pass** or **Fail**.
A lightweight web interface is built using **Streamlit** to allow users to input student details and get instant predictions.

---

## Dataset

* **Name:** Student Performance Dataset (Portuguese)
* **File:** `student-por.csv`
* **Source:** UCI Machine Learning Repository
* **Target Variable:**

  * `G3` (Final Grade)
  * Pass → `G3 ≥ 10`
  * Fail → `G3 < 10`

---

## Features Used

* `studytime` – Weekly study time
* `failures` – Number of past class failures
* `absences` – Number of school absences
* `G1` – First period grade
* `G2` – Second period grade

---

## Technologies Used

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## Project Structure

```
student-performance-ml/
│
├── model.py          # Trains and saves the ML model
├── app.py            # Streamlit web application
├── student-por.csv   # Dataset
├── model.pkl         # Saved model (generated after training)
└── README.md
```

---

## How the Project Works

1. The dataset is loaded and preprocessed.
2. A new target column (`pass`) is created based on the final grade.
3. A **Logistic Regression** model is trained using selected features.
4. The trained model is saved using Joblib.
5. The Streamlit app loads the model and provides a user-friendly interface for predictions.

---

## How to Run the Project

### 1. Install dependencies

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

### 2. Train the model

```bash
python model.py
```

This will generate the `model.pkl` file.

### 3. Run the web application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Output

* **Pass**: Student is likely to pass the subject
* **Fail**: Student is likely to fail the subject

Predictions are based on the input values provided through the web interface.

---

## Purpose of the Project

This project was created during leisure time to practice:

* Machine learning fundamentals
* Data preprocessing and feature selection
* Model training and evaluation
* Building simple web interfaces for ML models

---

## Future Improvements

* Use additional features from the dataset
* Try different machine learning models
* Display model accuracy and performance metrics
* Deploy the application online

---

This project is for educational and personal learning purposes.
