def calculate_severity(risk, fidelity):
    final_score = (0.6 * risk) + (0.4 * fidelity)

    if final_score >= 75:
        level = "CRITICAL"
    elif final_score >= 50:
        level = "HIGH"
    elif final_score >= 25:
        level = "MEDIUM"
    else:
        level = "LOW"

    print("Final Severity:", level)
    return level
