def detect_threat(log):

    if log["status"] == "Failed Login":
        print("\n" + "=" * 45)
        print("🚨 SECURITY ALERT")
        print("=" * 45)
        print("Alert Type : Failed Login")
        print(f"Timestamp  : {log['timestamp']}")
        print(f"User       : {log['username']}")
        print(f"IP         : {log['ip']}")
        print(f"Status     : {log['status']}")
        print(f"Source     : {log['source']}")
        print("Severity   : Medium")
        print("Description: Authentication failure detected.")

        print("=" * 45)