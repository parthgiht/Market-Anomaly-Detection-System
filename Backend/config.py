# Configuration and settings - To be implemented
"""
Configuration settings for FastAPI application
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings"""
    
    # Application info
    APP_NAME: str = "Fraud Detection & Alert System"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Real-time fraud detection and alert management"
    
    # Server config
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    
    # CORS settings
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    
    # Detection thresholds
    DETECTION_THRESHOLD: float = 0.5
    CRITICAL_THRESHOLD: float = 0.9
    HIGH_THRESHOLD: float = 0.7
    MEDIUM_THRESHOLD: float = 0.5
    LOW_THRESHOLD: float = 0.3
    
    # Model weights (for ensemble)
    XGBOOST_WEIGHT: float = 0.3
    ISOLATION_FOREST_WEIGHT: float = 0.25
    LIGHTGBM_WEIGHT: float = 0.25
    STATISTICAL_WEIGHT: float = 0.2
    
    # Business rules
    HIGH_AMOUNT_THRESHOLD: float = 5000.0
    INTERNATIONAL_BOOST: float = 15.0
    HIGH_AMOUNT_BOOST: float = 20.0
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()