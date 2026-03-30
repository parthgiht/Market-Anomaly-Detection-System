"""
API Client for Backend Communication
Complete implementation of all FastAPI endpoints
"""

import requests
from typing import Dict, Any, List, Optional
import streamlit as st


class APIClient:
    """API client for backend communication"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Optional[Dict]:
        """Make HTTP request to API"""
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.request(method, url, timeout=10, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {str(e)}")
            return None
        
    # ========================================================================
    # DETECTION ENDPOINTS
    # ========================================================================
    
    def detect_fraud(self, transaction_data: Dict) -> Optional[Dict]:
        """Submit transaction for anomaly detection"""
        return self._make_request("POST", "/detection/detect", json=transaction_data)
    
    def batch_detect_fraud(self, transactions: List[Dict]) -> Optional[Dict]:
        """Batch fraud detection"""
        return self._make_request("POST", "/detection/batch-detect", json=transactions)
    
    def get_model_info(self) -> Optional[Dict]:
        """Get model configuration info"""
        return self._make_request("GET", "/detection/model-info")
    

    # ========================================================================
    # ALERT ENDPOINTS
    # ========================================================================
    
    def get_all_alerts(self, priority: Optional[str] = None) -> Optional[List[Dict]]:
        """Get all alerts with optional priority filter"""
        params = {"priority": priority} if priority else {}
        return self._make_request("GET", "/alerts/", params=params)
    
    def get_alert(self, alert_id: str) -> Optional[Dict]:
        """Get specific alert"""
        return self._make_request("GET", f"/alerts/{alert_id}")
    
    def update_alert(self, alert_id: str, update_data: Dict) -> Optional[Dict]:
        """Update alert"""
        return self._make_request("PUT", f"/alerts/{alert_id}", json=update_data)
    
    def delete_alert(self, alert_id: str) -> Optional[Dict]:
        """Delete alert"""
        return self._make_request("DELETE", f"/alerts/{alert_id}")
    
    def get_alert_stats(self) -> Optional[Dict]:
        """Get alert statistics"""
        return self._make_request("GET", "/alerts/stats/summary")
    
    # ========================================================================
    # CASE ENDPOINTS
    # ========================================================================
    
    def get_all_cases(self, status: Optional[str] = None) -> Optional[List[Dict]]:
        """Get all cases with optional status filter"""
        params = {"status": status} if status else {}
        return self._make_request("GET", "/cases/", params=params)
    
    def get_case(self, case_id: str) -> Optional[Dict]:
        """Get specific case"""
        return self._make_request("GET", f"/cases/{case_id}")
    
    def create_case(self, case_data: Dict) -> Optional[Dict]:
        """Create new case"""
        return self._make_request("POST", "/cases/", json=case_data)
    
    def update_case(self, case_id: str, update_data: Dict) -> Optional[Dict]:
        """Update case"""
        return self._make_request("PUT", f"/cases/{case_id}", json=update_data)
    
    def delete_case(self, case_id: str) -> Optional[Dict]:
        """Delete case"""
        return self._make_request("DELETE", f"/cases/{case_id}")
    
    def get_case_stats(self) -> Optional[Dict]:
        """Get case statistics"""
        return self._make_request("GET", "/cases/stats/summary")
    
    # ========================================================================
    # METRICS ENDPOINTS
    # ========================================================================
    
    def get_system_metrics(self) -> Optional[Dict]:
        """Get system-wide metrics"""
        return self._make_request("GET", "/metrics/system")
    
    def get_performance_metrics(self) -> Optional[Dict]:
        """Get model performance metrics"""
        return self._make_request("GET", "/metrics/performance")
    
    def get_alerts_trend(self) -> Optional[Dict]:
        """Get alerts trend"""
        return self._make_request("GET", "/metrics/alerts-trend")
    
    def get_user_metrics(self, user_id: str) -> Optional[Dict]:
        """Get user-specific metrics"""
        return self._make_request("GET", f"/metrics/user/{user_id}")
    
    # ========================================================================
    # USER ENDPOINTS
    # ========================================================================
    
    def get_all_users(self, risk_level: Optional[str] = None) -> Optional[List[Dict]]:
        """Get all users"""
        params = {"risk_level": risk_level} if risk_level else {}
        return self._make_request("GET", "/users/", params=params)
    
    def get_user_profile(self, user_id: str) -> Optional[Dict]:
        """Get user profile"""
        return self._make_request("GET", f"/users/{user_id}")
    
    def get_user_transactions(self, user_id: str) -> Optional[Dict]:
        """Get user transactions"""
        return self._make_request("GET", f"/users/{user_id}/transactions")
    
    def get_user_behavior(self, user_id: str) -> Optional[Dict]:
        """Get user behavior"""
        return self._make_request("GET", f"/users/{user_id}/behavior")
    
    def get_users_summary(self) -> Optional[Dict]:
        """Get users summary"""
        return self._make_request("GET", "/users/stats/summary")
    
    # ========================================================================
    # FEEDBACK ENDPOINTS
    # ========================================================================
    
    def submit_feedback(self, feedback_data: Dict) -> Optional[Dict]:
        """Submit feedback"""
        return self._make_request("POST", "/feedback/", json=feedback_data)
    
    def get_all_feedback(self) -> Optional[List[Dict]]:
        """Get all feedback"""
        return self._make_request("GET", "/feedback/")
    
    def get_feedback(self, feedback_id: str) -> Optional[Dict]:
        """Get specific feedback"""
        return self._make_request("GET", f"/feedback/{feedback_id}")
    
    def get_feedback_summary(self) -> Optional[Dict]:
        """Get feedback summary"""
        return self._make_request("GET", "/feedback/stats/summary")
    
    # ========================================================================
    # HEALTH CHECK
    # ========================================================================
    
    def health_check(self) -> Optional[Dict]:
        """Check API health"""
        try:
            url = self.base_url.replace('/api/v1', '/health')
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None