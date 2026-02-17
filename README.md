# 🩺 DiabetesPulse-AI-Agent

## Project Overview
An **AI agent–based healthcare application** that collects basic health inputs from users, predicts diabetes risk using a trained machine learning model, and explains the result in simple language using generative AI.

## Features
- Predicts diabetes risk probability using **Random Forest**
- Classifies risk (Low / Moderate / High)
- Generates AI-based explanation in simple language
- Provides lifestyle recommendations
- Interactive web interface using **Streamlit**

##  Architecture
This system uses a **two-agent design**:

1. **Prediction Agent**
   - Random Forest Classifier
   - Outputs diabetes classification and probability

2. **Explanation Agent**
   - Gemini 2.5 Flash API
   - Converts numeric output into human-readable explanation

**Workflow:**

- ├──User Input (Age, Glucose, BP, Pregnancies) 
- ├── Prediction Agent (ML Model)
- ├── Explanation Agent (Gemini API)
- ├──Streamlit UI Display

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit (Interactive UI)  
- Google Gemini 2.5 Flash (REST API)
- Requests (API calls)

## Project Structure
- DiabetesPulse/
- ├── data/ # Training dataset (CSV)
- ├── model/ # Trained ML model (diabetes_model.pkl)
- ├── screenshots/ # Optional: App screenshots
- ├── app.py # Streamlit app
- ├── train_model.py # Script to train model
- ├── requirements.txt # All project dependencies
- ├── README.md # This file
- └── .gitignore # Ignore API keys, pycache, env

## Installation
- Install dependencies: pip install -r requirements.txt

- Set API key: export GEMINI_API_KEY="your_api_key"

- Run: streamlit run app.py

## Dataset Source:
- Pima Indians Diabetes Dataset from Kaggle
- Used only for training the prediction model
[Dataset Link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Used only the following columns for learning purposes: **Pregnancies**, **Glucose**, **BloodPressure**, **Age**,**Outcome**

## Example Usage
### High Risk Example
- Glucose: 180
- Age: 50
- Blood Pressure: 160

**Output**:
- Prediction: Diabetic
- Risk Probability: 85%
- AI Explanation: “Your glucose and blood pressure are high. Regular exercise and healthy eating are recommended.”

### Low Risk Example
- Glucose: 90
- Age: 25
- Blood Pressure: 120

**Output**:
- Prediction: Not Diabetic
- Risk Probability: 10%
- AI Explanation: “Your health indicators are within normal range. Maintain healthy lifestyle.”

## Screenshots/ Preview 
<img width="581" height="455" alt="Screenshot 1" src="https://github.com/user-attachments/assets/63bcda84-2e9f-4c6f-830d-41844c7185e2" />

<img width="578" height="369" alt="Screenshot 2" src="https://github.com/user-attachments/assets/7e48c840-0938-400e-99d2-a4ca91fe6d52" />

<img width="646" height="283" alt="Screenshot 3" src="https://github.com/user-attachments/assets/1f96a728-5741-4495-a778-bb083a7638de" />



**⚠️ Disclaimer**
This application is for educational purposes only and does not replace professional medical advice.

## Author
Rohini R
