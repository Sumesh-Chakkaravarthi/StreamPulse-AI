"""
StreamPulse AI — Public Incident & AI Diagnostic Contract.
Defines schemas for anomaly incidents, TreeSHAP feature attributions, and ISO 9001 Sustaining sign-offs.
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class AnomalySeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class IncidentStatus(str, Enum):
    OPEN = "OPEN"
    INVESTIGATING = "INVESTIGATING"
    RESOLVED = "RESOLVED"
    DISMISSED = "DISMISSED"


class AgentDiagnosticReport(BaseModel):
    """Structured root-cause diagnosis synthesized by the Autonomous AI Agent."""

    suspected_failure_mode: str = Field(
        ..., description="Classified physical hardware failure mode"
    )
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Diagnostic model confidence score"
    )
    astm_sop_code: str = Field(
        ..., description="Applicable ASTM / EPA / ISO standard procedure"
    )
    root_cause_explanation: str = Field(
        ..., description="Technical engineering rationale explaining the failure"
    )
    remediation_protocol: list[str] = Field(
        ..., description="Sequential steps for technician or sustaining engineer"
    )
    chain_of_thought_steps: list[str] = Field(
        ..., description="Step-by-step diagnostic reasoning log"
    )
    agent_latency_ms: float = Field(
        ..., description="Agent inference turnaround time in milliseconds"
    )


class AnomalyIncidentRecord(BaseModel):
    """Immutable audit record representing an instrumentation anomaly trip."""

    incident_uuid: str = Field(
        ..., description="Unique immutable incident identifier (e.g., INC-A1B2C3D4)"
    )
    node_id: str = Field(..., description="Target sensor station identifier")
    detected_at: datetime = Field(
        default_factory=datetime.utcnow, description="Detection timestamp (ISO 8601)"
    )
    severity: AnomalySeverity = Field(
        ..., description="Calculated operational severity"
    )
    composite_score: float = Field(
        ..., ge=0.0, le=1.0, description="Ensemble ML + PINN anomaly score"
    )

    # Explainable AI & Domain Attribution
    shap_contributions_json: dict[str, float] = Field(
        default_factory=dict, description="TreeSHAP marginal feature attributions"
    )
    pinn_violation: bool = Field(
        default=False, description="Whether physical thermodynamic bounds were breached"
    )
    agent_report: AgentDiagnosticReport | None = Field(
        None, description="Full autonomous agent diagnosis"
    )

    # ISO 9001 Metrological Sign-off
    status: IncidentStatus = Field(
        default=IncidentStatus.OPEN, description="Incident lifecycle state"
    )
    resolved_by: str | None = Field(None, description="Sustaining engineer identity")
    resolved_at: datetime | None = Field(None, description="Resolution timestamp")
    resolution_notes: str | None = Field(
        None, description="Corrective actions logged for ISO audit trail"
    )
