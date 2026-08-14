import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import json
from normalize_logs import normalize_windows_log, normalize_linux_log
from detection.detect_threats import detect_threat


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


# =====================================================
# NORMALIZE LOGS
# =====================================================

normalized_logs = []


# Normalize Windows Logs
for index, row in windows_logs.iterrows():

    normalized_windows = normalize_windows_log(row)
    normalized_logs.append(normalized_windows)


# Normalize Linux Logs
for log in linux_logs:

    normalized_linux = normalize_linux_log(log)
    normalized_logs.append(normalized_linux)


print("\n========== NORMALIZED LOGS ==========\n")

for log in normalized_logs:
    print(log)


# =====================================================
# TEST RESULTS
# =====================================================

print("\n========== TEST RESULTS ==========\n")

print("Windows Logs Loaded   :", len(windows_logs))
print("Linux Logs Loaded     :", len(linux_logs))
print("Normalized Logs Total :", len(normalized_logs))


# =====================================================
# THREAT DETECTION ENGINE
# =====================================================

print("\n========== THREAT DETECTION ==========\n")

for log in normalized_logs:

    detect_threat(log, normalized_logs)