# Barclays Hack-O-Hire Project

## Cyber incident response system
## 🎨 Table of Contents

- [Cyber incident response system](#cyber-incident-response-system)
- [Contributors](#contributors)
- [Company Logo](#company-logo)
- [Description](#description)
- [Technology Stack](#technology-stack)
- [Idea](#idea)
- [PPT](#ppt)

## Cyber incident response system
## Contributors
- Shalaka Parhad
- Vanshika Agrawal
- Mansi Sawarkar
- Akshita Paliwal
- Nidhi Patil


## Company Logo

<p align="center">
  <img src="Barclays-Logo.svg" width="300">
</p>


## Description

This project was developed for the Barclays Hack-O-Hire Hackathon to build an intelligent Cyber Incident Response System that detects and correlates security anomalies across logs and alerts. The system identifies irregular patterns, reduces false positives, and enables faster, automated responses to potential cyber threats in banking environments.

## Technology Stack

- **Frontend:** React.js, Tailwind CSS, Chart.js, D3.js  
- **Backend:** Python, FastAPI (REST APIs), Elasticsearch  
- **AI & ML:** PyOD, tsfresh, NetworkX, custom ML models  
- **AI Reasoning & LLMs:** LangChain, Hugging Face Transformers, Ollama  
- **Security & Audit:** Hyperledger Fabric, SHA-256 hashing  
- **Visualization:** Matplotlib, Plotly

## Idea

**Abstract:**

Modern security teams are overwhelmed by high volumes of alerts that lack context and require significant manual effort to investigate. Our project presents an AI-powered Autonomous Incident Response System that not only detects threats but understands and responds to them intelligently.
The system ingests security telemetry from sources such as SIEM, EDR, firewalls, and authentication systems, reduces alert noise, and correlates events to build a complete incident view. It applies behavioral analytics and contextual threat modeling to evaluate each incident based on confidence (fidelity) and business impact (risk), ensuring accurate prioritization.
After reconstructing the full attack story, the system generates a tailored response playbook and executes actions based on severity: fully autonomous for low-severity incidents, approval-based for medium-severity cases, and manual escalation for high and critical threats. A tamper-proof audit layer ensures forensic integrity, while SOC and executive dashboards provide operational and strategic visibility.


**Aim:**

The aim of this project is to build an intelligent incident response platform that reduces alert noise, improves threat understanding, and enables risk-aware responses through a combination of automation and human oversight.

**Our Solution:**

The system follows a modular, layered architecture that normalizes incoming security data and applies anomaly detection and correlation to identify meaningful incidents. A reasoning layer evaluates severity using confidence and risk metrics, triggering policy-driven response workflows. Depending on severity, incidents are handled autonomously, routed for approval, or escalated to analysts, with all actions securely logged in a tamper-resistant audit layer.

**Conclusion:**

By transitioning from alert-centric analysis to incident-centric intelligence, the proposed system enhances response speed, accuracy, and consistency. The solution reduces operational burden on security teams while providing strong auditability and scalability for modern banking and enterprise SOC environments.

## PPT

The presentation for Round 1 of the Hack-O-Hire Hackathon is available below:

- 👉 [View Round 1 PPT](TechByte_CCOEW_190226.pptx)



