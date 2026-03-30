"""
Case Investigation Models
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from ..core.enums import CaseStatus


class Case(BaseModel):
    """Investigation case"""
    case_id: str
    alert_id: str
    transaction_id: str
    investigator: str
    status: CaseStatus
    evidence: Dict[str, Any] = Field(default_factory=dict)
    decision: Optional[str] = None
    resolution_notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    resolved_at: Optional[datetime] = None


class CaseCreate(BaseModel):
    """Create case request"""
    alert_id: str
    transaction_id: str
    investigator: str


class CaseUpdate(BaseModel):
    """Update case request"""
    status: Optional[CaseStatus] = None
    evidence: Optional[Dict[str, Any]] = None
    decision: Optional[str] = None
    resolution_notes: Optional[str] = None