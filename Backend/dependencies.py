# Dependency injection - To be implemented
"""
Dependency Injection
"""

from functools import lru_cache
from .services.detector import MockEnsembleDetector, detector


@lru_cache()
def get_detector() -> MockEnsembleDetector:
    """Get detector instance"""
    return detector