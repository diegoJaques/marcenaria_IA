"""
MarcenAI - Configurações da Aplicação
Gerencia todas as variáveis de ambiente e configurações
"""

from pydantic_settings import BaseSettings
from typing import List, Union
import os


class Settings(BaseSettings):
    """Configurações da aplicação"""

    # App
    APP_ENV: str = "development"
    DEBUG: bool = True
    APP_NAME: str = "MarcenAI"
    VERSION: str = "1.0.0"

    # Database
    DATABASE_URL: str = "postgresql://marcenai:marcenai123@localhost:5432/marcenai_db"

    # MinIO/S3
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin123"
    MINIO_BUCKET: str = "project-images"
    MINIO_SECURE: bool = False

    # OpenAI
    OPENAI_API_KEY: str = "sk-your-key-here"
    OPENAI_MODEL: str = "dall-e-3"
    OPENAI_IMAGE_SIZE: str = "1024x1024"
    OPENAI_IMAGE_QUALITY: str = "standard"  # standard ou hd

    # CORS - aceita string ou lista
    CORS_ORIGINS: Union[str, List[str]] = "http://localhost:3000,http://localhost:5173"

    # Upload
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def cors_origins_list(self) -> List[str]:
        """Converte CORS_ORIGINS para lista"""
        if isinstance(self.CORS_ORIGINS, str):
            return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
        return self.CORS_ORIGINS

    @property
    def is_development(self) -> bool:
        """Verifica se está em ambiente de desenvolvimento"""
        return self.APP_ENV == "development"

    @property
    def minio_public_url(self) -> str:
        """URL pública do MinIO para acesso externo (navegador)"""
        protocol = "https" if self.MINIO_SECURE else "http"
        # Se o endpoint é interno do Docker (minio:9000), usar localhost
        if self.MINIO_ENDPOINT == "minio:9000":
            return f"{protocol}://localhost:9000"
        return f"{protocol}://{self.MINIO_ENDPOINT}"


# Instância global de configurações
settings = Settings()
