"""
MarcenAI - API Principal
Sistema de geração de imagens de projetos de marcenaria com IA

Projeto de Extensão II - Análise e Desenvolvimento de Sistemas
Aluno: Diego Jaques Tinoco
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import engine, Base
from app.routes import projects, health

# Lifespan para inicialização e finalização
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação"""
    # Startup
    print("🚀 Iniciando MarcenAI...")

    # Criar tabelas do banco de dados
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas do banco de dados criadas/verificadas")

    yield

    # Shutdown
    print("🛑 Encerrando MarcenAI...")

# Criar aplicação FastAPI
app = FastAPI(
    title="MarcenAI API",
    description="Sistema de geração de projetos de marcenaria com IA",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(health.router, tags=["Health"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])

# Rota raiz
@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "🪵 MarcenAI API está funcionando!",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "operational"
    }

# Handler global de erros
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handler global para exceções não tratadas"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Erro interno do servidor",
            "detail": str(exc) if settings.DEBUG else "Entre em contato com o suporte",
            "type": type(exc).__name__
        }
    )
