# StreamPulse AI ⚡
### Enterprise Industrial IoT Telemetry, Physics-Informed Anomaly Engine & Autonomous Agent Diagnostics

[![CI/CD Specification Validation](https://github.com/Sumesh-Chakkaravarthi/StreamPulse-AI/actions/workflows/verify-spec.yml/badge.svg)](https://github.com/Sumesh-Chakkaravarthi/StreamPulse-AI/actions)
![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Isolation%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![Explainability](https://img.shields.io/badge/Explainability-TreeSHAP-red)
![Physics-Informed](https://img.shields.io/badge/Guardrails-PINN%20Thermodynamics-purple)
![Autonomous AI Agent](https://img.shields.io/badge/AI%20Agent-Chain--of--Thought%20SOPs-A855F7)
![Prometheus](https://img.shields.io/badge/Observability-Prometheus%20%26%20OTel-E6522C?logo=prometheus&logoColor=white)
![Redpanda](https://img.shields.io/badge/Streaming-Redpanda%20Kafka-orange)
![ISO Compliance](https://img.shields.io/badge/Metrology-ISO%2017025%20%2F%209001-green)

---

## 🌊 Executive Overview

**StreamPulse AI** is an enterprise-grade, distributed industrial IoT telemetry, physics-informed anomaly detection, and autonomous diagnostic platform engineered for continuous **water quality instrumentation, electrochemical sensor arrays, and industrial fluidic skids**.

Analytical sensors deployed in municipal, industrial, and semiconductor water treatment facilities—such as glass pH electrodes, dual-platinum amperometric potentiostats, optical turbidity meters, and inductive toroidal conductivity probes—suffer from slow, silent, multi-hour degradation:
* **Organic Biofouling & Protein Adsorption:** Dielectric passivation of working electrodes.
* **Porous Ceramic Reference Junction Poisoning:** Silver sulfide ($\text{Ag}_2\text{S}$) precipitate precipitation distorting liquid junction potential.
* **Slow Monotonic Voltage Drift:** Reference electrolyte dilution causing insidious measurement skew.
* **Sudden Transducer Fractures & Cavitation:** Hydrodynamic water hammer shocks and microbubble optical interference.

Traditional industrial monitoring relies on static, hard-coded thresholds that sound alarms only after catastrophic process failure or regulatory EPA violations occur. **StreamPulse AI** delivers an end-to-end, mission-critical infrastructure combining **Physics-Informed Neural Networks (PINN)**, **Explainable AI (TreeSHAP)**, **Store-and-Forward Edge Buffering**, and an **Autonomous Chain-of-Thought (CoT) Diagnostic Agent**.

---

## 🏗️ End-to-End System Architecture

```mermaid
flowchart TD
    subgraph FIELD ["1. Industrial Field Sensor Stations"]
        N1["NODE-WA-01: Intake (Glass pH & RTD Temp)"]
        N2["NODE-WA-02: Electrochemical Potentiostat Cell"]
        N3["NODE-WA-03: Filtration Turbidity Skid"]
        N4["NODE-WA-04: Effluent Discharge Line"]
    end

    subgraph EDGE ["2. Edge Computing & Store-and-Forward Layer"]
        EDGE_AGENTS["Edge Gateway Agents (1s Rolling Window Aggregation)"]
        SQLITE_BUF[("Local SQLite Persistent Queue (Zero Data Loss)")]
        BACKOFF["Tenacity Exponential Backoff Retries"]
        EDGE_AGENTS -->|Network Partition Drop| SQLITE_BUF --> BACKOFF
    end

    subgraph INGESTION ["3. Event Streaming & High-Throughput Core"]
        BROKER["Redpanda Kafka / Redis Event Stream"]
        API["FastAPI Ingestion Gateway (18 REST Endpoints)"]
        VAL["Pydantic v2 Schema Validator & Metrology Check"]
        WS["Full-Duplex Telemetry WebSocket (/ws/telemetry)"]
        OTEL["Prometheus Telemetry Scraper (/metrics)"]
    end

    subgraph INTELLIGENCE ["4. Hybrid AI & Autonomous Diagnostics"]
        PINN["Physics Guardrail (Nernstian Slope & Cottrell Kinetics)"]
        ISO_FOREST["Multivariate Isolation Forest (Sub-second Outliers)"]
        SEQ_AUTO["Sequential Drift Autoencoder (Multi-Hour Trajectories)"]
        SHAP["TreeSHAP Exact Feature Attribution Engine"]
        AGENT["🧠 Autonomous AI Diagnostic Agent (Chain-of-Thought)"]
        KB[("ASTM / EPA / ISO Standard Operating Procedures")]
    end

    subgraph DIGITAL_TWIN ["5. Predictive Digital Twin & Persistence"]
        DB[("Async PostgreSQL / SQLite Time-Series Database")]
        TWIN["Digital Twin Engine (RUL Days & 45-Day Health Curves)"]
        AUDIT["Immutable ISO 9001 Metrological Audit Trail"]
    end

    subgraph OPERATIONS ["6. Cyber-Operations Mission Control"]
        DASH["Streamlit Industrial Operations Center (6 Tabs)"]
        SANDBOX["Interactive Hardware Failure Injection Sandbox"]
        ALERTS["Automated Webhook Dispatcher (PagerDuty / Slack)"]
    end

    FIELD --> EDGE_AGENTS
    EDGE_AGENTS -->|Online Stream| BROKER --> API
    BACKOFF -->|Reconnected Flush| API
    API --> VAL --> DB
    API --> OTEL
    API --> PINN & ISO_FOREST & SEQ_AUTO
    PINN & ISO_FOREST & SEQ_AUTO -->|Anomaly Trip (Score >= 0.60)| SHAP
    SHAP --> AGENT
    KB <--> AGENT
    AGENT --> AUDIT --> DB
    AGENT --> ALERTS
    API --> TWIN --> DASH
    API --> WS --> DASH
    SANDBOX -.-> FIELD
```

---

## 🔬 Monitored Physical Telemetry & Failure Mode Catalog

StreamPulse AI models the continuous physical electrochemistry of analytical water instrumentation:

| Transducer Type | Monitored Metric | Nominal Range | Primary Failure Mode | Physical Mechanism & Standard Procedure |
| :--- | :--- | :--- | :--- | :--- |
| **Glass pH Electrode** | Potential / pH | $6.8 - 7.6\ \text{pH}$ | `JUNCTION_POISON` | Porous ceramic junction clogged by $\text{Ag}_2\text{S}$ precipitates; liquid junction potential distortion. **SOP-705**. |
| **Amperometric Potentiostat** | Current ($\mu\text{A}$) | $0.45 - 0.52\ \mu\text{A}$ | `BIOFOULING` | Organic biofilm passivating platinum working electrode; Cottrell electron transfer suppression. **SOP-410**. |
| **Optical Turbidimeter** | Turbidity (NTU) | $0.8 - 1.5\text{ NTU}$ | `CAVITATION_SPIKE` | Suction cavitation & microbubble scattering across $90^\circ$ optical beam. **EPA 180.1 / SOP-301**. |
| **Magnetic Flow Meter** | Flow Rate (LPM) | $14.0 - 16.0\text{ LPM}$ | `PUMP_SURGING` | Fluid cavitation, impeller wear, and mechanical ripple. **SOP-204**. |
| **Toroidal Conductivity** | Conductivity ($\mu\text{S/cm}$)| $300 - 400\ \mu\text{S/cm}$ | `SALT_DEPOSITION` | Mineral scaling altering inductive toroidal cell constant. **ISO 7888**. |
| **Pt100 RTD Sensor** | Temperature (${}^\circ\text{C}$) | $20.0 - 24.0{}^\circ\text{C}$ | `THERMAL_SHOCK` | RTD drift disrupting thermodynamic Nernst compensation. |
| **All Channels** | Signal-to-Noise (dB) | $>40\text{ dB}$ | `FLATLINE_FAIL` | Transducer membrane fracture or open-circuit BNC disconnect ($\sigma^2 \to 0,\ \text{SNR} < 5\text{ dB}$). **SOP-102**. |

---

## ⚡ The 5 Core Engineering Breakthroughs

### 1. Physics-Informed (PINN) Thermodynamic & Electrochemical Guardrails
Traditional ML treats sensor streams as abstract numbers. StreamPulse AI hardcodes the fundamental laws of chemical physics:
* **Dynamic Nernstian Slope Verification:**
  $$E_{\text{Nernst}}(T, \text{pH}) = E^0 - \frac{2.3026 \cdot R \cdot (T_{{}^\circ\text{C}} + 273.15)}{F} \cdot (\text{pH} - 7.0)$$
  Continuously computes theoretical sensitivity ($54 - 62\ \text{mV/pH}$) to distinguish real chemical pH excursions from reference electrode failure.
* **Cottrell Voltammetric Current Kinetics:**
  Tracks the effective electroactive surface area $A_{\text{eff}}(t)$ to detect sub-microamp biofilm passivation prior to signal flatlining.

### 2. Autonomous AI Diagnostic Agent with Chain-of-Thought (CoT)
Fulfills the core Sustaining Engineering mandate: *"Analyze probe failures to determine, document, and correct root causes."*
When an anomaly trips:
1. Extracts multi-modal telemetry vectors and TreeSHAP attribution percentages.
2. Queries an embedded vector store of **ASTM D1293**, **EPA 180.1**, and **ISO 17025** standard operating procedures.
3. Executes a multi-step Chain-of-Thought (CoT) reasoning workflow.
4. Generates an audit-grade diagnostic ticket with structured root-cause explanations and step-by-step remediation procedures.

### 3. Store-and-Forward Edge Buffering (Zero Data Loss)
Field industrial networks are inherently subject to WiFi/cellular dropouts:
* During network partitions, edge agents seamlessly buffer readings in a local SQLite persistent queue.
* Upon reconnection, an asynchronous worker flushes buffered packets in FIFO order using `tenacity` exponential backoff.
* Guarantees **zero data loss** across extended network disconnects.

### 4. Predictive Digital Twins & Remaining Useful Life (RUL)
Each sensor station runs a mathematical Digital Twin:
* Tracks operational runtime hours, thermal shocks, chemical stress cycles, and calibration drift.
* Forecasts a **45-day health degradation trajectory**:
  $$H(t) = H_0 \cdot \exp(-\lambda_{\text{stress}} \cdot t)$$
* Calculates Remaining Useful Life (RUL) in days, notifying technicians before probes breach the 70% recalibration threshold.

### 5. Enterprise Observability & Prometheus Metrics
* Native `/metrics` endpoint exposing custom gauges, counters, and latency histograms (`streampulse_*`).
* **Locust load testing benchmark** validates **5,240 packets/sec** throughput with **sub-15ms p99 latency**.

---

## 📊 Performance & Scalability Benchmarks

Detailed performance evaluation conducted via Locust load test simulating 100 concurrent industrial sensor skids:

| Benchmark Parameter | Measured Result | Production SLA Target | Compliance |
| :--- | :--- | :--- | :--- |
| **Sustained Ingestion Throughput** | **5,240 pkts/sec** | >3,000 pkts/sec | ✅ **174% of Target** |
| **Median Response Latency (p50)** | **2.1 ms** | < 5.0 ms | ✅ **Exceeds Target** |
| **95th Percentile Latency (p95)** | **6.8 ms** | < 10.0 ms | ✅ **Exceeds Target** |
| **99th Percentile Latency (p99)** | **14.2 ms** | < 15.0 ms | ✅ **Exceeds Target** |
| **Packet Drop Rate (150k Packets)** | **0.00%** | 0.00% | ✅ **Zero Data Loss** |
| **End-to-End AI Diagnostic Latency** | **18.4 ms** | < 50.0 ms | ✅ **Sub-50ms Real-Time** |

Full benchmark documentation available at [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md).

---

## 📡 API Contract & System Specifications

StreamPulse AI defines a comprehensive, strictly-typed API contract:
* **OpenAPI 3.1 Specification:** [`openapi.json`](openapi.json)
* **API Endpoint Reference:** [`docs/API_REFERENCE.md`](docs/API_REFERENCE.md)
* **Prometheus Metrics Specification:** [`docs/METRICS.md`](docs/METRICS.md)
* **Mathematical & System Design:** [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
* **Metrological & ISO Traceability Manual:** [`docs/ISO_COMPLIANCE.md`](docs/ISO_COMPLIANCE.md)
* **Public Pydantic Schemas:** [`interfaces/`](interfaces/)

---

## 🖥️ Cyber-Operations Mission Control Dashboard

The StreamPulse AI dashboard provides an operator-grade, high-density industrial control interface:

1. **Tab 1 — Fleet Overview & Digital Twins:** Fleet-wide health index gauges, operational stress parameters, and 45-day predictive RUL curves.
2. **Tab 2 — Real-Time Telemetry & PINN Guardrails:** Multi-channel live timeseries showing dynamic Nernstian envelopes, Cottrell voltammetry, turbidity, and pump flow ripple.
3. **Tab 3 — Autonomous AI Diagnostic Agent & TreeSHAP:** Live Chain-of-Thought (CoT) terminal logs, Shapley attribution waterfalls, and step-by-step ASTM remediation protocols.
4. **Tab 4 — Hardware Fault Injection Sandbox:** Real-time simulation of probe failure modes (Biofouling, Ceramic Junction Clogging, Cavitation, Flatline) with sub-300ms pipeline reaction.
5. **Tab 5 — Edge Store-and-Forward Simulation:** Interactive network partition toggle ("Drop Network" / "Reconnect") demonstrating zero data loss and edge queue draining.
6. **Tab 6 — Observability & Pipeline Performance:** Live p50, p95, p99 latency meters, ingestion throughput gauges, and direct links to Prometheus `/metrics`.

---

## 🔒 Enterprise Intellectual Property & Code Access Protocol

> ### 🛡️ Notice to Hiring Managers, Technical Evaluators & Engineering Leadership
> 
> Due to proprietary instrumentation simulation equations, commercial edge-buffering algorithms, and intellectual property considerations, **the core operational implementation source code is maintained in a private repository**.
>
> **What is shared publicly in this showcase repository:**
> * Complete OpenAPI 3.1 REST contracts (`openapi.json`)
> * Complete Prometheus observability specifications (`docs/METRICS.md`)
> * High-throughput performance and load-testing benchmarks (`docs/BENCHMARKS.md`)
> * Full mathematical formulations, physics guardrail proofs, and sequence diagrams (`docs/ARCHITECTURE.md`)
> * Public Pydantic data schemas and interface specifications (`interfaces/`)
> * Microservice container orchestration topologies (`docker-compose.spec.yml`)
>
> **Full Code Access & Technical Deep-Dive:**  
> Full private repository access, live containerized Docker deployment bundles, and an interactive 1-on-1 technical architectural walkthrough are gladly provided to engineering leadership and hiring managers upon request.
>
> **Contact for Code Access:**  
> **Sumesh Chakkaravarthi**  
> 📧 Email: sumeshchakkaravarthi@gmail.com  
> 💼 LinkedIn: [linkedin.com/in/sumesh-chakkaravarthi](https://linkedin.com/in/sumesh-chakkaravarthi)

---

## 📜 Regulatory & Metrology Standards Alignment

StreamPulse AI was built from the ground up to reflect the rigorous QA standards required in analytical instrumentation manufacturing:
* **ASTM D1293-18:** Standard Test Methods for pH of Water (Nernstian Slope Verification)
* **EPA Method 180.1:** Determination of Turbidity by Nephelometry
* **ISO/IEC 17025:2017:** General requirements for competence of testing and calibration laboratories
* **ISO 9001:2015 §8.5.1:** Control of Production and Service Provision (Metrological Audit Trail)
* **ISO 7888:1985:** Water quality — Determination of electrical conductivity

---

## 📄 License
MIT Showcase Evaluation License. Copyright © 2026 Sumesh Chakkaravarthi.

