def response_decision_engine(detected_events):
    actions = []

    if "failed_login" in detected_events:
        actions.append("Enable account lockout policy")
    if "privilege_escalation" in detected_events:
        actions.append("Remove elevated privileges")
    if "lateral_movement_attempt" in detected_events:
        actions.append("Isolate affected systems")
    if "large_data_transfer" in detected_events:
        actions.append("Block outbound traffic temporarily")

    actions.append("Notify security team")
    actions.append("Start investigation process")

    print("\nResponse Actions:")
    for action in actions:
        print("-", action)

    return actions
