# Custom exceptions - To be implemented
"""
Custom exceptions for the fraud detection system
"""


class FraudDetectionException(Exception):
    """Base exception for fraud detection"""
    pass


class DetectionServiceException(FraudDetectionException):
    """Exception in detection service"""
    pass


class ValidationException(FraudDetectionException):
    """Data validation exception"""
    pass


class TransactionNotFound(FraudDetectionException):
    """Transaction not found exception"""
    pass


class AlertNotFound(FraudDetectionException):
    """Alert not found exception"""
    pass


class CaseNotFound(FraudDetectionException):
    """Case not found exception"""
    pass


class UnauthorizedException(FraudDetectionException):
    """Unauthorized access exception"""
    pass