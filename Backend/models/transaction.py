"""
Transaction Pydantic Models
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict
from datetime import datetime
import uuid


class TransactionInput(BaseModel):
    """Input transaction for fraud detection"""
    transaction_id: Optional[str] = Field(None, description="Unique transaction ID")
    user_id: str = Field(..., description="User identifier")
    amount: float = Field(..., gt=0, description="Transaction amount")
    merchant_id: Optional[str] = Field(None, description="Merchant identifier")
    merchant_category: Optional[str] = Field(None, description="Merchant category")
    location: Optional[str] = Field(None, description="Transaction location")
    device_type: Optional[str] = Field(None, description="Device used")
    timestamp: Optional[datetime] = Field(None, description="Transaction timestamp")
    
    is_international: bool = Field(default=False, description="Is international?")
    is_online: bool = Field(default=True, description="Is online?")
    card_present: bool = Field(default=False, description="Was card present?")
    
    features: Optional[Dict[str, float]] = Field(None, description="Feature vector")
    
    @field_validator('transaction_id', mode='before')
    @classmethod
    def set_transaction_id(cls, v):
        return v or f"TXN_{uuid.uuid4().hex[:12].upper()}"
    
    @field_validator('timestamp', mode='before')
    @classmethod
    def set_timestamp(cls, v):
        return v or datetime.now()
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "USER_12345",
                "amount": 1299.99,
                "merchant_category": "electronics",
                "location": "New York, NY"
            }
        }


class TransactionResponse(BaseModel):
    """Transaction response"""
    transaction_id: str
    user_id: str
    amount: float
    timestamp: datetime
    status: str = "Success"