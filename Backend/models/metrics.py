"""
Metrics and Analytics Models
"""

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class ModelMetrics(BaseModel):
    """Model performance metrics"""
    detection_rate: float
    false_positive_rate: float
    precision: float
    recall: float
    f1_score: float
    accuracy: float
    total_transactions: int
    total_alerts: int
    confirmed_frauds: int
    false_positives: int
    timestamp: datetime


class UserProfile(BaseModel):
    """User behavior profile"""
    user_id: str
    transaction_count: int = 0
    total_amount: float = 0.0
    avg_transaction_amount: float = 0.0
    max_transaction_amount: float = 0.0
    fraud_incidents: int = 0
    risk_level: str = "Low"
    typical_merchants: List[str] = Field(default_factory=list)
    typical_locations: List[str] = Field(default_factory=list)
    device_types: List[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime