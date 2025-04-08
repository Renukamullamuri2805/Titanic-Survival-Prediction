# 🚢 Titanic Survival Prediction – ML + Streamlit App

A complete machine learning pipeline that predicts Titanic passenger survival using logistic regression. This project includes data analysis, model training, and an interactive Streamlit web application for real-time predictions.

---

##  Overview

This project focuses on predicting the survival of Titanic passengers based on selected features such as **Passenger Class**, **Age**, and **Gender**. The solution includes:

- 📊 **Exploratory Data Analysis (EDA)** using Jupyter Notebook
- 🧠 **Model training** using Logistic Regression
- 🌐 **Deployment** via a user-friendly Streamlit application

---

##  Core Features

-  Data preprocessing and visualization in `Titanic_project.ipynb`
-  Logistic Regression model saved as `titanic2.pkl`
-  Streamlit app `titanic.py` for real-time predictions
-  Minimal UI for inputting Pclass, Age, and Gender
-  Instant feedback: **Survived** or **Not Survived**

---
##  Technologies Used

- **Python**
- **Pandas**, **Seaborn**, **Matplotlib** – for data analysis and visualization
- **Scikit-learn** – for model building and evaluation
- **Pickle** – for model serialization
- **Streamlit** – for deploying the web interface
  
##  Demo (How It Works)

1. **User Input:**
   - Passenger Class (`1`, `2`, or `3`)
   - Age (`e.g., 25`)
   - Gender (`0` for Female, `1` for Male)

2. **Click "Predict"**

3. **Output:**
   -  *Survived*
   -  *Not Survived*

---

## 📁 Project Structure
  ├── Titanic_project.ipynb # Data analysis & model training 
  ├── titanic2.pkl # Serialized logistic regression model 
  ├── titanic.py # Streamlit frontend app 
  └── README.md # Project documentation
