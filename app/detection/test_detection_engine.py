from app.detection.detect_threats import detect_threat


# =====================================================
# TEST 1 - NORMAL ACTIVITY
# Expected: Low
# Rule = Normal
# ML   = Normal
# =====================================================

normal_logs = [
    {
        "timestamp": "2026-08-14 10:00:00",
        "username": "normal_user",
        "ip": "192.168.1.10",
        "status": "Login Success",
        "source": "Windows"
    }
]


# =====================================================
# TEST 2 - RULE-ONLY THREAT
# Expected: Medium
# Rule = Threat
# ML   = Normal
# =====================================================

rule_only_logs = [
    {
        "timestamp": "2026-08-14 10:05:00",
        "username": "admin",
        "ip": "192.168.1.20",
        "status": "Failed Login",
        "source": "Windows"
    }
]


# =====================================================
# TEST 3 - ML-ONLY THREAT
# Expected: High
# Rule = Normal
# ML   = Suspicious
# =====================================================

ml_only_logs = [
    {
        "timestamp": "2026-08-14 10:10:00",
        "username": "attacker",
        "ip": "192.168.1.30",
        "status": "Failed Login",
        "source": "Linux"
    },
    {
        "timestamp": "2026-08-14 10:11:00",
        "username": "attacker",
        "ip": "192.168.1.30",
        "status": "Failed Login",
        "source": "Linux"
    },
    {
        "timestamp": "2026-08-14 10:12:00",
        "username": "attacker",
        "ip": "192.168.1.30",
        "status": "Failed Login",
        "source": "Linux"
    },
    {
        "timestamp": "2026-08-14 10:13:00",
        "username": "attacker",
        "ip": "192.168.1.30",
        "status": "Logoff",
        "source": "Linux"
    }
]


# =====================================================
# TEST 4 - RULE + ML THREAT
# Expected: Critical
# Rule = Threat
# ML   = Suspicious
# =====================================================

combined_logs = [
    {
        "timestamp": "2026-08-14 10:20:00",
        "username": "guest",
        "ip": "192.168.1.40",
        "status": "Failed Login",
        "source": "Linux"
    },
    {
        "timestamp": "2026-08-14 10:21:00",
        "username": "guest",
        "ip": "192.168.1.40",
        "status": "Failed Login",
        "source": "Linux"
    },
    {
        "timestamp": "2026-08-14 10:22:00",
        "username": "guest",
        "ip": "192.168.1.40",
        "status": "Failed Login",
        "source": "Linux"
    }
]


# =====================================================
# RUN TESTS
# =====================================================

print("\n" + "=" * 55)
print("        THREAT DETECTION ENGINE TESTS")
print("=" * 55)


# -----------------------------------------------------
# Test 1
# -----------------------------------------------------

print("\n\n========== TEST 1: NORMAL ACTIVITY ==========\n")

detect_threat(
    normal_logs[0],
    normal_logs
)


# -----------------------------------------------------
# Test 2
# -----------------------------------------------------

print("\n\n========== TEST 2: RULE-ONLY THREAT ==========\n")

detect_threat(
    rule_only_logs[0],
    rule_only_logs
)


# -----------------------------------------------------
# Test 3
# -----------------------------------------------------

print("\n\n========== TEST 3: ML-ONLY THREAT ==========\n")

# Use the Logoff event as the current event.
# Therefore the rule does not detect a Failed Login,
# but the user's previous activity creates
# suspicious ML features.

detect_threat(
    ml_only_logs[3],
    ml_only_logs
)


# -----------------------------------------------------
# Test 4
# -----------------------------------------------------

print("\n\n========== TEST 4: RULE + ML THREAT ==========\n")

result = detect_threat(
    combined_logs[2],
    combined_logs
)

print("\n========== RETURNED ALERT ==========\n")
print(result)

print("\n" + "=" * 55)
print("        ALL THREAT DETECTION TESTS COMPLETED")
print("=" * 55)