"""
MarcenAI - Serviço de Integração com OpenAI
Gerencia chamadas para DALL-E para geração de imagens
"""

from openai import OpenAI
from typing import Optional
import base64
import io
from PIL import Image

from app.core.config import settings


class OpenAIService:
    """Serviço para geração de imagens com DALL-E"""

    def __init__(self):
        """Inicializa cliente OpenAI"""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
        self.size = settings.OPENAI_IMAGE_SIZE
        self.quality = settings.OPENAI_IMAGE_QUALITY

    async def generate_image(
        self,
        prompt: str,
        n: int = 1,
        size: Optional[str] = None,
        quality: Optional[str] = None
    ) -> list[dict]:
        """
        Gera imagem(ns) usando DALL-E

        Args:
            prompt: Prompt para geração
            n: Número de imagens (1-4)
            size: Tamanho (1024x1024, 1024x1792, 1792x1024)
            quality: Qualidade (standard ou hd)

        Returns:
            Lista de dicts com url e revised_prompt

        Raises:
            Exception: Se houver erro na API
        """
        try:
            # Usar configurações padrão se não fornecidas
            size = size or self.size
            quality = quality or self.quality

            # Validar número de imagens (DALL-E 3 aceita apenas 1)
            if self.model == "dall-e-3" and n > 1:
                n = 1

            print(f"🎨 Gerando imagem com DALL-E...")
            print(f"📝 Prompt: {prompt[:100]}...")

            # Chamar API OpenAI
            response = self.client.images.generate(
                model=self.model,
                prompt=prompt,
                n=n,
                size=size,
                quality=quality,
                response_format="url"  # ou "b64_json" para base64
            )

            results = []
            for image_data in response.data:
                results.append({
                    "url": image_data.url,
                    "revised_prompt": getattr(image_data, "revised_prompt", prompt)
                })

            print(f"✅ {len(results)} imagem(ns) gerada(s) com sucesso!")
            return results

        except Exception as e:
            print(f"❌ Erro ao gerar imagem: {str(e)}")
            raise Exception(f"Erro ao gerar imagem com OpenAI: {str(e)}")

    async def download_image(self, image_url: str) -> bytes:
        """
        Baixa imagem gerada pela API

        Args:
            image_url: URL da imagem

        Returns:
            Bytes da imagem

        Raises:
            Exception: Se houver erro no download
        """
        try:
            import httpx

            async with httpx.AsyncClient() as client:
                response = await client.get(image_url)
                response.raise_for_status()
                return response.content

        except Exception as e:
            print(f"❌ Erro ao baixar imagem: {str(e)}")
            raise Exception(f"Erro ao baixar imagem: {str(e)}")

    def validate_api_key(self) -> bool:
        """
        Valida se a API key está configurada corretamente

        Returns:
            True se válida, False caso contrário
        """
        if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY == "sk-your-key-here":
            return False

        try:
            # Tenta listar modelos para validar a key
            self.client.models.list()
            return True
        except Exception as e:
            print(f"⚠️ API Key inválida: {str(e)}")
            return False


# Instância global do serviço
openai_service = OpenAIService()
