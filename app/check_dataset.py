import pandas as pd

# Load training dataset
data = pd.read_csv("data/ml/training_data.csv")

print("\n========== DATASET ==========\n")
print(data)

print("\n========== DATASET INFO ==========\n")

print("Total Rows       :", len(data))
print("Total Columns    :", len(data.columns))

print("\n========== LABEL COUNT ==========\n")

print("Normal (0)       :", len(data[data["label"] == 0]))
print("Suspicious (1)   :", len(data[data["label"] == 1]))

print("\n========== MISSING VALUES ==========\n")

print(data.isnull().sum())
print("\n========== FINAL DATASET CHECK ==========\n")

print("Duplicate Rows :", data.duplicated().sum())

print("Labels Present :", sorted(data["label"].unique()))

print("Minimum Failed Login Count :", data["failed_login_count"].min())
print("Maximum Failed Login Count :", data["failed_login_count"].max())

print("Minimum Login Frequency    :", data["login_frequency"].min())
print("Maximum Login Frequency    :", data["login_frequency"].max())