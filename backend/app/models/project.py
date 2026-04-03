"""
MarcenAI - Modelos de Projeto
Define a estrutura de dados para projetos de marcenaria
"""

from sqlalchemy import Column, String, Text, DateTime, Enum, Integer, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum
import uuid

from app.core.database import Base


# Enums para categorização (SUPER SIMPLES para o marceneiro)
class FurnitureType(str, enum.Enum):
    """Tipos de móveis - Linguagem simples"""
    CADEIRA = "cadeira"  # 🪑
    SOFA = "sofa"  # 🛋️
    ARMARIO = "armario"  # 🚪
    ESTANTE = "estante"  # 📚
    MESA = "mesa"  # 🍽️
    BANCADA = "bancada"  # 🔨
    CAMA = "cama"  # 🛏️
    CRIADO = "criado"  # 📦
    OUTRO = "outro"  # 💡


class FurnitureStyle(str, enum.Enum):
    """Estilos - Linguagem simples e visual"""
    MODERNO = "moderno"  # Limpo, minimalista
    RUSTICO = "rustico"  # Madeira natural, artesanal
    INDUSTRIAL = "industrial"  # Metal e madeira
    CLASSICO = "classico"  # Tradicional, elegante
    CONTEMPORANEO = "contemporaneo"  # Atual, sofisticado
    PROVENCAL = "provencal"  # Romântico, vintage


class Room(str, enum.Enum):
    """Ambientes da casa - Todo mundo conhece"""
    COZINHA = "cozinha"  # 🍳
    SALA = "sala"  # 🛋️
    QUARTO = "quarto"  # 🛏️
    BANHEIRO = "banheiro"  # 🚿
    ESCRITORIO = "escritorio"  # 💼
    AREA_EXTERNA = "area_externa"  # 🌳
    LAVANDERIA = "lavanderia"  # 🧺
    GARAGEM = "garagem"  # 🚗


class Project(Base):
    """
    Modelo principal de Projeto
    Armazena todas as informações de um projeto de móvel
    """
    __tablename__ = "projects"

    # Identificação
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # Informações básicas (respostas do questionário)
    furniture_type = Column(Enum(FurnitureType), nullable=False)
    room = Column(Enum(Room), nullable=False)
    style = Column(Enum(FurnitureStyle), nullable=False)

    # Detalhes
    size = Column(String(50))  # "pequeno", "médio", "grande"
    dimensions = Column(String(200))  # Ex: "180cm x 90cm x 45cm" (opcional, texto livre)

    # Dimensões específicas (NOVO - para móveis planejados sob medida)
    width_cm = Column(Float)  # Largura em centímetros
    height_cm = Column(Float)  # Altura em centímetros
    depth_cm = Column(Float)  # Profundidade em centímetros

    material = Column(String(100))  # Ex: "madeira de lei", "MDF", "pinus"
    color = Column(String(100))  # Ex: "natural", "branco", "preto"
    special_features = Column(Text)  # Ex: "3 gavetas, portas de vidro"

    # Imagem de referência (NOVO - para o marceneiro enviar foto de exemplo)
    reference_image_url = Column(String(500))  # URL da imagem de referência no MinIO
    reference_image_object = Column(String(200))  # Nome do objeto no bucket

    # Cliente (opcional)
    client_name = Column(String(200))
    client_notes = Column(Text)  # Observações do cliente

    # Prompt gerado automaticamente (invisível para o usuário)
    generated_prompt = Column(Text, nullable=False)

    # Metadados
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relacionamento com imagens
    images = relationship("ProjectImage", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project {self.id} - {self.furniture_type} para {self.room}>"


class ProjectImage(Base):
    """
    Modelo de Imagem do Projeto
    Armazena as imagens geradas pela IA
    """
    __tablename__ = "project_images"

    # Identificação
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String(36), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)

    # Armazenamento
    image_url = Column(String(500), nullable=False)  # URL no MinIO
    minio_object_name = Column(String(200), nullable=False)  # Nome do arquivo no bucket

    # Metadados da imagem
    width = Column(Integer, default=1024)
    height = Column(Integer, default=1024)
    format = Column(String(10), default="png")
    file_size = Column(Integer)  # Tamanho em bytes

    # Prompt usado para gerar esta imagem específica (pode variar se houve refinamento)
    prompt_used = Column(Text, nullable=False)

    # Refinamento (se usuário pediu ajustes)
    refinement_notes = Column(Text)  # Ex: "adicionar gavetas", "mudar cor para branco"
    is_refined = Column(Integer, default=0)  # 0 = original, 1+ = número de refinamentos

    # Favorita/Escolhida
    is_selected = Column(Integer, default=0)  # 1 se foi a escolhida pelo cliente

    # Metadados
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamento
    project = relationship("Project", back_populates="images")

    def __repr__(self):
        return f"<ProjectImage {self.id} - Project {self.project_id}>"
