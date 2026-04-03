"""
MarcenAI - Serviço de Armazenamento MinIO
Gerencia upload e download de imagens no MinIO (S3-compatible)
"""

from minio import Minio
from minio.error import S3Error
from typing import Optional
import io
from datetime import timedelta
import uuid

from app.core.config import settings


class MinIOService:
    """Serviço para gerenciamento de arquivos no MinIO"""

    def __init__(self):
        """Inicializa cliente MinIO"""
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE
        )
        self.bucket = settings.MINIO_BUCKET

        # Garantir que o bucket existe
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        """Cria bucket se não existir"""
        try:
            if not self.client.bucket_exists(self.bucket):
                self.client.make_bucket(self.bucket)
                print(f"✅ Bucket '{self.bucket}' criado no MinIO")

                # Definir política pública para leitura
                policy = f'''{{
                    "Version": "2012-10-17",
                    "Statement": [
                        {{
                            "Effect": "Allow",
                            "Principal": {{"AWS": ["*"]}},
                            "Action": ["s3:GetObject"],
                            "Resource": ["arn:aws:s3:::{self.bucket}/*"]
                        }}
                    ]
                }}'''
                self.client.set_bucket_policy(self.bucket, policy)
                print(f"✅ Política pública configurada para o bucket")
        except S3Error as e:
            print(f"⚠️ Erro ao verificar/criar bucket: {e}")

    async def upload_image(
        self,
        image_data: bytes,
        filename: Optional[str] = None,
        content_type: str = "image/png"
    ) -> tuple[str, str]:
        """
        Faz upload de imagem para o MinIO

        Args:
            image_data: Bytes da imagem
            filename: Nome do arquivo (gera UUID se não fornecido)
            content_type: Tipo MIME da imagem

        Returns:
            Tupla (object_name, public_url)

        Raises:
            Exception: Se houver erro no upload
        """
        try:
            # Gerar nome único se não fornecido
            if not filename:
                extension = content_type.split("/")[-1]
                filename = f"{uuid.uuid4()}.{extension}"

            # Garantir que o filename tenha um caminho organizado
            object_name = f"projects/{filename}"

            # Converter bytes para stream
            image_stream = io.BytesIO(image_data)
            image_size = len(image_data)

            # Upload para MinIO
            self.client.put_object(
                bucket_name=self.bucket,
                object_name=object_name,
                data=image_stream,
                length=image_size,
                content_type=content_type
            )

            # Construir URL pública
            public_url = self.get_public_url(object_name)

            print(f"✅ Imagem enviada para MinIO: {object_name}")
            return object_name, public_url

        except S3Error as e:
            print(f"❌ Erro ao fazer upload para MinIO: {str(e)}")
            raise Exception(f"Erro ao fazer upload: {str(e)}")

    def get_public_url(self, object_name: str) -> str:
        """
        Retorna URL pública de um objeto

        Args:
            object_name: Nome do objeto no bucket

        Returns:
            URL pública completa
        """
        # URL pública do MinIO
        base_url = settings.minio_public_url
        return f"{base_url}/{self.bucket}/{object_name}"

    def get_presigned_url(
        self,
        object_name: str,
        expires: timedelta = timedelta(hours=24)
    ) -> str:
        """
        Gera URL pré-assinada temporária

        Args:
            object_name: Nome do objeto
            expires: Tempo de expiração

        Returns:
            URL pré-assinada
        """
        try:
            url = self.client.presigned_get_object(
                bucket_name=self.bucket,
                object_name=object_name,
                expires=expires
            )
            return url
        except S3Error as e:
            print(f"❌ Erro ao gerar URL pré-assinada: {str(e)}")
            raise Exception(f"Erro ao gerar URL: {str(e)}")

    async def delete_image(self, object_name: str) -> bool:
        """
        Deleta imagem do MinIO

        Args:
            object_name: Nome do objeto

        Returns:
            True se deletado com sucesso
        """
        try:
            self.client.remove_object(
                bucket_name=self.bucket,
                object_name=object_name
            )
            print(f"🗑️ Imagem deletada: {object_name}")
            return True
        except S3Error as e:
            print(f"❌ Erro ao deletar imagem: {str(e)}")
            return False

    def list_images(self, prefix: str = "projects/") -> list[str]:
        """
        Lista todas as imagens com determinado prefixo

        Args:
            prefix: Prefixo para filtrar objetos

        Returns:
            Lista de nomes de objetos
        """
        try:
            objects = self.client.list_objects(
                bucket_name=self.bucket,
                prefix=prefix,
                recursive=True
            )
            return [obj.object_name for obj in objects]
        except S3Error as e:
            print(f"❌ Erro ao listar imagens: {str(e)}")
            return []


# Instância global do serviço
minio_service = MinIOService()
