from ingestion.ingest import ingest_logs, validate_logs
from ueba.ueba import ueba_detection
from correlation.correlate import correlate_attack
from correlation.mitre_mapping import map_mitre
from threat_graph.graph import build_threat_graph
from scoring.risk import calculate_risk_score
from scoring.fidelity import calculate_fidelity_score
from scoring.severity import calculate_severity
from response.decision import response_decision_engine
from summary.summary import generate_summary
from audit.hash_chain import generate_hash_chain

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
