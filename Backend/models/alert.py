"""
Alert Models
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..core.enums import PriorityLevel, CaseStatus


class Alert(BaseModel):
    """Alert model"""
    alert_id: str
    transaction_id: str
    user_id: str
    amount: float
    risk_score: float
    priority: PriorityLevel
    status: CaseStatus = CaseStatus.PENDING
    description: str
    assigned_to: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class AlertCreate(BaseModel):
    """Create alert request"""
    transaction_id: str
    user_id: str
    amount: float
    risk_score: float
    priority: PriorityLevel
    description: str


class AlertUpdate(BaseModel):
    """Update alert request"""
    status: Optional[CaseStatus] = None
    assigned_to: Optional[str] = None
    notes: Optional[str] = None


class AlertResponse(BaseModel):
    """Alert response"""
    alert_id: str
    transaction_id: str
    priority: PriorityLevel
    status: CaseStatus
    created_at: datetime