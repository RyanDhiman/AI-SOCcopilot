import pandas as pd
import json
from normalize_logs import normalize_windows_log, normalize_linux_log

# Read Windows CSV Logs
windows_logs = pd.read_csv("data/windows/windows_logs.csv")

print("========== WINDOWS LOGS ==========\n")

for index, row in windows_logs.iterrows():
    print(f"Timestamp : {row['Timestamp']}")
    print(f"Event ID  : {row['EventID']}")
    print(f"Username  : {row['Username']}")
    print(f"Source IP : {row['SourceIP']}")
    print(f"Status    : {row['Status']}")
    print("-" * 40)

# Read Linux JSON Logs
with open("data/linux/linux_logs.json", "r") as file:
    linux_logs = json.load(file)

print("\n========== LINUX LOGS ==========\n")

for log in linux_logs:
    print(f"Timestamp : {log['timestamp']}")
    print(f"Service   : {log['service']}")
    print(f"User      : {log['user']}")
    print(f"IP        : {log['ip']}")
    print(f"Status    : {log['status']}")
    print("-" * 40)

normalized_logs = []

# Normalize Windows Logs
for index, row in windows_logs.iterrows():
    normalized_windows = normalize_windows_log(row)#calls function
    normalized_logs.append(normalized_windows)

# Normalize Linux Logs
for log in linux_logs:
    normalized_linux = normalize_linux_log(log)
    normalized_logs.append(normalized_linux)

print("\n========== NORMALIZED LOGS ==========\n")

for log in normalized_logs:
    print(log)

    print("\n========== TEST RESULTS ==========\n")

print(f"Windows Logs Loaded   : {len(windows_logs)}")
print(f"Linux Logs Loaded     : {len(linux_logs)}")
print(f"Normalized Logs Total : {len(normalized_logs)}")