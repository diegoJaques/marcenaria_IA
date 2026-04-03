"""
MarcenAI - Rotas de Health Check
Endpoints para verificar saúde da aplicação e dependências
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.core.config import settings
from app.models.schemas import HealthResponse
from app.services.openai_service import openai_service
from app.services.minio_service import minio_service

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check(db: Session = Depends(get_db)):
    """
    Verifica saúde da aplicação e dependências

    Retorna status de:
    - API
    - Banco de dados
    - MinIO
    - OpenAI API
    """
    status_details = {
        "api": "ok",
        "database": "checking",
        "minio": "checking",
        "openai": "checking"
    }

    # Testar banco de dados
    try:
        db.execute("SELECT 1")
        status_details["database"] = "ok"
    except Exception as e:
        status_details["database"] = f"error: {str(e)}"

    # Testar MinIO
    try:
        minio_service.client.bucket_exists(minio_service.bucket)
        status_details["minio"] = "ok"
    except Exception as e:
        status_details["minio"] = f"error: {str(e)}"

    # Testar OpenAI (opcional - não falha o health check)
    try:
        if openai_service.validate_api_key():
            status_details["openai"] = "ok"
        else:
            status_details["openai"] = "warning: api key not configured"
    except Exception as e:
        status_details["openai"] = f"warning: {str(e)}"

    # Status geral
    overall_status = "healthy"
    if "error" in str(status_details):
        overall_status = "unhealthy"
    elif "warning" in str(status_details):
        overall_status = "degraded"

    return HealthResponse(
        status=overall_status,
        message=f"MarcenAI API - {overall_status}",
        version=settings.VERSION,
        timestamp=datetime.now()
    )


@router.get("/ping")
async def ping():
    """Endpoint simples de ping"""
    return {"message": "pong", "timestamp": datetime.now()}
