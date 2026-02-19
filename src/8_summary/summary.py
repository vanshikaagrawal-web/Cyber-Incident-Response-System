def generate_summary(detected_events):
    summary = "Detected events: " + ", ".join(detected_events)
    print("\nSummary:")
    print(summary)
    return summary
