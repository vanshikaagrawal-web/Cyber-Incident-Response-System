MITRE_MAP = {
    "failed_login": "Credential Access",
    "privilege_escalation": "Privilege Escalation",
    "lateral_movement_attempt": "Lateral Movement",
    "large_data_transfer": "Exfiltration"
}

def map_mitre(detected_events):
    stages = set()

    for event in detected_events:
        if event in MITRE_MAP:
            stages.add(MITRE_MAP[event])

    print("Mapped MITRE Stages:", stages)
    return stages
