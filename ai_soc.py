import json
import hashlib
import networkx as nx
import matplotlib.pyplot as plt


# ==============================
# PROTOTYPE ASSET REGISTRY
# ==============================
ASSET_REGISTRY = {
    "HR_Server": {"criticality": 90, "sensitivity": 85},
    "Finance_Server": {"criticality": 95, "sensitivity": 95},
    "User_Laptop": {"criticality": 40, "sensitivity": 30}
}

PREVIOUS_HASH = "0" * 64


# ==============================
# STEP 1 — LOG INGESTION
# ==============================
def ingest_logs():
    try:
        with open("logs.json", "r") as f:
            logs = json.load(f)
        print("\nTotal Logs Ingested:", len(logs))
        return logs
    except Exception as e:
        print("Log ingestion failed:", e)
        return []


# ==============================
# VALIDATE CUSTOM LOG STRUCTURE
# ==============================
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


# ==============================
# STEP 2 — UEBA Detection
# ==============================
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


# ==============================
# STEP 3 — CORRELATION ENGINE
# ==============================
def correlate_attack(logs):
    detected_events = set(log.get("event_type") for log in logs)

    print("Detected Event Types:", detected_events)

    if len(detected_events) > 1:
        print("Multi-stage activity detected")
        return detected_events

    print("No major attack chain detected")
    return None


# ==============================
# MITRE STAGE MAPPING
# ==============================
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


# ==============================
# STEP 4 — RESPONSE DECISION ENGINE
# ==============================
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


# ==============================
# STEP 5 — THREAT GRAPH (Dynamic Node Selection)
# ==============================
def build_threat_graph(logs):
    G = nx.Graph()

    for log in logs:
        src = log.get("source_ip")
        dst = log.get("destination_ip")

        if src and dst:
            G.add_edge(src, dst)

    if len(G.nodes()) == 0:
        print("No graph data available.")
        return []

    # Dynamic compromised node selection
    compromised_node = max(G.degree, key=lambda x: x[1])[0]

    print("Compromised Node Selected:", compromised_node)

    blast = nx.single_source_shortest_path_length(G, compromised_node, cutoff=2)
    subgraph = G.subgraph(blast.keys())

    print("Affected Nodes:", list(blast.keys()))

    plt.figure(figsize=(6, 4))
    nx.draw(subgraph, with_labels=True)
    plt.title("Blast Radius")
    plt.show()

    return list(blast.keys())


# ==============================
# RISK SCORING ENGINE
# ==============================
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


# ==============================
# FIDELITY SCORING ENGINE
# ==============================
def calculate_fidelity_score(detected_events):
    correlation_strength = len(detected_events) * 25
    fidelity_score = min(100, correlation_strength)

    print("Fidelity Score:", fidelity_score)
    return fidelity_score


# ==============================
# SEVERITY CALCULATION
# ==============================
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


# ==============================
# STEP 6 — EXECUTIVE SUMMARY
# ==============================
def generate_summary(detected_events):
    summary = "Detected events: " + ", ".join(detected_events)
    print("\nSummary:")
    print(summary)
    return summary


# ==============================
# HASH CHAIN AUDIT
# ==============================
def generate_hash_chain(text):
    global PREVIOUS_HASH
    combined = text + PREVIOUS_HASH
    new_hash = hashlib.sha256(combined.encode()).hexdigest()
    PREVIOUS_HASH = new_hash

    print("\nChained SHA256 Hash:")
    print(new_hash)


# ==============================
# MAIN
# ==============================
def main():
    logs = ingest_logs()

    if not logs:
        return

    logs = validate_logs(logs)

    ueba_detection(logs)

    detected_events = correlate_attack(logs)

    if detected_events:
        map_mitre(detected_events)

        affected_nodes = build_threat_graph(logs)

        risk = calculate_risk_score(detected_events, affected_nodes)
        fidelity = calculate_fidelity_score(detected_events)

        calculate_severity(risk, fidelity)

        response_decision_engine(detected_events)

        summary = generate_summary(detected_events)
        generate_hash_chain(summary)

    else:
        print("System normal")


if __name__ == "__main__":
    main()
