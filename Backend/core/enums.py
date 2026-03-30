"""
Enumerations for the fraud detection system
"""

from enum import Enum


class PriorityLevel(str, Enum):
    """Priority levels for alerts"""
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFO = "Info"

class DetectionMethod(str, Enum):
    """Detection methods used"""
    ENSEMBLE = "Ensemble"
    SUPERVISED = "Supervised"
    UNSUPERVISED = "Unsupervised"
    BUSINESS_RULES = "Business Rules"
    HYBRID = "Hybrid"

class CaseStatus(str, Enum):
    """Case investigation status"""
    PENDING = "Pending"
    ASSIGNED = "Assigned"
    IN_REVIEW = "In Review"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    ESCALATED = "Escalated"