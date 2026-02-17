import streamlit as st
import pickle
import pandas as pd
import requests

# ==============================

API_KEY= "YOUR_GOOGLE_API_KEY"

# ==============================

# LOAD TRAINED ML MODEL
# ==============================

with open("model/diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature names must match training data exactly
FEATURE_NAMES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "Age"
]

# ==============================
# PREDICTION FUNCTION
# ==============================

def predict_diabetes(user_input):
    input_df = pd.DataFrame([user_input], columns=FEATURE_NAMES)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability

# ==============================
# AI EXPLANATION FUNCTION
# ==============================

def explain_result(user_input, probability):
    prompt = f"""
    Patient Data:
    Pregnancies: {user_input[0]}
    Glucose: {user_input[1]}
    Blood Pressure: {user_input[2]}
    Age: {user_input[3]}

    Risk probability: {probability:.2f}

    Explain in simple language and give short lifestyle advice.
    """

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"



    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"API Error: {result}"

    except Exception as e:
        return f"AI explanation failed: {e}"


# ==============================
# STREAMLIT UI
# ==============================

st.title("🩺 DiabetesPulse AI Agent")

preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
age = st.number_input("Age", min_value=0)

if st.button("Analyze"):

    inputs = [preg, glucose, bp, age]

    pred, prob = predict_diabetes(inputs)

    st.subheader("Result")
    st.write("Prediction:", "Diabetic" if pred else "Not Diabetic")
    st.metric("Risk Probability", f"{prob*100:.1f}%")

    with st.spinner("Generating AI explanation..."):
        explanation = explain_result(inputs, prob)

    st.markdown("### 🧠 AI Explanation")
    st.write(explanation)

st.caption(
    "⚠️ This tool is for educational purposes only and does not replace professional medical advice."
)
