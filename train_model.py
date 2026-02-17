import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/diabetes.csv")

X = df[["Pregnancies", "Glucose", "BloodPressure", "Age"]]
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model/diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved")
