"""
Streamlit Pages Package

This module defines metadata and structure for all Streamlit dashboard pages.
Each page is automatically discovered by Streamlit, but this file enables:

- Package-level imports
- Centralized page metadata
- Future programmatic navigation or access control
"""

# Page registry (optional but professional)
PAGES = {
    "Detection": {
        "file": "Detection.py",
        "icon": "🎯",
        "description": "Real-time fraud detection and risk analysis"
    },
    "Alerts": {
        "file": "Alerts.py",
        "icon": "🚨",
        "description": "Alert monitoring and management"
    },
    "Cases": {
        "file": "Cases.py",
        "icon": "📋",
        "description": "Fraud investigation case handling"
    },
    "Analytics": {
        "file": "Analytics.py",
        "icon": "📈",
        "description": "System analytics and performance metrics"
    },
    "Users": {
        "file": "Users.py",
        "icon": "👥",
        "description": "User profiles and behavioral insights"
    },
    "Feedback": {
        "file": "Feedback.py",
        "icon": "💬",
        "description": "Model feedback and learning signals"
    },
    "Settings": {
        "file": "Settings.py",
        "icon": "⚙️",
        "description": "System configuration and diagnostics"
    },
}

__all__ = ["PAGES"]
