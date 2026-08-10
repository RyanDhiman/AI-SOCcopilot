import pandas as pd
import joblib

# Create new security events for testing
test_events = pd.DataFrame([
    {
        "failed_login_count": 0,
        "source": 0,
        "privilege_activity": 0,
        "login_frequency": 1
    },
    {
        "failed_login_count": 5,
        "source": 0,
        "privilege_activity": 0,
        "login_frequency": 5
    },
    {
        "failed_login_count": 1,
        "source": 1,
        "privilege_activity": 1,
        "login_frequency": 2
    },
    {
        "failed_login_count": 4,
        "source": 1,
        "privilege_activity": 0,
        "login_frequency": 4
    }
])

print("\n========== NEW TEST SECURITY EVENTS ==========\n")
print(test_events)

# Load the trained Random Forest model
model_path = "models/random_forest.pkl"

model = joblib.load(model_path)

print("\n========== MODEL LOADED ==========\n")
print("Saved Random Forest model loaded successfully.")

# Make predictions on new test events
predictions = model.predict(test_events)

print("\n========== MODEL PREDICTIONS ==========\n")
print(predictions)

# Verify and display predictions
print("\n========== PREDICTION VERIFICATION ==========\n")

for index, prediction in enumerate(predictions):
    if prediction == 0:
        result = "Normal"
    else:
        result = "Suspicious"

    print(f"Event {index + 1} : {result}")