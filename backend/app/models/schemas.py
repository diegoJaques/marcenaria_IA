"""
MarcenAI - Schemas Pydantic
Validação e serialização de dados da API
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.project import FurnitureType, FurnitureStyle, Room


# ============== REQUEST SCHEMAS (Entrada) ==============

class ProjectCreateRequest(BaseModel):
    """
    Schema para criação de projeto
    Campos em linguagem SIMPLES para o marceneiro preencher
    """
    # Perguntas básicas
    furniture_type: FurnitureType = Field(..., description="Que tipo de móvel?")
    room: Room = Field(..., description="Para qual ambiente?")
    style: FurnitureStyle = Field(..., description="Qual o estilo?")

    # Detalhes (opcionais)
    size: Optional[str] = Field(None, description="Tamanho: pequeno, médio ou grande")
    dimensions: Optional[str] = Field(None, description="Medidas específicas (ex: 180x90x45cm)")

    # Dimensões específicas para móveis planejados sob medida
    width_cm: Optional[float] = Field(None, description="Largura em centímetros", gt=0, le=1000)
    height_cm: Optional[float] = Field(None, description="Altura em centímetros", gt=0, le=1000)
    depth_cm: Optional[float] = Field(None, description="Profundidade em centímetros", gt=0, le=1000)

    material: Optional[str] = Field(None, description="Material preferido")
    color: Optional[str] = Field(None, description="Cor desejada")
    special_features: Optional[str] = Field(None, description="Características especiais")

    # Imagem de referência (URL será preenchida após upload)
    reference_image_url: Optional[str] = Field(None, description="URL da imagem de referência")

    # Cliente (opcional)
    client_name: Optional[str] = Field(None, description="Nome do cliente")
    client_notes: Optional[str] = Field(None, description="Observações do cliente")

    class Config:
        json_schema_extra = {
            "example": {
                "furniture_type": "armario",
                "room": "cozinha",
                "style": "moderno",
                "size": "grande",
                "dimensions": "180cm x 90cm x 45cm",
                "width_cm": 180.0,
                "height_cm": 220.0,
                "depth_cm": 45.0,
                "material": "MDF branco",
                "color": "branco com detalhes em preto",
                "special_features": "3 gavetas, 2 portas com vidro, puxadores pretos",
                "reference_image_url": "http://localhost:9000/project-images/reference_abc123.jpg",
                "client_name": "João da Silva",
                "client_notes": "Cliente quer aproveitar bem o espaço"
            }
        }


class ImageRefinementRequest(BaseModel):
    """Schema para refinar uma imagem existente"""
    refinement_notes: str = Field(..., description="O que mudar? (ex: 'adicionar gavetas', 'mudar cor para branco')")

    class Config:
        json_schema_extra = {
            "example": {
                "refinement_notes": "adicionar mais gavetas e mudar a cor para tom de madeira natural"
            }
        }


# ============== RESPONSE SCHEMAS (Saída) ==============

class ProjectImageResponse(BaseModel):
    """Schema de resposta para imagem de projeto"""
    id: str
    image_url: str
    prompt_used: str
    width: int
    height: int
    is_selected: bool
    refinement_notes: Optional[str] = None
    is_refined: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProjectResponse(BaseModel):
    """Schema de resposta para projeto completo"""
    id: str
    furniture_type: str
    room: str
    style: str
    size: Optional[str] = None
    dimensions: Optional[str] = None
    width_cm: Optional[float] = None
    height_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    material: Optional[str] = None
    color: Optional[str] = None
    special_features: Optional[str] = None
    reference_image_url: Optional[str] = None
    client_name: Optional[str] = None
    client_notes: Optional[str] = None
    generated_prompt: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    images: List[ProjectImageResponse] = []

    class Config:
        from_attributes = True


class ProjectListResponse(BaseModel):
    """Schema de resposta para lista de projetos (simplificado)"""
    id: str
    furniture_type: str
    room: str
    style: str
    client_name: Optional[str] = None
    created_at: datetime
    images_count: int = 0
    thumbnail_url: Optional[str] = None  # URL da primeira imagem

    class Config:
        from_attributes = True


# ============== UTILITY SCHEMAS ==============

class HealthResponse(BaseModel):
    """Schema de resposta para health check"""
    status: str
    message: str
    version: str
    timestamp: datetime


class ErrorResponse(BaseModel):
    """Schema padrão de erro"""
    error: str
    detail: Optional[str] = None
    type: Optional[str] = None
