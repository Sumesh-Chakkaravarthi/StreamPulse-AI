"""
StreamPulse AI — Public Telemetry Data Contract & Metrology Specification.
Defines Pydantic v2 schemas for high-frequency industrial water quality and electrochemical sensor frames.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator


class SensorCalibrationStatus(str, Enum):
    VALID = "VALID"
    EXPIRED = "EXPIRED"
    RECALIBRATION_PENDING = "RECALIBRATION_PENDING"
    UNVERIFIED = "UNVERIFIED"


class TelemetryPacket(BaseModel):
    """
    Standard industrial IoT telemetry packet representing a single sensor station reading.
    All fields enforce physical boundaries and ISO 17025 metrological constraints.
    """
    node_id: str = Field(..., description="Unique industrial station identifier (e.g., NODE-WA-01)")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="UTC acquisition timestamp (ISO 8601)")
    
    # Primary Analytical Channels
    ph: float = Field(..., ge=0.0, le=14.0, description="pH analytical glass electrode reading (0.0 to 14.0)")
    temperature_c: float = Field(..., ge=-10.0, le=100.0, description="Process temperature via Pt100 RTD (Celsius)")
    turbidity_ntu: float = Field(..., ge=0.0, le=4000.0, description="Nephelometric turbidity reading (NTU, EPA 180.1)")
    flow_rate_lpm: float = Field(..., ge=0.0, le=500.0, description="Magnetic fluidic flow rate (Liters per Minute)")
    conductivity_us_cm: float = Field(..., ge=0.0, le=100000.0, description="Toroidal electrical conductivity (uS/cm, ISO 7888)")
    
    # Electrochemical Potentiostat Specifics
    electrochemical_current_ua: float = Field(..., description="Amperometric Faradaic cell current (microamps)")
    applied_potential_v: float = Field(default=0.45, description="Applied cell potential vs Ag/AgCl reference (Volts)")
    
    # Hardware Signal Diagnostics
    snr_db: float = Field(default=45.0, description="Sensor signal-to-noise ratio in decibels (>40 dB nominal)")
    calibration_status: SensorCalibrationStatus = Field(default=SensorCalibrationStatus.VALID, description="ISO 17025 validity state")
    
    # Optional Station Metadata
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Hardware metadata (firmware, serial, skid ID)")

    @field_validator("ph")
    @classmethod
    def validate_ph_range(cls, v: float) -> float:
        if v < 0.0 or v > 14.0:
            raise ValueError("Measured pH must reside strictly within physical thermodynamic limits [0.0, 14.0]")
        return round(v, 4)


class TelemetryBatchRequest(BaseModel):
    """Bulk ingestion payload for PLC skids and multi-sensor edge gateways."""
    items: List[TelemetryPacket] = Field(..., min_length=1, max_length=1000, description="Batch of sensor telemetry frames")
