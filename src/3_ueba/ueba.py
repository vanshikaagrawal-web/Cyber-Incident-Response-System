def ueba_detection(logs):
    anomalies = []

    for log in logs:
        if log.get("geo_location") == "Russia":
            anomalies.append(log)

        timestamp = log.get("timestamp", "")
        if "T" in timestamp:
            try:
                hour = int(timestamp.split("T")[1][:2])
                if hour >= 23 or hour <= 5:
                    anomalies.append(log)
            except:
                pass

    print("UEBA Anomalies Detected:", len(anomalies))
    return anomalies
