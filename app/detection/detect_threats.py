import joblib
import pandas as pd


# =====================================================
# LOAD TRAINED MODEL
# =====================================================

MODEL_PATH = "models/random_forest.pkl"

model = joblib.load(MODEL_PATH)


def detect_threat(log, normalized_logs):

    # =====================================================
    # RULE-BASED DETECTION
    # =====================================================

    rule_detected = False

    if log["status"] == "Failed Login":
        rule_detected = True

    # =====================================================
    # GET USER ACTIVITY
    # =====================================================

    username = log["username"]

    user_logs = [
        item
        for item in normalized_logs
        if item["username"].lower() == username.lower()
    ]

    # =====================================================
    # CALCULATE ML FEATURES
    # =====================================================

    failed_login_count = sum(
        1
        for item in user_logs
        if item["status"] == "Failed Login"
    )

    if log["source"] == "Windows":
        source_value = 0
    else:
        source_value = 1

    privilege_activity = int(
        any(
            item["status"] == "Privilege Escalation"
            for item in user_logs
        )
    )

    login_frequency = sum(
        1
        for item in user_logs
        if item["status"] in ["Login Success", "Failed Login"]
    )

    # =====================================================
    # CREATE ML FEATURES
    # =====================================================

    features = pd.DataFrame([{
        "failed_login_count": failed_login_count,
        "source": source_value,
        "privilege_activity": privilege_activity,
        "login_frequency": login_frequency
    }])

    # =====================================================
    # MACHINE LEARNING DETECTION
    # =====================================================

    ml_prediction = model.predict(features)[0]

    ml_detected = bool(ml_prediction == 1)

    # =====================================================
    # FINAL THREAT LOGIC
    # =====================================================

    if rule_detected and ml_detected:

        severity = "Critical"
        detection_method = "Rule + Machine Learning"
        threat_detected = True

    elif rule_detected:

        severity = "Medium"
        detection_method = "Rule-Based"
        threat_detected = True

    elif ml_detected:

        severity = "High"
        detection_method = "Machine Learning"
        threat_detected = True

    else:

        severity = "Low"
        detection_method = "None"
        threat_detected = False

    # =====================================================
    # CREATE ALERT RESULT
    # =====================================================

    alert = {
        "username": username,
        "ip": log["ip"],
        "timestamp": log["timestamp"],
        "source": log["source"],
        "status": log["status"],
        "failed_login_count": failed_login_count,
        "privilege_activity": privilege_activity,
        "login_frequency": login_frequency,
        "rule_detected": rule_detected,
        "ml_detected": ml_detected,
        "threat_detected": threat_detected,
        "detection_method": detection_method,
        "severity": severity
    }

    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    print("\n========== THREAT DETECTION ENGINE ==========\n")

    print("User              :", username)
    print("Failed Logins     :", failed_login_count)
    print("Source            :", log["source"])
    print("Privilege Activity:", privilege_activity)
    print("Login Frequency   :", login_frequency)

    print(
        "Rule Detection    :",
        "Threat" if rule_detected else "Normal"
    )

    print(
        "ML Detection      :",
        "Suspicious" if ml_detected else "Normal"
    )

    print("\n========== FINAL THREAT DECISION ==========\n")

    print("Threat Detected   :", threat_detected)
    print("Detection Method  :", detection_method)
    print("Severity          :", severity)

    if threat_detected:
        print("\n🚨 SECURITY THREAT DETECTED")
    else:
        print("\n✅ NO THREAT DETECTED")

    print("=" * 45)

    # Return structured result
    return alert