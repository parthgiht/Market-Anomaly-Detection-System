"""
Detection Result Models
"""

from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime
from ..core.enums import PriorityLevel, DetectionMethod


class DetectionResult(BaseModel):
    """Fraud detection result"""
    transaction_id: str
    user_id: str
    amount: float
    risk_score: float = Field(..., ge=0, le=100)
    is_fraud: bool
    is_anomaly: bool
    priority: PriorityLevel
    confidence: float = Field(..., ge=0, le=1)
    
    model_scores: Dict[str, float]
    detection_method: DetectionMethod
    anomaly_features: List[str] = Field(default_factory=list)
    
    recommended_action: str
    requires_review: bool
    auto_blocked: bool = Field(default=False)
    
    timestamp: datetime
    processing_time_ms: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "transaction_id": "TXN_ABC123",
                "user_id": "USER_123",
                "amount": 2500.00,
                "risk_score": 87.5,
                "is_fraud": True,
                "is_anomaly": True,
                "priority": "High",
                "confidence": 0.875
            }
        }

