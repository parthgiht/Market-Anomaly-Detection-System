"""
Dashboard Configuration Settings
"""

# API Configuration
API_BASE_URL = "https://backend-market-anomaly-detection.onrender.com/api/v1"

# Dashboard Settings
APP_TITLE = "Market Anomaly Detection System"
APP_ICON = "🕵️‍♂️"
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# Auto-refresh Settings
AUTO_REFRESH_INTERVAL = 60000  # milliseconds (60 seconds)

# Page Configuration
PAGE_TITLES = {
    "overview": "Dashboard Overview",
    "detection": "Fraud Detection",
    "alerts": "Alert Management",
    "cases": "Case Management",
    "analytics": "Analytics & Metrics",
    "users": "User Profiles",
    "feedback": "Feedback System",
    "settings": "Settings"
}

# Color Scheme
COLORS = {
    "primary": "#1f77b4",
    "critical": "#ff4444",
    "high": "#ff8800",
    "medium": "#ffbb33",
    "low": "#00C851",
    "info": "#33b5e5"
}

# Chart Settings
CHART_HEIGHT = 400
CHART_TEMPLATE = "plotly_white"

# Table Settings
DEFAULT_PAGE_SIZE = 20
MAX_DISPLAY_ITEMS = 100
