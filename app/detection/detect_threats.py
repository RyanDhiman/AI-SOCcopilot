def detect_threat(log):

    if log["status"] == "Failed Login":

        print("\n🚨 SECURITY ALERT")
        print("-" * 30)
        print(f"User     : {log['username']}")
        print(f"IP       : {log['ip']}")
        print(f"Status   : {log['status']}")
        print(f"Source   : {log['source']}")
        print("Severity : Medium")