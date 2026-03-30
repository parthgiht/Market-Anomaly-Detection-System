"""
Alert Management API Endpoints
"""
import uuid
from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..models.alert import Alert, AlertCreate, AlertUpdate, AlertResponse
from ..services.alert_service import (
    create_alert,
    get_alert,
    get_all_alerts,
    get_alerts_by_priority,
    update_alert,
    delete_alert
)
from ..core.enums import PriorityLevel, CaseStatus
from ..core.logging import logger

router = APIRouter(prefix="/api/v1/alerts", tags=["Alerts"])


@router.post("/", response_model=Dict[str, Any])
async def create_new_alert(alert_data: AlertCreate) -> Dict[str, Any]:
    """
    Create a new alert
    
    Args:
        alert_data: Alert creation data
    
    Returns:
        Created alert details
    """
    try:
        logger.info(f"Creating alert for transaction: {alert_data.transaction_id}")
        
        alert = create_alert(
            transaction_id=alert_data.transaction_id or f"TXN_{uuid.uuid4().hex[:12].upper()}",
            user_id=alert_data.user_id,
            amount=alert_data.amount,
            risk_score=alert_data.risk_score,
            priority=alert_data.priority,
            description=alert_data.description
        )
        
        return alert
    
    except Exception as e:
        logger.error(f"Error creating alert: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error creating alert: {str(e)}")


@router.get("/", response_model=List[Dict[str, Any]])
async def list_all_alerts(
    priority: Optional[PriorityLevel] = Query(None, description="Filter by priority")
) -> List[Dict[str, Any]]:
    """
    Get all alerts with optional filtering
    
    Args:
        priority: Optional priority filter
    
    Returns:
        List of alerts
    """
    try:
        if priority:
            logger.info(f"Fetching alerts with priority: {priority}")
            return get_alerts_by_priority(priority)
        else:
            logger.info("Fetching all alerts")
            return get_all_alerts()
    
    except Exception as e:
        logger.error(f"Error fetching alerts: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching alerts: {str(e)}")


@router.get("/{alert_id}", response_model=Dict[str, Any])
async def get_alert_by_id(alert_id: str) -> Dict[str, Any]:
    """
    Get a specific alert by ID
    
    Args:
        alert_id: Alert ID
    
    Returns:
        Alert details
    """
    try:
        logger.info(f"Fetching alert: {alert_id}")
        alert = get_alert(alert_id)
        
        if not alert:
            logger.warning(f"Alert not found: {alert_id}")
            raise HTTPException(status_code=404, detail=f"Alert {alert_id} not found")
        
        return alert
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching alert: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching alert: {str(e)}")


@router.put("/{alert_id}", response_model=Dict[str, Any])
async def update_alert_details(alert_id: str, alert_update: AlertUpdate) -> Dict[str, Any]:
    """
    Update an alert
    
    Args:
        alert_id: Alert ID
        alert_update: Update data
    
    Returns:
        Updated alert details
    """
    try:
        logger.info(f"Updating alert: {alert_id}")
        
        updated_alert = update_alert(
            alert_id=alert_id,
            status=alert_update.status,
            assigned_to=alert_update.assigned_to,
            notes=alert_update.notes
        )
        
        if not updated_alert:
            logger.warning(f"Alert not found for update: {alert_id}")
            raise HTTPException(status_code=404, detail=f"Alert {alert_id} not found")
        
        return updated_alert
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating alert: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error updating alert: {str(e)}")


@router.delete("/{alert_id}", response_model=Dict[str, str])
async def delete_alert_by_id(alert_id: str) -> Dict[str, str]:
    """
    Delete an alert
    
    Args:
        alert_id: Alert ID
    
    Returns:
        Deletion confirmation
    """
    try:
        logger.info(f"Deleting alert: {alert_id}")
        
        success = delete_alert(alert_id)
        
        if not success:
            logger.warning(f"Alert not found for deletion: {alert_id}")
            raise HTTPException(status_code=404, detail=f"Alert {alert_id} not found")
        
        return {"message": f"Alert {alert_id} deleted successfully"}
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting alert: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error deleting alert: {str(e)}")


@router.get("/stats/summary", response_model=Dict[str, Any])
async def get_alerts_summary() -> Dict[str, Any]:
    """
    Get alerts summary statistics
    
    Returns:
        Alert statistics
    """
    try:
        alerts = get_all_alerts()
        
        critical = sum(1 for a in alerts if a['priority'] == PriorityLevel.CRITICAL)
        high = sum(1 for a in alerts if a['priority'] == PriorityLevel.HIGH)
        medium = sum(1 for a in alerts if a['priority'] == PriorityLevel.MEDIUM)
        low = sum(1 for a in alerts if a['priority'] == PriorityLevel.LOW)

        pending = sum(1 for a in alerts if a['status'] == CaseStatus.PENDING)
        assigned = sum(1 for a in alerts if a['status'] == CaseStatus.ASSIGNED)
        resolved = sum(1 for a in alerts if a['status'] == CaseStatus.RESOLVED)
        
        return {
            'total_alerts': len(alerts),
            'by_priority': {
                'critical': critical,
                'high': high,
                'medium': medium,
                'low': low
            },
            'by_status': {
                'pending': pending,
                'assigned': assigned,
                'resolved': resolved
            },
            'timestamp': datetime.now()
        }
    
    except Exception as e:
        logger.error(f"Error getting alert summary: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting summary: {str(e)}")