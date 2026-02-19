ASSET_REGISTRY = {
    "HR_Server": {"criticality": 90, "sensitivity": 85},
    "Finance_Server": {"criticality": 95, "sensitivity": 95},
    "User_Laptop": {"criticality": 40, "sensitivity": 30}
}

def calculate_risk_score(detected_events, affected_nodes):
    base_severity = len(detected_events) * 20
    blast_radius = len(affected_nodes) * 10

    asset_score = 0
    for node in affected_nodes:
        if node in ASSET_REGISTRY:
            asset_score += ASSET_REGISTRY[node]["criticality"] * 0.3

    risk_score = min(100, base_severity + blast_radius + asset_score)
    print("Risk Score:", risk_score)
    return risk_score
