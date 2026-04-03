"""
MarcenAI - Rotas de Projetos
Endpoints principais para gestão de projetos de marcenaria
"""

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.core.database import get_db
from app.models.project import Project, ProjectImage
from app.models.schemas import (
    ProjectCreateRequest,
    ProjectResponse,
    ProjectListResponse,
    ImageRefinementRequest
)
from app.services.prompt_generator import prompt_generator
from app.services.openai_service import openai_service
from app.services.minio_service import minio_service

router = APIRouter()


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    request: ProjectCreateRequest,
    db: Session = Depends(get_db)
):
    """
    Cria novo projeto de marcenaria e gera imagem com IA

    Este é o endpoint PRINCIPAL do sistema!
    1. Recebe informações simples do marceneiro
    2. Gera prompt otimizado automaticamente
    3. Chama DALL-E para criar a imagem
    4. Salva tudo no banco e MinIO
    5. Retorna projeto completo com imagem
    """
    try:
        print("\n🪵 === CRIANDO NOVO PROJETO ===")

        # 1. Gerar prompt otimizado
        print("📝 Gerando prompt otimizado...")
        generated_prompt = prompt_generator.generate_prompt(
            furniture_type=request.furniture_type,
            room=request.room,
            style=request.style,
            size=request.size,
            dimensions=request.dimensions,
            width_cm=request.width_cm,
            height_cm=request.height_cm,
            depth_cm=request.depth_cm,
            material=request.material,
            color=request.color,
            special_features=request.special_features
        )
        print(f"✅ Prompt gerado: {generated_prompt[:100]}...")

        # 2. Criar registro do projeto no banco
        project = Project(
            id=str(uuid.uuid4()),
            furniture_type=request.furniture_type,
            room=request.room,
            style=request.style,
            size=request.size,
            dimensions=request.dimensions,
            width_cm=request.width_cm,
            height_cm=request.height_cm,
            depth_cm=request.depth_cm,
            material=request.material,
            color=request.color,
            special_features=request.special_features,
            reference_image_url=request.reference_image_url,
            client_name=request.client_name,
            client_notes=request.client_notes,
            generated_prompt=generated_prompt
        )
        db.add(project)
        db.commit()
        db.refresh(project)
        print(f"✅ Projeto criado no banco: {project.id}")

        # 3. Gerar imagem com DALL-E
        print("🎨 Chamando DALL-E para gerar imagem...")
        image_results = await openai_service.generate_image(
            prompt=generated_prompt,
            n=1  # DALL-E 3 gera apenas 1 imagem por vez
        )

        # 4. Baixar e salvar imagem no MinIO
        for idx, image_result in enumerate(image_results):
            print(f"📥 Baixando imagem {idx + 1}...")
            image_bytes = await openai_service.download_image(image_result["url"])

            print(f"☁️ Fazendo upload para MinIO...")
            filename = f"{project.id}_{idx}.png"
            object_name, public_url = await minio_service.upload_image(
                image_data=image_bytes,
                filename=filename,
                content_type="image/png"
            )

            # 5. Criar registro da imagem no banco
            project_image = ProjectImage(
                id=str(uuid.uuid4()),
                project_id=project.id,
                image_url=public_url,
                minio_object_name=object_name,
                width=1024,
                height=1024,
                format="png",
                file_size=len(image_bytes),
                prompt_used=generated_prompt,
                is_selected=1 if idx == 0 else 0  # Primeira é selecionada por padrão
            )
            db.add(project_image)

        db.commit()
        db.refresh(project)

        print("✅ === PROJETO CRIADO COM SUCESSO ===\n")

        # 6. Retornar projeto completo
        return ProjectResponse.from_orm(project)

    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao criar projeto: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar projeto: {str(e)}"
        )


@router.get("/", response_model=List[ProjectListResponse])
async def list_projects(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """
    Lista todos os projetos (paginado)

    Query params:
    - skip: Número de registros para pular (padrão: 0)
    - limit: Número máximo de registros (padrão: 50)
    """
    try:
        projects = db.query(Project).offset(skip).limit(limit).all()

        # Converter para response com thumbnail
        results = []
        for project in projects:
            thumbnail_url = None
            if project.images:
                # Pegar primeira imagem como thumbnail
                thumbnail_url = project.images[0].image_url

            results.append(ProjectListResponse(
                id=project.id,
                furniture_type=project.furniture_type.value,
                room=project.room.value,
                style=project.style.value,
                client_name=project.client_name,
                created_at=project.created_at,
                images_count=len(project.images),
                thumbnail_url=thumbnail_url
            ))

        return results

    except Exception as e:
        print(f"❌ Erro ao listar projetos: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao listar projetos: {str(e)}"
        )


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str, db: Session = Depends(get_db)):
    """
    Busca projeto específico por ID

    Retorna projeto completo com todas as imagens
    """
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Projeto {project_id} não encontrado"
        )

    return ProjectResponse.from_orm(project)


