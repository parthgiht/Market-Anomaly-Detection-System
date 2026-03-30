"""
Feedback Models
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class FeedbackInput(BaseModel):
    """Feedback for model improvement"""
    transaction_id: str
    alert_id: Optional[str] = None
    actual_label: bool = Field(..., description="True=fraud, False=legitimate")
    investigator: str
    notes: str
    confidence_rating: int = Field(..., ge=1, le=5)
    evidence_quality: str = Field(default="medium")


class FeedbackResponse(BaseModel):
    """Feedback response"""
    feedback_id: str
    transaction_id: str
    actual_label: bool
    created_at: datetime
    status: str = "Received"