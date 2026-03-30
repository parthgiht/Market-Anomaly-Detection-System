# Case management service - To be implemented
"""
Case Management Service
"""

from datetime import datetime
from typing import Dict, Optional, List, Any
from ..core.enums import CaseStatus
from ..utils.helpers import generate_id
from ..core.logging import logger

# In-memory cases storage
cases: Dict = {}


def create_case(
    alert_id: str,
    transaction_id: str,
    investigator: str
) -> Dict:
    """Create a new case"""
    case_id = generate_id("CASE")
    
    case = {
        'case_id': case_id,
        'alert_id': alert_id,
        'transaction_id': transaction_id,
        'investigator': investigator,
        'status': CaseStatus.PENDING,
        'evidence': {},
        'decision': None,
        'resolution_notes': None,
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
        'resolved_at': None
    }
    
    cases[case_id] = case
    logger.info(f"Case created: {case_id} for alert {alert_id}")
    
    return case


def get_case(case_id: str) -> Optional[Dict]:
    """Get case by ID"""
    return cases.get(case_id)


def get_all_cases() -> List[Dict]:
    """Get all cases"""
    return list(cases.values())


def get_cases_by_status(status: CaseStatus) -> List[Dict]:
    """Get cases by status"""
    return [c for c in cases.values() if c['status'] == status]


def update_case(
    case_id: str,
    status: Optional[CaseStatus] = None,
    evidence: Optional[Dict[str, Any]] = None,
    decision: Optional[str] = None,
    resolution_notes: Optional[str] = None
) -> Optional[Dict]:
    """Update case"""
    if case_id not in cases:
        logger.warning(f"Case not found: {case_id}")
        return None
    
    case = cases[case_id]
    
    if status:
        case['status'] = status
        if status == CaseStatus.RESOLVED:
            case['resolved_at'] = datetime.now()
    
    if evidence:
        case['evidence'].update(evidence)
    
    if decision:
        case['decision'] = decision
    
    if resolution_notes:
        case['resolution_notes'] = resolution_notes
    
    case['updated_at'] = datetime.now()
    
    logger.info(f"Case updated: {case_id}")
    
    return case


def delete_case(case_id: str) -> bool:
    """Delete case"""
    if case_id in cases:
        del cases[case_id]
        logger.info(f"Case deleted: {case_id}")
        return True
    return False