# FastAPI main application - To be implemented
"""
FastAPI Main Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .core.logging import setup_logging, logger
from .api import detection, alerts, cases, feedback, metrics, users

# Setup logging
setup_logging()

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="Real-time fraud detection and alert management",
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

# Include routers
app.include_router(detection.router)
app.include_router(alerts.router)
app.include_router(cases.router)
app.include_router(feedback.router)
app.include_router(metrics.router)
app.include_router(users.router)


@app.get("/", tags=["Root"])
async def root():
    """API root endpoint"""
    return {
        "service": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "operational",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    from .services.alert_service import alerts as alert_storage
    from .services.case_service import cases as case_storage
    
    return {
        "status": "healthy",
        "statistics": {
            "total_alerts": len(alert_storage),
            "total_cases": len(case_storage)
        }
    }


@app.on_event("startup")
async def startup_event():
    """Startup event"""
    logger.info("=" * 80)
    logger.info(f"{settings.APP_NAME} v{settings.VERSION}")
    logger.info("=" * 80)
    logger.info("Server ready!")
    logger.info(f"API Documentation: http://localhost:{settings.PORT}/docs")
    logger.info("=" * 80)


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    logger.info("Shutting down gracefully...")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT
    )