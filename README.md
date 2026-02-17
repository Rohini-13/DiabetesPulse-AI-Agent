# DiabetesPulse-AI-Agent

An **AI agent–based healthcare application** that collects basic health inputs from users, predicts diabetes risk using a trained machine learning model, and explains the result in simple language using generative AI.

## Features
- Predicts diabetes risk probability using Random Forest
- Classifies risk (Low / Moderate / High)
- Generates AI-based explanation in simple language
- Provides lifestyle recommendations
- Interactive web interface using Streamlit

##  Architecture

This system uses a two-agent design:

1. **Prediction Agent**
   - Random Forest Classifier
   - Outputs diabetes classification and probability

2. **Explanation Agent**
   - Gemini 2.5 Flash API
   - Converts numeric output into human-readable explanation

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Google Gemini 2.5 Flash (REST API)
- Requests

## Project Structure

DiabetesPulse/
├── data/
├── model/
├── app.py
├── train_model.py
├── requirements.txt

-----
## Installation
- pip install -r requirements.txt

- Set API key:
export GEMINI_API_KEY="your_api_key"

- Run:
streamlit run app.py

**⚠️ Disclaimer**

This application is for educational purposes only and does not replace professional medical advice.
