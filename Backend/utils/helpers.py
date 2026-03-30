# Helper functions - To be implemented
"""
Helper functions and utilities
"""

import uuid
from datetime import datetime
from typing import Optional


# TXN_9f3a82c1   → Transaction
# ALERT_12ab90  → Fraud alert
# CASE_00321    → Investigation case

def generate_id(prefix: str) -> str:
    """
    Generate unique ID with prefix
    
    Args:
        prefix: ID prefix (e.g., 'TXN', 'ALERT', 'CASE')
    
    Returns:
        Formatted unique ID
    """
    return f"{prefix}_{uuid.uuid4().hex[:12].upper()}"


def get_current_timestamp() -> datetime:
    """
    Get current timestamp
    
    Returns:
        Current datetime
    """
    return datetime.now()


def format_timestamp(dt: datetime) -> str:
    """
    Format datetime to ISO string
    
    Args:
        dt: Datetime to format
    
    Returns:
        ISO formatted string
    """
    return dt.isoformat()


def parse_timestamp(timestamp_str: str) -> Optional[datetime]:
    """
    Parse ISO timestamp string
    
    Args:
        timestamp_str: ISO formatted timestamp string
    
    Returns:
        Datetime object or None if parsing fails
    """
    try:
        return datetime.fromisoformat(timestamp_str)
    except (ValueError, TypeError):
        return None


def round_float(value: float, decimals: int = 2) -> float:
    """
    Round float to specified decimals
    
    Args:
        value: Float value to round
        decimals: Number of decimal places
    
    Returns:
        Rounded float
    """
    return round(value, decimals)