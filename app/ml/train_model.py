import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)

# Load processed dataset
data = pd.read_csv("data/ml/processed_data.csv")

# Separate features and label
X = data.drop("label", axis=1)
y = data["label"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the Random Forest model
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n========== MODEL ACCURACY ==========\n")
print(f"Accuracy : {accuracy:.2f}")
print(f"Accuracy Percentage : {accuracy * 100:.2f}%")

# Calculate precision and recall
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print("\n========== PRECISION & RECALL ==========\n")
print(f"Precision : {precision:.2f}")
print(f"Precision Percentage : {precision * 100:.2f}%")
print(f"Recall    : {recall:.2f}")
print(f"Recall Percentage    : {recall * 100:.2f}%")

# Generate confusion matrix
cm = confusion_matrix(y_test, predictions)

print("\n========== CONFUSION MATRIX ==========\n")
print(cm)

# Generate classification report
report = classification_report(
    y_test,
    predictions,
    target_names=["Normal", "Suspicious"]
)

print("\n========== CLASSIFICATION REPORT ==========\n")
print(report)

# Display model information
print("\n========== RANDOM FOREST MODEL ==========\n")
print(model)

# Display dataset split
print("\n========== DATASET SPLIT ==========\n")
print("Total Examples    :", len(data))
print("Training Examples :", len(X_train))
print("Testing Examples  :", len(X_test))

# Display training data
print("\n========== TRAINING DATA ==========\n")
print(X_train)

# Display testing data
print("\n========== TESTING DATA ==========\n")
print(X_test)

# Display training labels
print("\n========== TRAINING LABELS ==========\n")
print(y_train)

# Display testing labels
print("\n========== TESTING LABELS ==========\n")
print(y_test)

# Confirm model training
print("\n========== MODEL TRAINING ==========\n")
print("Random Forest model trained successfully.")

# Display predictions
print("\n========== MODEL PREDICTIONS ==========\n")
print(predictions)

# Display actual labels
print("\n========== ACTUAL LABELS ==========\n")
print(y_test.values)
# Final evaluation summary

print("\n========== FINAL MODEL EVALUATION ==========\n")

print(f"Accuracy  : {accuracy * 100:.2f}%")
print(f"Precision : {precision * 100:.2f}%")
print(f"Recall    : {recall * 100:.2f}%")

print("\nModel evaluation completed successfully.")
# Save trained model

model_path = "models/random_forest.pkl"

joblib.dump(model, model_path)

print("\n========== MODEL SAVED ==========\n")
print(f"Model saved to: {model_path}")
# Load saved model
loaded_model = joblib.load(model_path)

# Make predictions using loaded model
loaded_predictions = loaded_model.predict(X_test)

print("\n========== LOADED MODEL VERIFICATION ==========\n")
print("Original Predictions :", predictions)
print("Loaded Model Predictions :", loaded_predictions)

if (predictions == loaded_predictions).all():
    print("Saved model verification successful.")
else:
    print("Saved model verification failed.")