"""
MarcenAI - Gerador de Prompts Inteligente
Converte respostas simples do marceneiro em prompts otimizados para IA

Este é o "cérebro" do sistema - transforma inputs simples em prompts detalhados
"""

from typing import Dict, Optional
from app.models.project import FurnitureType, FurnitureStyle, Room


class PromptGenerator:
    """
    Gerador inteligente de prompts para DALL-E
    Converte informações simples em descrições fotorrealísticas detalhadas
    """

    # Traduções e contextos para cada tipo de móvel
    FURNITURE_CONTEXTS = {
        FurnitureType.CADEIRA: {
            "en": "chair",
            "details": "with ergonomic design, comfortable seating",
            "typical_materials": "wood, upholstered seat"
        },
        FurnitureType.SOFA: {
            "en": "sofa",
            "details": "with comfortable cushions, elegant proportions",
            "typical_materials": "upholstered fabric, wooden frame"
        },
        FurnitureType.ARMARIO: {
            "en": "cabinet",
            "details": "with organized storage, quality hardware",
            "typical_materials": "solid wood or MDF"
        },
        FurnitureType.ESTANTE: {
            "en": "bookshelf",
            "details": "with multiple shelves, sturdy construction",
            "typical_materials": "wood or MDF with modern finish"
        },
        FurnitureType.MESA: {
            "en": "table",
            "details": "with smooth surface, stable structure",
            "typical_materials": "solid wood or MDF top"
        },
        FurnitureType.BANCADA: {
            "en": "workbench",
            "details": "with resistant surface, functional design",
            "typical_materials": "durable wood or composite"
        },
        FurnitureType.CAMA: {
            "en": "bed frame",
            "details": "with headboard, sturdy construction",
            "typical_materials": "solid wood"
        },
        FurnitureType.CRIADO: {
            "en": "nightstand",
            "details": "with drawers, compact design",
            "typical_materials": "wood or MDF"
        },
        FurnitureType.OUTRO: {
            "en": "custom furniture piece",
            "details": "with artisanal craftsmanship",
            "typical_materials": "quality materials"
        }
    }

    # Contextos de estilo
    STYLE_CONTEXTS = {
        FurnitureStyle.MODERNO: {
            "en": "modern minimalist",
            "description": "clean lines, simple forms, neutral colors",
            "finishing": "matte finish, metal accents"
        },
        FurnitureStyle.RUSTICO: {
            "en": "rustic artisanal",
            "description": "natural wood grain, handcrafted details, warm tones",
            "finishing": "natural wood finish, visible texture"
        },
        FurnitureStyle.INDUSTRIAL: {
            "en": "industrial",
            "description": "metal and wood combination, raw aesthetics",
            "finishing": "exposed hardware, dark metal elements"
        },
        FurnitureStyle.CLASSICO: {
            "en": "classic traditional",
            "description": "elegant details, refined proportions, timeless design",
            "finishing": "polished finish, decorative elements"
        },
        FurnitureStyle.CONTEMPORANEO: {
            "en": "contemporary",
            "description": "current trends, sophisticated design, balanced aesthetics",
            "finishing": "high-quality finish, modern details"
        },
        FurnitureStyle.PROVENCAL: {
            "en": "french provincial",
            "description": "romantic details, vintage charm, soft colors",
            "finishing": "distressed paint, decorative hardware"
        }
    }

    # Contextos de ambiente
    ROOM_CONTEXTS = {
        Room.COZINHA: "kitchen environment, clean and functional",
        Room.SALA: "living room setting, comfortable and inviting",
        Room.QUARTO: "bedroom setting, relaxing atmosphere",
        Room.BANHEIRO: "bathroom environment, moisture-resistant",
        Room.ESCRITORIO: "office environment, professional setting",
        Room.AREA_EXTERNA: "outdoor setting, weather-resistant",
        Room.LAVANDERIA: "laundry room, practical environment",
        Room.GARAGEM: "garage setting, durable construction"
    }

    def generate_prompt(
        self,
        furniture_type: FurnitureType,
        room: Room,
        style: FurnitureStyle,
        size: Optional[str] = None,
        dimensions: Optional[str] = None,
        width_cm: Optional[float] = None,
        height_cm: Optional[float] = None,
        depth_cm: Optional[float] = None,
        material: Optional[str] = None,
        color: Optional[str] = None,
        special_features: Optional[str] = None
    ) -> str:
        """
        Gera prompt otimizado para DALL-E baseado nos inputs do usuário

        Args:
            furniture_type: Tipo de móvel
            room: Ambiente
            style: Estilo
            size: Tamanho (pequeno/médio/grande)
            dimensions: Dimensões em texto livre
            width_cm: Largura em centímetros (móveis planejados)
            height_cm: Altura em centímetros (móveis planejados)
            depth_cm: Profundidade em centímetros (móveis planejados)
            material: Material
            color: Cor
            special_features: Características especiais

        Returns:
            Prompt otimizado em inglês para DALL-E
        """

        # Obter contextos
        furniture_ctx = self.FURNITURE_CONTEXTS.get(furniture_type, {})
        style_ctx = self.STYLE_CONTEXTS.get(style, {})
        room_ctx = self.ROOM_CONTEXTS.get(room, "")

        # Construir prompt parte por parte
        prompt_parts = []

        # Início: Fotorrealismo e qualidade
        prompt_parts.append("A photorealistic 3D rendering of a")

        # Estilo + Tipo de móvel
        style_name = style_ctx.get("en", style.value)
        furniture_name = furniture_ctx.get("en", furniture_type.value)
        prompt_parts.append(f"{style_name} {furniture_name}")

        # Material
        if material:
            prompt_parts.append(f"made of {material}")
        else:
            default_material = furniture_ctx.get("typical_materials", "quality wood")
            prompt_parts.append(f"made of {default_material}")

        # Cor
        if color:
            prompt_parts.append(f"in {color} color")

        # Características especiais
        if special_features:
            prompt_parts.append(f"featuring {special_features}")
        else:
            default_details = furniture_ctx.get("details", "")
            if default_details:
                prompt_parts.append(default_details)

        # Detalhes do estilo
        style_description = style_ctx.get("description", "")
        if style_description:
            prompt_parts.append(f"with {style_description}")

        # Dimensões/Tamanho (PRIORIDADE para móveis planejados sob medida)
        has_specific_dimensions = width_cm or height_cm or depth_cm

        if has_specific_dimensions:
            # Móvel planejado sob medida - adicionar contexto profissional
            dim_parts = []
            if width_cm:
                dim_parts.append(f"{width_cm:.0f}cm wide")
            if height_cm:
                dim_parts.append(f"{height_cm:.0f}cm high")
            if depth_cm:
                dim_parts.append(f"{depth_cm:.0f}cm deep")

            dimensions_text = " x ".join(dim_parts)
            prompt_parts.append(f"custom-made furniture with precise dimensions: {dimensions_text}")
            prompt_parts.append("tailored measurements for perfect fit")
            prompt_parts.append("professional carpentry work")

        elif dimensions:
            # Dimensões em texto livre
            prompt_parts.append(f"custom dimensions approximately {dimensions}")
            prompt_parts.append("made-to-measure furniture")

        elif size:
            # Tamanho genérico (pequeno/médio/grande)
            size_context = {
                "pequeno": "compact size, space-saving design",
                "médio": "medium size, balanced proportions",
                "grande": "large size, spacious design"
            }
            size_desc = size_context.get(size.lower(), "")
            if size_desc:
                prompt_parts.append(size_desc)

        # Finishing (acabamento baseado no estilo)
        finishing = style_ctx.get("finishing", "")
        if finishing:
            prompt_parts.append(finishing)

        # Contexto do ambiente
        if room_ctx:
            prompt_parts.append(f"designed for {room_ctx}")

        # Qualidade de renderização
        prompt_parts.append("professional furniture photography")
        prompt_parts.append("studio lighting")
        prompt_parts.append("high detail wood grain texture")
        prompt_parts.append("interior design magazine quality")
        prompt_parts.append("4K resolution")

        # Juntar tudo com vírgulas e pontos adequados
        prompt = ", ".join(prompt_parts) + "."

        return prompt

    def refine_prompt(self, original_prompt: str, refinement_notes: str) -> str:
        """
        Refina um prompt existente com base em notas de ajuste

        Args:
            original_prompt: Prompt original
            refinement_notes: O que mudar (em português)

        Returns:
            Prompt refinado
        """

        # Traduções comuns de ajustes
        refinement_translations = {
            "mais claro": "lighter tone",
            "mais escuro": "darker tone",
            "maior": "larger size",
            "menor": "smaller size",
            "adicionar gavetas": "add drawers",
            "adicionar portas": "add doors",
            "sem gavetas": "without drawers",
            "sem portas": "without doors",
            "mudar cor": "change color to",
            "mais moderno": "more modern design",
            "mais rústico": "more rustic appearance",
            "madeira natural": "natural wood tone",
            "branco": "white color",
            "preto": "black color",
            "cinza": "gray color"
        }

        # Traduzir notas de refinamento
        refinement_english = refinement_notes.lower()
        for pt, en in refinement_translations.items():
            refinement_english = refinement_english.replace(pt, en)

        # Inserir refinamento antes dos detalhes de qualidade
        quality_marker = "professional furniture photography"
        if quality_marker in original_prompt:
            parts = original_prompt.split(quality_marker)
            refined = f"{parts[0]}, {refinement_english}, {quality_marker}{parts[1]}"
        else:
            # Se não encontrar o marcador, adiciona no meio
            parts = original_prompt.split(",")
            mid = len(parts) // 2
            parts.insert(mid, f" {refinement_english}")
            refined = ",".join(parts)

        return refined

    def generate_simple_description(
        self,
        furniture_type: FurnitureType,
        room: Room,
        style: FurnitureStyle
    ) -> str:
        """
        Gera descrição SIMPLES em português para mostrar ao marceneiro

        Args:
            furniture_type: Tipo de móvel
            room: Ambiente
            style: Estilo

        Returns:
            Descrição amigável em português
        """

        furniture_names = {
            FurnitureType.CADEIRA: "Cadeira",
            FurnitureType.SOFA: "Sofá",
            FurnitureType.ARMARIO: "Armário",
            FurnitureType.ESTANTE: "Estante",
            FurnitureType.MESA: "Mesa",
            FurnitureType.BANCADA: "Bancada",
            FurnitureType.CAMA: "Cama",
            FurnitureType.CRIADO: "Criado-mudo",
            FurnitureType.OUTRO: "Móvel"
        }

        room_names = {
            Room.COZINHA: "cozinha",
            Room.SALA: "sala",
            Room.QUARTO: "quarto",
            Room.BANHEIRO: "banheiro",
            Room.ESCRITORIO: "escritório",
            Room.AREA_EXTERNA: "área externa",
            Room.LAVANDERIA: "lavanderia",
            Room.GARAGEM: "garagem"
        }

        style_names = {
            FurnitureStyle.MODERNO: "moderna",
            FurnitureStyle.RUSTICO: "rústica",
            FurnitureStyle.INDUSTRIAL: "industrial",
            FurnitureStyle.CLASSICO: "clássica",
            FurnitureStyle.CONTEMPORANEO: "contemporânea",
            FurnitureStyle.PROVENCAL: "provençal"
        }

        furniture = furniture_names.get(furniture_type, str(furniture_type.value))
        ambiente = room_names.get(room, str(room.value))
        estilo = style_names.get(style, str(style.value))

        return f"{furniture} {estilo} para {ambiente}"


# Instância global do gerador
prompt_generator = PromptGenerator()