@router.post("/{project_id}/refine", response_model=ProjectResponse)
async def refine_project_image(
    project_id: str,
    request: ImageRefinementRequest,
    db: Session = Depends(get_db)
):
    """
    Refina/ajusta imagem de um projeto existente

    O marceneiro pode pedir ajustes como:
    - "adicionar mais gavetas"
    - "mudar cor para branco"
    - "tornar mais rústico"

    Gera nova imagem baseada no refinamento
    """
    try:
        print(f"\n🔄 === REFINANDO PROJETO {project_id} ===")

        # Buscar projeto
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Projeto {project_id} não encontrado"
            )

        # Refinar prompt
        print(f"📝 Refinando prompt com: {request.refinement_notes}")
        refined_prompt = prompt_generator.refine_prompt(
            original_prompt=project.generated_prompt,
            refinement_notes=request.refinement_notes
        )
        print(f"✅ Novo prompt: {refined_prompt[:100]}...")

        # Gerar nova imagem
        print("🎨 Gerando nova imagem refinada...")
        image_results = await openai_service.generate_image(
            prompt=refined_prompt,
            n=1
        )

        # Baixar e salvar
        for idx, image_result in enumerate(image_results):
            image_bytes = await openai_service.download_image(image_result["url"])

            # Número de refinamentos já existentes
            refinement_count = len([img for img in project.images if img.is_refined > 0]) + 1

            filename = f"{project.id}_refined_{refinement_count}.png"
            object_name, public_url = await minio_service.upload_image(
                image_data=image_bytes,
                filename=filename,
                content_type="image/png"
            )

            # Criar nova imagem refinada
            project_image = ProjectImage(
                id=str(uuid.uuid4()),
                project_id=project.id,
                image_url=public_url,
                minio_object_name=object_name,
                width=1024,
                height=1024,
                format="png",
                file_size=len(image_bytes),
                prompt_used=refined_prompt,
                refinement_notes=request.refinement_notes,
                is_refined=refinement_count,
                is_selected=1  # Nova imagem vira a selecionada
            )

            # Desmarcar imagens antigas como selecionadas
            for img in project.images:
                img.is_selected = 0

            db.add(project_image)

        db.commit()
        db.refresh(project)

        print("✅ === REFINAMENTO CONCLUÍDO ===\n")
        return ProjectResponse.from_orm(project)

    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao refinar projeto: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao refinar projeto: {str(e)}"
        )


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: str, db: Session = Depends(get_db)):
    """
    Deleta projeto e todas as suas imagens

    Remove:
    - Registro do banco de dados
    - Imagens do MinIO
    """
    try:
        project = db.query(Project).filter(Project.id == project_id).first()

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Projeto {project_id} não encontrado"
            )

        # Deletar imagens do MinIO
        for image in project.images:
            await minio_service.delete_image(image.minio_object_name)

        # Deletar do banco (cascade vai deletar as imagens)
        db.delete(project)
        db.commit()

        print(f"🗑️ Projeto {project_id} deletado com sucesso")
        return None

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao deletar projeto: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar projeto: {str(e)}"
        )


@router.patch("/{project_id}/images/{image_id}/select")
async def select_image(
    project_id: str,
    image_id: str,
    db: Session = Depends(get_db)
):
    """
    Marca uma imagem como selecionada/favorita

    Útil quando há várias opções e o cliente escolhe uma
    """
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")

        image = db.query(ProjectImage).filter(
            ProjectImage.id == image_id,
            ProjectImage.project_id == project_id
        ).first()

        if not image:
            raise HTTPException(status_code=404, detail="Imagem não encontrada")

        # Desmarcar todas as outras
        for img in project.images:
            img.is_selected = 0

        # Marcar esta como selecionada
        image.is_selected = 1
        db.commit()

        return {"message": "Imagem selecionada com sucesso", "image_id": image_id}

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload-reference", status_code=status.HTTP_200_OK)
async def upload_reference_image(
    file: UploadFile = File(...)
):
    """
    Faz upload de imagem de referência

    Esta imagem será usada pelo marceneiro como exemplo/inspiração
    para a geração do móvel planejado.

    Returns:
        URL pública da imagem de referência no MinIO
    """
    try:
        print(f"\n📸 === UPLOAD DE IMAGEM DE REFERÊNCIA ===")
        print(f"📄 Arquivo: {file.filename}")
        print(f"📋 Content-Type: {file.content_type}")

        # Validar tipo de arquivo
        allowed_types = ["image/jpeg", "image/jpg", "image/png", "image/webp"]
        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Tipo de arquivo não suportado. Use: {', '.join(allowed_types)}"
            )

        # Ler bytes da imagem
        image_bytes = await file.read()
        file_size = len(image_bytes)

        # Validar tamanho (máximo 10MB)
        max_size = 10 * 1024 * 1024  # 10MB
        if file_size > max_size:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Arquivo muito grande. Máximo: 10MB. Tamanho: {file_size / 1024 / 1024:.2f}MB"
            )

        print(f"📊 Tamanho: {file_size / 1024:.2f} KB")

        # Gerar nome único para o arquivo
        file_extension = file.filename.split(".")[-1] if "." in file.filename else "jpg"
        filename = f"reference_{uuid.uuid4()}.{file_extension}"

        # Upload para MinIO
        print(f"☁️ Fazendo upload para MinIO...")
        object_name, public_url = await minio_service.upload_image(
            image_data=image_bytes,
            filename=filename,
            content_type=file.content_type
        )

        print(f"✅ Upload concluído!")
        print(f"📎 URL: {public_url}\n")

        return {
            "success": True,
            "reference_image_url": public_url,
            "object_name": object_name,
            "filename": filename,
            "file_size": file_size
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Erro ao fazer upload: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao fazer upload da imagem: {str(e)}"
        )
