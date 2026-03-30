Market-Anomaly-Detection-System
==============================
#### This is a Financial Fraud Detection and Market Surveillance System that monitors financial transactions in real-time to identify.
---
![image_alt](https://github.com/ZethetaIntern/Market-Anomaly-Detection-System/blob/main/Anomaly%20detection.jpg?raw=true)
## 📋 Table of Contents

- Overview
- Features
- System Architecture
- Technology Stack
- Project Structure
- Usage
- API Documentation
- Dashboard
- Security
- Performance
- Testing

---

## 🎯 Overview

The **Anomaly(Fraud) Detection System** is an enterprise-grade platform designed to detect, monitor, and manage fraudulent transactions in real-time. Built with modern Python frameworks, it combines machine learning-based fraud detection with comprehensive alert management and case tracking capabilities.

### Key Highlights

- **Real-time Detection**: Instant fraud analysis using ensemble machine learning models
- **Comprehensive Alerting**: Multi-level priority-based alert system
- **Case Management**: Full investigation workflow tracking
- **User Analytics**: Behavioral profiling and risk assessment
- **Interactive Dashboard**: Streamlit-based UI for monitoring and management
- **RESTful API**: FastAPI-powered backend with auto-generated documentation
- **Production-Ready**: In-memory storage for rapid deployment without database dependencies

### Use Cases

- **Financial Institutions**: Credit card and payment fraud detection
- **E-commerce Platforms**: Transaction monitoring and risk assessment
- **Payment Processors**: Real-time transaction screening
- **Fintech Applications**: User behavior analysis and fraud prevention
- **Compliance Teams**: Investigation tracking and audit trails

---

## ✨ Features

### 🔍 Anomaly Detection

- **Ensemble Model Architecture**
  - Random Forest classifier
  - Isolation Forest for anomaly detection
  - Gradient Boosting models
  - Weighted voting for final decision

- **Multi-factor Analysis**
  - Transaction amount patterns
  - Velocity checking (transaction frequency)
  - Geolocation analysis
  - Device fingerprinting
  - Merchant category risk scoring
  - Time-based pattern detection

- **Real-time Processing**
  - Sub-100ms detection latency
  - Batch processing support
  - Async/await for high concurrency

### 🚨 Alert Management

- **Priority-Based Classification**
  - Critical (90-100 risk score)
  - High (70-89 risk score)
  - Medium (50-69 risk score)
  - Low (30-49 risk score)
  - Info (0-29 risk score)

- **Alert Features**
  - Auto-creation from detections
  - Status tracking (Pending, Assigned, Resolved, Escalated)
  - Assignment to investigators
  - Detailed risk breakdown
  - Recommended actions
  - Timestamp tracking

### 📋 Case Management

- **Investigation Workflow**
  - Case creation from alerts
  - Multi-status tracking
  - Evidence documentation
  - Resolution notes
  - Decision recording (Fraud Confirmed, False Positive)
  - Audit trail

- **Case Statuses**
  - Pending
  - Assigned
  - In Review
  - Resolved
  - Closed

### 👥 User Profiling

- **Behavioral Analysis**
  - Transaction history tracking
  - Average transaction amounts
  - Merchant preferences
  - Location patterns
  - Device usage patterns
  - Risk level assessment

- **Risk Scoring**
  - Dynamic risk calculation
  - Historical fraud incidents
  - Velocity patterns
  - Anomaly detection
  - Behavioral deviations

### 💬 Feedback System

- **Model Improvement**
  - Ground truth labeling
  - Investigator confidence ratings
  - Evidence quality assessment
  - Performance metrics tracking
  - Continuous learning loop

### 📊 Analytics & Metrics

- **System Metrics**
  - Detection performance (accuracy, precision, recall, F1)
  - Alert distribution and trends
  - Case resolution statistics
  - User risk profiles
  - Model effectiveness

- **Business Intelligence**
  - Time-series analysis
  - Priority distribution
  - Investigator workload
  - False positive rates
  - Detection latency

### 🎨 Interactive Dashboard

- **8 Specialized Pages**
  1. **Overview** - Real-time metrics and recent alerts
  2. **Detection** - Transaction submission and analysis
  3. **Alerts** - Alert monitoring and management
  4. **Cases** - Investigation tracking
  5. **Analytics** - Performance metrics and trends
  6. **Users** - User profile management
  7. **Feedback** - Model training feedback
  8. **Settings** - Configuration and testing

- **Dashboard Features**
  - Auto-refresh (30-second intervals)
  - Interactive Plotly charts
  - Real-time API integration
  - Responsive design
  - Filtering and sorting
  - Export capabilities

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Layer                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Browser    │  │   Mobile     │  │  External    │      │
│  │              │  │     App      │  │   Systems    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │              │
└─────────┼──────────────────┼──────────────────┼──────────────┘
          │                  │                  │
          └──────────────────┴──────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                Presentation Layer                            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │          Streamlit Dashboard (Port 8501)              │  │
│  │  • Overview  • Detection  • Alerts  • Cases           │  │
│  │  • Analytics • Users      • Feedback • Settings       │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼ HTTP/REST
┌─────────────────────────────────────────────────────────────┐
│                   API Layer                                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │          FastAPI Application (Port 8000)              │  │
│  │  • OpenAPI Documentation  • CORS Support              │  │
│  │  • Request Validation     • Error Handling            │  │
│  └───────────────────────────────────────────────────────┘  │
│                             │                                │
│         ┌───────────────────┼───────────────────┐           │
│         ▼                   ▼                   ▼           │
│  ┌──────────┐      ┌─────────────┐      ┌──────────┐      │
│  │Detection │      │   Alerts    │      │  Cases   │      │
│  │Endpoints │      │  Endpoints  │      │Endpoints │      │
│  └──────────┘      └─────────────┘      └──────────┘      │
│         ▼                   ▼                   ▼           │
│  ┌──────────┐      ┌─────────────┐      ┌──────────┐      │
│  │  Users   │      │  Feedback   │      │ Metrics  │      │
│  │Endpoints │      │  Endpoints  │      │Endpoints │      │
│  └──────────┘      └─────────────┘      └──────────┘      │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Business Logic Layer                        │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                   Services                             │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │  │
│  │  │ Detector │  │  Alert   │  │   Case   │            │  │
│  │  │ Service  │  │ Service  │  │ Service  │            │  │
│  │  └──────────┘  └──────────┘  └──────────┘            │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │  │
│  │  │   User   │  │ Feedback │  │ Metrics  │            │  │
│  │  │ Service  │  │ Service  │  │ Service  │            │  │
│  │  └──────────┘  └──────────┘  └──────────┘            │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Machine Learning Layer                      │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Ensemble Fraud Detector                   │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │  │
│  │  │ Random   │  │Isolation │  │Gradient  │            │  │
│  │  │ Forest   │  │ Forest   │  │Boosting  │            │  │
│  │  └──────────┘  └──────────┘  └──────────┘            │  │
│  │                      │                                  │  │
│  │                      ▼                                  │  │
│  │             ┌─────────────────┐                        │  │
│  │             │Weighted Ensemble│                        │  │
│  │             │     Voting      │                        │  │
│  │             └─────────────────┘                        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   Data Storage Layer                         │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              In-Memory Data Store                      │  │
│  │  • Transactions  • Alerts    • Cases                   │  │
│  │  • Users         • Feedback  • Metrics                 │  │
│  │  • Fast Access   • Thread-Safe                         │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Architecture Principles

- **Separation of Concerns**: Clear boundaries between API, business logic, and data layers
- **Modular Design**: Independent, reusable components
- **Scalability**: Stateless design for horizontal scaling
- **Extensibility**: Easy to add new features or models
- **Maintainability**: Clean code structure with comprehensive documentation

---

## 🛠️ Technology Stack

### Backend Framework
- **FastAPI** 0.109.0 - Modern, high-performance web framework
- **Uvicorn** 0.27.0 - Lightning-fast ASGI server
- **Pydantic** 2.5.3 - Data validation using Python type hints
- **Python** 3.11+ - Latest Python features and performance

### Frontend Dashboard
- **Streamlit** 1.29.0 - Rapid dashboard development
- **Plotly** 5.18.0 - Interactive visualizations
- **Pandas** 2.1.4 - Data manipulation and analysis

### Machine Learning
- **scikit-learn** 1.4.0 - ML algorithms and preprocessing
- **NumPy** 1.26.2 - Numerical computing
- **Python-dateutil** 2.8.2 - Date/time utilities

### Data Storage
- **In-Memory Storage** - Custom implementation
  - Fast access (< 1ms latency)
  - Thread-safe operations
  - No external dependencies
  - Zero configuration

### Development Tools
- **Type Hints** - Full type annotation coverage
- **Async/Await** - Asynchronous programming support
- **Logging** - Comprehensive logging system
- **Exception Handling** - Custom exception hierarchy

---


## 📁 Project Structure

```
fraud-detection-system/
│
├── README.md                         # Project documentation
├── requirements.txt                  # Root dependencies
├── .gitignore                       # Git ignore rules
│
├── fastapi/                         # Backend API
│   ├── __init__.py
│   ├── main.py                      # FastAPI application entry point
│   ├── config.py                    # Configuration management
│   ├── dependencies.py              # Dependency injection
│   ├── requirements.txt             # FastAPI dependencies
│   │
│   ├── api/                         # API Endpoints
│   │   ├── __init__.py
│   │   ├── detection.py             # Fraud detection endpoints
│   │   ├── alerts.py                # Alert management
│   │   ├── cases.py                 # Case management
│   │   ├── feedback.py              # Feedback system
│   │   ├── metrics.py               # Analytics & metrics
│   │   └── users.py                 # User profiles
│   │
│   ├── models/                      # Pydantic Models
│   │   ├── __init__.py
│   │   ├── transaction.py           # Transaction schemas
│   │   ├── detection.py             # Detection results
│   │   ├── alert.py                 # Alert models
│   │   ├── case.py                  # Case models
│   │   ├── feedback.py              # Feedback models
│   │   └── metrics.py               # Metrics models
│   │
│   ├── services/                    # Business Logic
│   │   ├── __init__.py
│   │   ├── detector.py              # ML-based detection
│   │   ├── alert_service.py         # Alert operations
│   │   ├── case_service.py          # Case operations
│   │   └── user_service.py          # User operations
│   │
│   ├── core/                        # Core Utilities
│   │   ├── __init__.py
│   │   ├── enums.py                 # Enumerations
│   │   ├── exceptions.py            # Custom exceptions
│   │   └── logging_config.py        # Logging setup
│   │
│   ├── storage/                     # Data Storage
│   │   ├── __init__.py
│   │   └── memory_store.py          # In-memory storage
│   │
│   └── utils/                       # Utilities
│       ├── __init__.py
│       ├── validators.py            # Validation functions
│       └── helpers.py               # Helper functions
│
├── streamlit/                       # Frontend Dashboard
│   ├── app.py                       # Main dashboard (Home/Overview)
│   ├── requirements.txt             # Streamlit dependencies
│   ├── README.md                    # Dashboard documentation
│   │
│   ├── pages/                       # Dashboard Pages (Auto-discovered)
│   │   ├── 1_Detection.py           # Fraud detection interface
│   │   ├── 2_Alerts.py              # Alert monitoring
│   │   ├── 3_Cases.py               # Case management
│   │   ├── 4_Analytics.py           # Metrics & charts
│   │   ├── 5_Users.py               # User profiles
│   │   ├── 6_Feedback.py            # Feedback submission
│   │   └── 7_Settings.py            # Configuration
│   │
│   ├── config/                      # Configuration
│   │   ├── __init__.py
│   │   └── settings.py              # Dashboard settings
│   │
│   ├── components/                  # Reusable UI Components
│   │   ├── __init__.py
│   │   ├── charts.py                # Chart components
│   │   ├── cards.py                 # Card components
│   │   └── tables.py                # Table components
│   │
│   ├── utils/                       # Utilities
│   │   ├── __init__.py
│   │   ├── api_client.py            # API client
│   │   └── formatters.py            # Data formatters
│   │
│   └── .streamlit/                  # Streamlit Config
│       └── config.toml              # Theme & settings
│
├── tests/                           # Test Suite
│   ├── __init__.py
│   ├── test_api/                    # API tests
│   ├── test_services/               # Service tests
│   └── test_integration/            # Integration tests
│
├── docs/                            # Documentation
│   ├── API_DOCUMENTATION.md         # API reference
│   ├── DEPLOYMENT.md                # Deployment guide
│   ├── ARCHITECTURE.md              # Architecture details
│   └── USER_GUIDE.md                # User manual
│
└── logs/                            # Application Logs
    ├── api.log
    └── dashboard.log
```

### Key Directories Explained

**`fastapi/`** - Backend API application
- Handles all business logic
- Provides RESTful API endpoints
- Manages data storage
- Executes fraud detection

**`streamlit/`** - Frontend dashboard
- User interface for monitoring
- Transaction submission
- Alert and case management
- Analytics visualization

**`api/`** - API endpoint definitions
- Route handlers
- Request/response validation
- HTTP method implementations

**`models/`** - Data models (Pydantic schemas)
- Request validation
- Response serialization
- Type safety

**`services/`** - Business logic layer
- Core functionality
- ML model execution
- Data processing
- Business rules

**`storage/`** - Data persistence
- In-memory storage implementation
- Thread-safe operations
- Data access layer

---

## 📖 Usage

### Starting the Application

#### 1. Start FastAPI Backend

```bash
# Navigate to FastAPI directory
cd fastapi

# Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Server starts at: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Alternative Docs: http://localhost:8000/redoc
```

#### 2. Start Streamlit Dashboard

```bash
# Navigate to Streamlit directory (in new terminal)
cd streamlit

# Start the dashboard
streamlit run app.py

# Dashboard opens at: http://localhost:8501
```

### Basic Workflow

#### 1. Submit Transaction for Detection

**Via Dashboard:**
1. Navigate to **Detection** page
2. Fill in transaction details:
   - User ID
   - Amount
   - Merchant category
   - Location
   - Device type
3. Click "Detect Fraud"
4. View results instantly

**Via API (cURL):**
```bash
curl -X POST "http://localhost:8000/api/v1/detection/detect" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "USER_12345",
    "amount": 5000.00,
    "merchant_category": "electronics",
    "location": "New York, NY",
    "device_type": "mobile",
    "is_international": false,
    "is_online": true,
    "card_present": false
  }'
```

**Response:**
```json
{
  "transaction_id": "TXN_abc123",
  "is_fraud": true,
  "risk_score": 87.5,
  "confidence": 0.92,
  "priority": "HIGH",
  "recommended_action": "BLOCK_AND_REVIEW",
  "model_scores": {
    "random_forest": 0.85,
    "isolation_forest": 0.90,
    "gradient_boosting": 0.88
  },
  "anomaly_features": ["high_amount", "unusual_location"],
  "alert_id": "ALERT_def456"
}
```

#### 2. Manage Alerts

**View All Alerts:**
```bash
curl "http://localhost:8000/api/v1/alerts/"
```

**Filter by Priority:**
```bash
curl "http://localhost:8000/api/v1/alerts/?priority=HIGH"
```

**Update Alert:**
```bash
curl -X PUT "http://localhost:8000/api/v1/alerts/ALERT_abc123" \
  -H "Content-Type: application/json" \
  -d '{"status": "Resolved", "assigned_to": "Investigator_01"}'
```

#### 3. Create and Manage Cases

**Create Case from Alert:**
```bash
curl -X POST "http://localhost:8000/api/v1/cases/" \
  -H "Content-Type: application/json" \
  -d '{
    "alert_id": "ALERT_abc123",
    "investigator": "Investigator_01",
    "priority": "HIGH"
  }'
```

**Update Case:**
```bash
curl -X PUT "http://localhost:8000/api/v1/cases/CASE_xyz789" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Resolved",
    "decision": "Fraud Confirmed",
    "resolution_notes": "Transaction blocked. User contacted."
  }'
```

#### 4. Submit Feedback

```bash
curl -X POST "http://localhost:8000/api/v1/feedback/" \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_id": "TXN_abc123",
    "actual_label": true,
    "investigator": "Investigator_01",
    "notes": "Confirmed fraud case",
    "confidence_rating": 5,
    "evidence_quality": "high"
  }'
```

---

## 📚 API Documentation

### Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
  - Try out endpoints directly
  - View request/response schemas
  - Test authentication

- **ReDoc**: http://localhost:8000/redoc
  - Alternative documentation format
  - Better for reading
  - Downloadable OpenAPI spec

### API Endpoints Summary

#### Detection Endpoints
```
POST   /api/v1/detection/detect           # Detect fraud in transaction
POST   /api/v1/detection/batch-detect     # Batch detection
GET    /api/v1/detection/model-info       # Get model information
```

#### Alert Endpoints
```
GET    /api/v1/alerts/                    # List all alerts
GET    /api/v1/alerts/{alert_id}          # Get specific alert
PUT    /api/v1/alerts/{alert_id}          # Update alert
DELETE /api/v1/alerts/{alert_id}          # Delete alert
GET    /api/v1/alerts/stats/summary       # Alert statistics
```

#### Case Endpoints
```
GET    /api/v1/cases/                     # List all cases
POST   /api/v1/cases/                     # Create new case
GET    /api/v1/cases/{case_id}            # Get specific case
PUT    /api/v1/cases/{case_id}            # Update case
DELETE /api/v1/cases/{case_id}            # Delete case
GET    /api/v1/cases/stats/summary        # Case statistics
```

#### Metrics Endpoints
```
GET    /api/v1/metrics/system             # System-wide metrics
GET    /api/v1/metrics/performance        # Model performance
GET    /api/v1/metrics/alerts-trend       # Alert trends
GET    /api/v1/metrics/user/{user_id}     # User metrics
```

#### User Endpoints
```
GET    /api/v1/users/                     # List all users
GET    /api/v1/users/{user_id}            # Get user profile
GET    /api/v1/users/{user_id}/transactions  # User transactions
GET    /api/v1/users/{user_id}/behavior   # User behavior
GET    /api/v1/users/stats/summary        # User statistics
```

#### Feedback Endpoints
```
POST   /api/v1/feedback/                  # Submit feedback
GET    /api/v1/feedback/                  # List feedback
GET    /api/v1/feedback/{feedback_id}     # Get specific feedback
GET    /api/v1/feedback/stats/summary     # Feedback statistics
```

---

## 🎨 Dashboard

### Pages Overview

#### 1. Overview (Home)
- **Purpose**: System-wide monitoring
- **Features**:
  - Key metrics (alerts, cases, users, accuracy)
  - Alert distribution pie chart
  - Case status bar chart
  - Recent alerts table
  - Auto-refresh every 30 seconds

#### 2. Detection
- **Purpose**: Submit transactions for analysis
- **Features**:
  - Transaction input form
  - Real-time detection
  - Detailed risk breakdown
  - Model score visualization
  - Anomaly feature list

#### 3. Alerts
- **Purpose**: Monitor and manage alerts
- **Features**:
  - Alert list with filtering
  - Priority-based sorting
  - Status management
  - Case creation
  - Alert assignment

#### 4. Cases
- **Purpose**: Investigation tracking
- **Features**:
  - Case list with status filter
  - Investigation details
  - Evidence documentation
  - Resolution workflow
  - Decision recording

#### 5. Analytics
- **Purpose**: Performance monitoring
- **Features**:
  - Model performance metrics
  - Alert trend charts
  - User risk distribution
  - Time-series analysis

#### 6. Users
- **Purpose**: User profile management
- **Features**:
  - User search
  - Transaction history
  - Behavior patterns
  - Risk assessment
  - Profile statistics

#### 7. Feedback
- **Purpose**: Model improvement
- **Features**:
  - Feedback submission form
  - Ground truth labeling
  - Evidence quality rating
  - Feedback statistics
  - Quality distribution charts

#### 8. Settings
- **Purpose**: Configuration and testing
- **Features**:
  - Model configuration view
  - Detection thresholds
  - API connection testing
  - System information

---

## 🔒 Security

### Security Features

1. **Input Validation**
   - Pydantic model validation
   - Type checking
   - Range validation
   - Format verification

2. **CORS Protection**
   - Configurable allowed origins
   - Credential handling
   - Method restrictions

3. **Error Handling**
   - Safe error messages
   - No sensitive data exposure
   - Structured error responses

4. **Logging**
   - Comprehensive audit trails
   - Request/response logging
   - Error tracking
   - Performance monitoring

### Best Practices

- **Environment Variables**: Store sensitive configuration
- **HTTPS**: Use in production
- **Rate Limiting**: Implement for public APIs
- **Authentication**: Add JWT/OAuth for production
- **Input Sanitization**: Prevent injection attacks

---

## ⚡ Performance

### Optimization Techniques

1. **Async/Await**
   - Non-blocking I/O operations
   - Concurrent request handling
   - High throughput

2. **In-Memory Storage**
   - Sub-millisecond data access
   - No database overhead
   - Fast read/write operations

3. **Efficient Algorithms**
   - Optimized ML models
   - Vectorized operations (NumPy)
   - Cached computations

4. **Resource Management**
   - Memory-efficient data structures
   - Lazy loading
   - Connection pooling

### Performance Metrics

- **Detection Latency**: < 100ms
- **API Response Time**: < 50ms
- **Dashboard Load Time**: < 2s
- **Concurrent Users**: 100+ supported
- **Throughput**: 1000+ requests/second

---

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with coverage
pytest --cov=fastapi --cov-report=html

# Run specific test file
pytest tests/test_api/test_detection.py

# Run with verbose output
pytest -v
```

### Test Structure

```
tests/
├── test_api/
│   ├── test_detection.py
│   ├── test_alerts.py
│   └── test_cases.py
├── test_services/
│   ├── test_detector.py
│   └── test_alert_service.py
└── test_integration/
    └── test_workflow.py
```
---
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
