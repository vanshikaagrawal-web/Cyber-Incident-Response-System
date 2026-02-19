def calculate_fidelity_score(detected_events):
    correlation_strength = len(detected_events) * 25
    fidelity_score = min(100, correlation_strength)
    print("Fidelity Score:", fidelity_score)
    return fidelity_score
