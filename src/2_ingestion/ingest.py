import json

def ingest_logs():
    try:
        with open("data/logs.json", "r") as f:
            logs = json.load(f)
        print("\nTotal Logs Ingested:", len(logs))
        return logs
    except Exception as e:
        print("Log ingestion failed:", e)
        return []

def validate_logs(logs):
    required_fields = [
        "source_ip",
        "destination_ip",
        "event_type",
        "timestamp"
    ]

    valid_logs = []

    for log in logs:
        if all(field in log for field in required_fields):
            valid_logs.append(log)

    print("Valid Logs:", len(valid_logs))
    return valid_logs
