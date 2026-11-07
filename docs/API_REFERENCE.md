# StreamPulse AI — REST & Streaming API Reference

The StreamPulse AI Ingestion & Diagnostic Core exposes a high-performance REST API and WebSocket streaming interface built with FastAPI.

Full OpenAPI 3.1 specification available at [`docs/openapi.json`](openapi.json).

---

## 1. Endpoints Summary

### Telemetry Ingestion
- `POST /api/v1/telemetry`: Ingests a single real-time sensor packet with Pydantic validation and physics checking.
- `POST /api/v1/telemetry/batch`: Ingests multi-sensor skid packets in bulk with atomic queuing.
- `GET /api/v1/telemetry/latest`: Fetches the latest telemetry frame across all stations.
- `GET /api/v1/telemetry/history`: Retrieves rolling historical telemetry frames with filtering by `node_id` and `limit`.
- `WS /ws/telemetry`: Full-duplex WebSocket broadcasting real-time sensor packets and anomaly notifications.

### Hardware Stations & Digital Twins
- `GET /api/v1/nodes`: Lists registered sensor stations, active probe types, and installation dates.
- `GET /api/v1/digital-twins`: Fetches operational state, remaining useful life (RUL), and health score for all stations.
- `GET /api/v1/digital-twins/{node_id}/forecast`: Generates a 45-day degradation forecast curve based on cumulative stress cycles.

### Edge Computing & Store-and-Forward
- `GET /api/v1/edge/status`: Queries network partition status and SQLite queue depths across edge nodes.
- `POST /api/v1/edge/partition-toggle`: Simulates field network disconnection / reconnection on a target node.
- `POST /api/v1/edge/flush/{node_id}`: Triggers immediate draining of an edge node's local backlog.

### Anomaly Incident Management & ISO Sign-Off
- `GET /api/v1/anomalies`: Lists open and historical anomaly incidents with ASTM SOP codes and TreeSHAP feature attributions.
- `POST /api/v1/anomalies/resolve/{incident_uuid}`: Allows Sustaining Engineers to log corrective actions and sign off for ISO 9001 audit compliance.

### Hardware Simulator Sandbox
- `POST /api/v1/simulator/inject-fault`: Dynamically triggers real-world probe failure modes (biofouling, junction poisoning, cavitation, flatline).
- `POST /api/v1/simulator/clear-fault`: Clears injected faults and resets probes to nominal baseline.

### System Health & Observability
- `GET /api/v1/health`: Ingestion pipeline readiness and database connectivity probe.
- `GET /api/v1/observability/stats`: In-memory latency tracker returning p50, p95, p99 percentiles and ingestion frequency (Hz).
- `GET /metrics`: Standard Prometheus scrape endpoint exposing custom `streampulse_*` metrics.

---

## 2. Example Payloads

### Ingesting Single Telemetry (`POST /api/v1/telemetry`)
```json
{
  "node_id": "NODE-WA-01",
  "timestamp": "2026-11-06T18:28:14.236Z",
  "ph": 7.14,
  "temperature_c": 22.4,
  "turbidity_ntu": 1.15,
  "flow_rate_lpm": 14.8,
  "conductivity_us_cm": 342.0,
  "electrochemical_current_ua": 0.485,
  "applied_potential_v": 0.45,
  "snr_db": 44.8,
  "calibration_status": "VALID"
}
```

### Anomaly Incident Response (`GET /api/v1/anomalies`)
```json
[
  {
    "incident_uuid": "INC-A94D182E",
    "node_id": "NODE-WA-01",
    "detected_at": "2026-11-06T18:28:14.236Z",
    "fault_type": "BIOFOULING_ELECTRODE_SCALING",
    "severity": "HIGH",
    "composite_score": 0.884,
    "confidence": 0.941,
    "astm_sop_code": "ASTM D1293 / SOP-410",
    "shap_contributions_json": {
      "electrochemical_current_ua": 0.42,
      "current_turbidity_ratio": 0.28,
      "pinn_violation_flag": 0.18,
      "ph_deviation": 0.08
    },
    "agent_report_json": {
      "suspected_failure_mode": "Working Electrode Passivation",
      "root_cause_explanation": "Severe reduction in Faradaic current density without turbidity spike indicates dielectric biofilm accumulation on platinum cell.",
      "remediation_protocol": [
        "Execute automated in-situ cathodic cleaning pulse (-1.2V for 15s).",
        "If recovery <10%, isolate cell and polish using 0.05um alumina slurry (SOP-410)."
      ]
    },
    "status": "OPEN"
  }
]
```
