# User profile service - To be implemented
"""
User Profile Service
"""

from datetime import datetime
from typing import Dict, Optional
from ..models.transaction import TransactionInput
from ..core.logging import logger


# Simple in-memory user profiles storage
user_profiles: Dict = {}


def update_user_profile(user_id: str, transaction: TransactionInput) -> Optional[Dict]:
    """Update user behavior profile"""
    if user_id not in user_profiles:
        user_profiles[user_id] = {
            'user_id': user_id,
            'transaction_count': 0,
            'total_amount': 0.0,
            'avg_transaction_amount': 0.0,
            'max_transaction_amount': 0.0,
            'fraud_incidents': 0,
            'risk_level': 'LOW',
            'typical_merchants': [],
            'typical_locations': [],
            'device_types': [],
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    
    profile = user_profiles[user_id]
    profile['transaction_count'] += 1
    profile['total_amount'] += transaction.amount
    profile['avg_transaction_amount'] = (
        profile['total_amount'] / profile['transaction_count']
    )
    profile['max_transaction_amount'] = max(
        profile['max_transaction_amount'], 
        transaction.amount
    )
    
    # Update typical behaviors
    if (transaction.merchant_id and 
        transaction.merchant_id not in profile['typical_merchants']):
        profile['typical_merchants'].append(transaction.merchant_id)
    
    if (transaction.location and 
        transaction.location not in profile['typical_locations']):
        profile['typical_locations'].append(transaction.location)
    
    if (transaction.device_type and 
        transaction.device_type not in profile['device_types']):
        profile['device_types'].append(transaction.device_type)
    
    profile['updated_at'] = datetime.now()
    
    logger.debug(f"Updated profile for user: {user_id}")
    
    return profile


def get_user_profile(user_id: str) -> Optional[Dict]:
    """Get user profile"""
    return user_profiles.get(user_id)


def get_all_user_profiles() -> Dict:
    """Get all user profiles"""
    return user_profiles