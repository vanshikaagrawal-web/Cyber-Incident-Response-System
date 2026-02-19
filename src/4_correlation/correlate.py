def correlate_attack(logs):
    detected_events = set(log.get("event_type") for log in logs)

    print("Detected Event Types:", detected_events)

    if len(detected_events) > 1:
        print("Multi-stage activity detected")
        return detected_events

    print("No major attack chain detected")
    return None
