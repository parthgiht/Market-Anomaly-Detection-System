"""
User Profile API Endpoints
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, List, Optional
from datetime import datetime

from ..services.user_service import (
    get_user_profile,
    get_all_user_profiles,
    update_user_profile
)
from ..models.metrics import UserProfile
from ..core.logging import logger

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.get("/{user_id}", response_model=Dict[str, Any])
async def get_user_profile_endpoint(user_id: str) -> Dict[str, Any]:
    """
    Get user profile
    
    Args:
        user_id: User ID
    
    Returns:
        User profile details
    """
    try:
        logger.info(f"Fetching user profile: {user_id}")
        
        profile = get_user_profile(user_id)
        
        if not profile:
            logger.warning(f"User profile not found: {user_id}")
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        
        return profile
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user profile: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching profile: {str(e)}")


@router.get("/", response_model=List[Dict[str, Any]])
async def list_all_users(
    risk_level: Optional[str] = Query(None, description="Filter by risk level")
) -> List[Dict[str, Any]]:
    """
    Get all user profiles with optional filtering
    
    Args:
        risk_level: Optional risk level filter (Low, Medium, High)
    
    Returns:
        List of user profiles
    """
    try:
        profiles = get_all_user_profiles()
        
        if risk_level:
            logger.info(f"Fetching users with risk level: {risk_level}")
            filtered = [p for p in profiles.values() if p['risk_level'] == risk_level.upper()]
            return filtered
        else:
            logger.info(f"Fetching all {len(profiles)} user profiles")
            return list(profiles.values())
    
    except Exception as e:
        logger.error(f"Error fetching user profiles: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching profiles: {str(e)}")


@router.get("/{user_id}/transactions", response_model=Dict[str, Any])
async def get_user_transactions(user_id: str) -> Dict[str, Any]:
    """
    Get user transaction summary
    
    Args:
        user_id: User ID
    
    Returns:
        User transaction statistics
    """
    try:
        logger.info(f"Fetching transactions for user: {user_id}")
        
        profile = get_user_profile(user_id)
        
        if not profile:
            logger.warning(f"User profile not found: {user_id}")
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        
        return {
            'user_id': user_id,
            'total_transactions': profile['transaction_count'],
            'total_amount': round(profile['total_amount'], 2),
            'avg_amount': round(profile['avg_transaction_amount'], 2),
            'max_amount': round(profile['max_transaction_amount'], 2),
            'fraud_incidents': profile['fraud_incidents']
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user transactions: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching transactions: {str(e)}")


@router.get("/{user_id}/behavior", response_model=Dict[str, Any])
async def get_user_behavior(user_id: str) -> Dict[str, Any]:
    """
    Get user behavior profile
    
    Args:
        user_id: User ID
    
    Returns:
        User behavior patterns
    """
    try:
        logger.info(f"Fetching behavior for user: {user_id}")
        
        profile = get_user_profile(user_id)
        
        if not profile:
            logger.warning(f"User profile not found: {user_id}")
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        
        return {
            'user_id': user_id,
            'risk_level': profile['risk_level'],
            'typical_merchants': profile['typical_merchants'],
            'typical_locations': profile['typical_locations'],
            'device_types': profile['device_types'],
            'created_at': profile['created_at'],
            'updated_at': profile['updated_at']
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user behavior: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching behavior: {str(e)}")


@router.get("/stats/summary", response_model=Dict[str, Any])
async def get_users_summary() -> Dict[str, Any]:
    """
    Get users summary statistics
    
    Returns:
        User statistics
    """
    try:
        profiles = get_all_user_profiles()
        
        if not profiles:
            return {
                'total_users': 0,
                'by_risk_level': {},
                'timestamp': datetime.now()
            }
        
        by_risk_level = {}
        for profile in profiles.values():
            risk = profile['risk_level']
            by_risk_level[risk] = by_risk_level.get(risk, 0) + 1
        
        avg_transactions = sum(p['transaction_count'] for p in profiles.values()) / len(profiles)
        total_amount = sum(p['total_amount'] for p in profiles.values())
        
        return {
            'total_users': len(profiles),
            'by_risk_level': by_risk_level,
            'avg_transactions_per_user': round(avg_transactions, 2),
            'total_transaction_amount': round(total_amount, 2),
            'timestamp': datetime.now()
        }
    
    except Exception as e:
        logger.error(f"Error getting users summary: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error getting summary: {str(e)}")