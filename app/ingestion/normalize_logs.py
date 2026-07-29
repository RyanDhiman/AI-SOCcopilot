def normalize_windows_log(row):
    return {
        "timestamp": row["Timestamp"],
        "username": row["Username"],
        "ip": row["SourceIP"],
        "status": row["Status"],
        "source": "Windows"
    }
def normalize_linux_log(log):
    return {
        "timestamp": log["timestamp"],
        "username": log["user"],
        "ip": log["ip"],
        "status": log["status"],
        "source": "Linux"
    }