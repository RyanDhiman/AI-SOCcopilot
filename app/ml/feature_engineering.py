import pandas as pd

# Load training dataset
data = pd.read_csv("data/ml/training_data.csv")

# Encode source
data["source"] = data["source"].map({
    "Windows": 0,
    "Linux": 1
})

print("\n========== ENCODED DATA ==========\n")
print(data)

# Separate features and label
X = data.drop("label", axis=1)
y = data["label"]

print("\n========== FEATURES (X) ==========\n")
print(X)

print("\n========== LABEL (y) ==========\n")
print(y)
print("\n========== PROCESSED DATA CHECK ==========\n")

print("X Rows       :", X.shape[0])
print("X Columns    :", X.shape[1])
print("y Values     :", len(y))

print("\nSource Values:")
print(sorted(X["source"].unique()))

print("\nMissing Values in X:")
print(X.isnull().sum())

print("\nMissing Values in y:")
print(y.isnull().sum())

# Save processed dataset
processed_data = X.copy()
processed_data["label"] = y

processed_data.to_csv("data/ml/processed_data.csv", index=False)

print("\n========== PROCESSED DATA SAVED ==========\n")
print("Saved to: data/ml/processed_data.csv")