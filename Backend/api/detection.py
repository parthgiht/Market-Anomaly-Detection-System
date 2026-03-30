"""
Fraud Detection API Endpoints
"""
import uuid
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any
from datetime import datetime

from ..models.transaction import TransactionInput, TransactionResponse
from ..models.detection import DetectionResult
from ..services.detector import detector
from ..services.user_service import update_user_profile
from ..services.alert_service import create_alert
from ..core.logging import logger

router = APIRouter(prefix="/api/v1/detection", tags=["Detection"])


@router.post("/detect", response_model=Dict[str, Any])
async def detect_fraud(transaction: TransactionInput) -> Dict[str, Any]:
    """
    Detect fraud in a transaction
    
    Args:
        transaction: Transaction input data
    
    Returns:
        Detection result with fraud score and recommendation
    """
    try:
        logger.info(f"Detecting fraud for transaction: {transaction.transaction_id}")
        
        # Perform detection
        detection_data = detector.detect(transaction)
        
        # Update user profile
        update_user_profile(transaction.user_id, transaction)
        
        # Create alert if fraud is detected
        if detection_data['is_fraud'] or detection_data['requires_review']:
            alert = create_alert(
                transaction_id=transaction.transaction_id,
                user_id=transaction.user_id,
                amount=transaction.amount,
                risk_score=detection_data['risk_score'],
                priority=detection_data['priority'],
                description=f"Suspicious transaction detected with risk score: {detection_data['risk_score']:.2f}"
            )
            detection_data['alert_id'] = alert.get('alert_id')
            logger.info(f"Alert created: {alert.get('alert_id')}")
        
        # Build response
        result = {
            'transaction_id': transaction.transaction_id or f"TXN_{uuid.uuid4().hex[:12].upper()}",
            'user_id': transaction.user_id,
            'amount': transaction.amount,
            'risk_score': detection_data['risk_score'],
            'is_fraud': detection_data['is_fraud'],
            'is_anomaly': detection_data['is_anomaly'],
            'priority': detection_data['priority'],
            'confidence': detection_data['confidence'],
            'model_scores': detection_data['model_scores'],
            'detection_method': detection_data['detection_method'],
            'anomaly_features': detection_data['anomaly_features'],
            'recommended_action': detection_data['recommended_action'],
            'requires_review': detection_data['requires_review'],
            'auto_blocked': detection_data['auto_blocked'],
            'timestamp': datetime.now(),
            'processing_time_ms': detection_data['processing_time_ms'],
            'alert_id': detection_data.get('alert_id')
        }
        
        return result
    
    except Exception as e:
        logger.error(f"Error detecting fraud: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Detection error: {str(e)}")


@router.post("/batch-detect", response_model=Dict[str, Any])
async def batch_detect_fraud(transactions: list[TransactionInput]) -> Dict[str, Any]:
    """
    Detect fraud in multiple transactions
    
    Args:
        transactions: List of transaction inputs
    
    Returns:
        List of detection results
    """
    try:
        logger.info(f"Batch detecting fraud for {len(transactions)} transactions")
        
        results = []
        alert_count = 0
        fraud_count = 0
        
        for transaction in transactions:
            detection_data = detector.detect(transaction)
            update_user_profile(transaction.user_id, transaction)
            
            if detection_data['is_fraud'] or detection_data['requires_review']:
                create_alert(
                    transaction_id=transaction.transaction_id,
                    user_id=transaction.user_id,
                    amount=transaction.amount,
                    risk_score=detection_data['risk_score'],
                    priority=detection_data['priority'],
                    description=f"Suspicious transaction detected"
                )
                alert_count += 1
            
            if detection_data['is_fraud']:
                fraud_count += 1
            
            results.append({
                'transaction_id': transaction.transaction_id,
                'risk_score': detection_data['risk_score'],
                'is_fraud': detection_data['is_fraud'],
                'priority': detection_data['priority']
            })
        
        return {
            'total_transactions': len(transactions),
            'fraud_detected': fraud_count,
            'alerts_created': alert_count,
            'results': results,
            'timestamp': datetime.now()
        }
    
    except Exception as e:
        logger.error(f"Error in batch detection: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Batch detection error: {str(e)}")


@router.get("/model-info", response_model=Dict[str, Any])
async def get_model_info() -> Dict[str, Any]:
    """Get model information and configuration"""
    from ..config import settings
    
    return {
        'models': {
            'xgboost': 'XGBoost Classifier',
            'isolation_forest': 'Isolation Forest',
            'lightgbm': 'LightGBM',
            'statistical': 'Statistical Methods'
        },
        'weights': {
            'xgboost': settings.XGBOOST_WEIGHT,
            'isolation_forest': settings.ISOLATION_FOREST_WEIGHT,
            'lightgbm': settings.LIGHTGBM_WEIGHT,
            'statistical': settings.STATISTICAL_WEIGHT
        },
        'thresholds': {
            'critical': settings.CRITICAL_THRESHOLD,
            'high': settings.HIGH_THRESHOLD,
            'medium': settings.MEDIUM_THRESHOLD,
            'low': settings.LOW_THRESHOLD,
            'detection': settings.DETECTION_THRESHOLD
        }
    }