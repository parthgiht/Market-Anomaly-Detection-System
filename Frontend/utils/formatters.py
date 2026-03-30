"""
Data Formatting Utilities
"""

from datetime import datetime
from typing import Any
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import COLORS


def format_currency(amount: float) -> str:
    """Format amount as currency"""
    return f"${amount:,.2f}"


def format_percentage(value: float, decimals: int = 2, is_ratio: bool = True) -> str:
    """Format value as percentage"""
    if is_ratio:
        value *= 100
    return f"{value:.{decimals}f}%"


def format_timestamp(timestamp: Any) -> str:
    """Format timestamp for display"""
    if isinstance(timestamp, str):
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except(ValueError, TypeError):
            return timestamp
    elif isinstance(timestamp, datetime):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return str(timestamp)


def format_number(number: float, decimals: int = 2) -> str:
    """Format number with thousands separator"""
    return f"{number:,.{decimals}f}"


def get_priority_color(priority: str) -> str:
    """Get color for priority level"""
    priority_upper = str(priority).upper()
    
    color_map = {
        "CRITICAL": COLORS["critical"],
        "HIGH": COLORS["high"],
        "MEDIUM": COLORS["medium"],
        "LOW": COLORS["low"],
        "INFO": COLORS["info"]
    }
    
    return color_map.get(priority_upper, "#999999")


def get_status_color(status: str) -> str:
    """Get color for status"""
    status_upper = str(status).upper()
    
    status_colors = {
        "PENDING": "#ffbb33",
        "ASSIGNED": "#33b5e5",
        "IN_REVIEW": "#33b5e5",
        "IN REVIEW": "#33b5e5",
        "RESOLVED": "#00C851",
        "CLOSED": "#666666",
        "ESCALATED": "#ff4444"
    }
    
    return status_colors.get(status_upper, "#999999")


def truncate_text(text: Any, max_length: int = 50) -> str:
    """Truncate text to maximum length"""
    if not text:
        return ""
    text = str(text)
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def format_risk_score(score: float) -> str:
    """Format risk score with color indicator"""
    score = max(0, min(score, 100))
    return f"{score:.2f}/100"


def get_risk_level(score: float) -> str:
    """Get risk level from score"""
    if score >= 90:
        return "CRITICAL"
    elif score >= 70:
        return "HIGH"
    elif score >= 50:
        return "MEDIUM"
    elif score >= 30:
        return "LOW"
    else:
        return "INFO"