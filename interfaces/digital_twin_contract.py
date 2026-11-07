"""
StreamPulse AI — Public Digital Twin & Prognostics Contract.
Defines schemas for hardware aging kinetics, Remaining Useful Life (RUL), and 45-day degradation forecast points.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class DigitalTwinState(BaseModel):
    """Real-time operational state and wear parameters of a physical transducer."""
    node_id: str = Field(..., description="Target sensor station identifier")
    health_index: float = Field(..., ge=0.0, le=100.0, description="Composite sensor health percentage (0-100%)")
    remaining_useful_life_days: int = Field(..., ge=0, description="Estimated days until recalibration/replacement threshold")
    operating_hours: float = Field(..., ge=0.0, description="Total continuous in-service runtime hours")
    stress_cycles: int = Field(..., ge=0, description="Cumulative count of thermal shocks, pressure spikes, and chemical extremes")
    last_calibrated_at: datetime = Field(..., description="Timestamp of most recent two-point NIST calibration")
    next_service_due: datetime = Field(..., description="Projected maintenance deadline")


class ForecastPoint(BaseModel):
    """Single point in a 45-day predictive health degradation trajectory."""
    day: int = Field(..., ge=1, le=90, description="Forecast day index")
    date_str: str = Field(..., description="Projected calendar date (YYYY-MM-DD)")
    projected_health: float = Field(..., ge=0.0, le=100.0, description="Projected health score percentage")
    confidence_upper: float = Field(..., ge=0.0, le=100.0, description="Upper bound 95% confidence interval")
    confidence_lower: float = Field(..., ge=0.0, le=100.0, description="Lower bound 95% confidence interval")
    status: str = Field(..., description="Regulatory status (NOMINAL, SERVICE_RECOMMENDED, CRITICAL)")


class DigitalTwinForecastResponse(BaseModel):
    """Complete prognostic report returned by /api/v1/digital-twins/{node_id}/forecast."""
    node_id: str = Field(..., description="Target sensor station identifier")
    generated_at: datetime = Field(default_factory=datetime.utcnow, description="Forecast calculation timestamp")
    state: DigitalTwinState = Field(..., description="Current operational state")
    forecast_points: list[ForecastPoint] = Field(..., description="Daily trajectory degradation curve")

