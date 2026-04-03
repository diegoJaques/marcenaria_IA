# Software Design Specification (SDS)
## MarcenAI - Sistema de Geração de Projetos de Marcenaria com IA

**Versão:** 1.0
**Data:** 03/04/2026
**Autor:** Diego Jaques Tinoco (RA: 38182672)
**Curso:** CST em Análise e Desenvolvimento de Sistemas
**Componente:** Projeto de Extensão II

---

## 1. INTRODUÇÃO

### 1.1 Propósito
Este documento descreve o design e a arquitetura do sistema MarcenAI, uma aplicação web desenvolvida para auxiliar marceneiros artesãos na criação de visualizações fotorrealísticas de projetos de móveis utilizando Inteligência Artificial.

### 1.2 Escopo
O MarcenAI é um sistema full-stack que:
- Coleta informações de projetos através de questionário guiado
- Gera prompts otimizados automaticamente
- Integra-se com OpenAI DALL-E para criar imagens
- Armazena projetos e imagens
- Permite refinamentos iterativos

### 1.3 Contexto do Projeto
**Programa de Extensão:** Ação e Difusão Cultural
**Objetivo:** Utilizar tecnologia para auxiliar profissionais de atividades culturais/artesanais

**Problema Identificado:**
Marceneiros precisam mostrar aos clientes como ficará o móvel antes de produzi-lo. Muitos usam ferramentas de IA de forma ineficiente, com prompts genéricos e muitas iterações.

**Solução Proposta:**
Interface simplificada que automatiza a geração de prompts otimizados, democratizando o acesso à tecnologia de IA para artesãos sem conhecimento técnico.

### 1.4 Stakeholders
- **Usuário Final:** Marceneiros artesãos (sem conhecimento técnico)
- **Cliente Final:** Clientes dos marceneiros (recebem as visualizações)
- **Desenvolvedor:** Diego Jaques Tinoco
- **Orientadores:** Professores do curso de ADS

---

## 2. VISÃO GERAL DO SISTEMA

### 2.1 Arquitetura Geral

```
┌────────────────────────────────────────────────────┐
│              CAMADA DE APRESENTAÇÃO                │
│         React + TailwindCSS (Frontend)             │
│    - Interface simplificada para não-técnicos      │
│    - Questionário guiado passo a passo             │
│    - Visualização de projetos e imagens            │
└─────────────────┬──────────────────────────────────┘
                  │ REST API (HTTP/JSON)
┌─────────────────▼──────────────────────────────────┐
│            CAMADA DE APLICAÇÃO                     │
│           FastAPI + Python (Backend)               │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  Rotas/Controllers                           │  │
│  │  - ProjectsRouter                            │  │
│  │  - HealthRouter                              │  │
│  └──────────────┬───────────────────────────────┘  │
│                 │                                   │
│  ┌──────────────▼───────────────────────────────┐  │
│  │  Serviços de Negócio                         │  │
│  │  - PromptGenerator (Engine de Prompts)       │  │
│  │  - OpenAIService (Integração DALL-E)         │  │
│  │  - MinIOService (Armazenamento)              │  │
│  └──────────────┬───────────────────────────────┘  │
│                 │                                   │
│  ┌──────────────▼───────────────────────────────┐  │
│  │  Modelos de Dados (ORM)                      │  │
│  │  - Project, ProjectImage, Enums              │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────┬──────────────┬───────────────────┘
                  │              │
       ┌──────────▼────┐    ┌────▼──────────┐
       │  PostgreSQL   │    │     MinIO     │
       │  (Metadados)  │    │   (Imagens)   │
       └───────────────┘    └───────────────┘
                  │
       ┌──────────▼────────────┐
       │   OpenAI API          │
       │   (DALL-E 3)          │
       └───────────────────────┘
```

### 2.2 Padrões Arquiteturais Aplicados

1. **MVC (Model-View-Controller):**
   - **Model:** SQLAlchemy models (Project, ProjectImage)
   - **View:** React components
   - **Controller:** FastAPI routes/endpoints

2. **Repository Pattern:**
   - Abstração do acesso a dados através do SQLAlchemy ORM

3. **Service Layer:**
   - Lógica de negócio isolada em serviços (PromptGenerator, OpenAIService, MinIOService)

4. **RESTful API:**
   - Endpoints seguem convenções REST
   - Recursos identificados por URIs
   - Métodos HTTP semânticos (GET, POST, DELETE, PATCH)

5. **Microserviços (parcial):**
   - Separação de responsabilidades (Backend, Banco, Storage, IA)
   - Containerização com Docker

---

## 3. DESIGN DE DADOS

### 3.1 Modelo Entidade-Relacionamento

```
┌─────────────────────────────────────────────┐
│              PROJECT                        │
├─────────────────────────────────────────────┤
│ id (PK)                VARCHAR(36)          │
│ furniture_type         ENUM                 │
│ room                   ENUM                 │
│ style                  ENUM                 │
│ size                   VARCHAR(50)          │
│ dimensions             VARCHAR(200)         │
│ material               VARCHAR(100)         │
│ color                  VARCHAR(100)         │
│ special_features       TEXT                 │
│ client_name            VARCHAR(200)         │
│ client_notes           TEXT                 │
│ generated_prompt       TEXT                 │
│ created_at             TIMESTAMP            │
│ updated_at             TIMESTAMP            │
└─────────────────┬───────────────────────────┘
                  │
                  │ 1:N
                  │
┌─────────────────▼───────────────────────────┐
│           PROJECT_IMAGE                     │
├─────────────────────────────────────────────┤
│ id (PK)                VARCHAR(36)          │
│ project_id (FK)        VARCHAR(36)          │
│ image_url              VARCHAR(500)         │
│ minio_object_name      VARCHAR(200)         │
│ width                  INTEGER              │
│ height                 INTEGER              │
│ format                 VARCHAR(10)          │
│ file_size              INTEGER              │
│ prompt_used            TEXT                 │
│ refinement_notes       TEXT                 │
│ is_refined             INTEGER              │
│ is_selected            INTEGER              │
│ created_at             TIMESTAMP            │
└─────────────────────────────────────────────┘
```

### 3.2 Enumerações (Enums)

**FurnitureType:**
- cadeira, sofa, armario, estante, mesa, bancada, cama, criado, outro

**Room:**
- cozinha, sala, quarto, banheiro, escritorio, area_externa, lavanderia, garagem

**FurnitureStyle:**
- moderno, rustico, industrial, classico, contemporaneo, provencal

### 3.3 Estratégia de Armazenamento

1. **Metadados (PostgreSQL):**
   - Informações estruturadas dos projetos
   - Relacionamentos entre entidades
   - Queries eficientes com índices

2. **Imagens (MinIO - S3-compatible):**
   - Arquivos binários de imagens
   - Escalabilidade horizontal
   - URLs públicas para acesso

3. **Separação de Responsabilidades:**
   - Banco relacional: O QUE armazenar
   - Object storage: ONDE armazenar

---

## 4. DESIGN DE COMPONENTES

### 4.1 Backend (FastAPI)

#### 4.1.1 Módulo: Core
**Responsabilidade:** Configurações centralizadas

**Componentes:**
- `config.py`: Gerenciamento de variáveis de ambiente (Settings)
- `database.py`: Setup SQLAlchemy, engine, sessões

#### 4.1.2 Módulo: Models
**Responsabilidade:** Definição de estruturas de dados

**Componentes:**
- `project.py`: Modelos ORM (Project, ProjectImage, Enums)
- `schemas.py`: Schemas Pydantic para validação/serialização

#### 4.1.3 Módulo: Services
**Responsabilidade:** Lógica de negócio

**Componentes:**

1. **PromptGenerator** (`prompt_generator.py`)
   - **Entrada:** Dados simples do formulário
   - **Processamento:**
     - Tradução para inglês técnico
     - Enriquecimento com contexto profissional
     - Adição de parâmetros de qualidade
   - **Saída:** Prompt otimizado para DALL-E
   - **Algoritmo:**
     ```
     prompt = [
       "Introdução fotorrealista",
       "Estilo + Tipo de móvel",
       "Material",
       "Cor",
       "Características especiais",
       "Detalhes do estilo",
       "Contexto do ambiente",
       "Parâmetros de qualidade (iluminação, resolução)"
     ].join(", ")
     ```

2. **OpenAIService** (`openai_service.py`)
   - **Responsabilidade:** Comunicação com API OpenAI
   - **Métodos:**
     - `generate_image(prompt)`: Gera imagem via DALL-E
     - `download_image(url)`: Baixa imagem gerada
     - `validate_api_key()`: Valida credenciais
   - **Tratamento de Erros:** Rate limiting, timeouts, API errors

3. **MinIOService** (`minio_service.py`)
   - **Responsabilidade:** Gerenciamento de armazenamento
   - **Métodos:**
     - `upload_image(bytes, filename)`: Upload para bucket
     - `get_public_url(object_name)`: URL pública
     - `delete_image(object_name)`: Remoção
   - **Configuração:** Buckets, políticas de acesso

#### 4.1.4 Módulo: Routes
**Responsabilidade:** Endpoints HTTP

**Rotas:**

1. **Health Router** (`health.py`)
   ```
   GET  /health  - Status de todos os serviços
   GET  /ping    - Ping básico
   ```

2. **Projects Router** (`projects.py`)
   ```
   POST   /api/v1/projects              - Criar projeto + gerar imagem
   GET    /api/v1/projects              - Listar projetos (paginado)
   GET    /api/v1/projects/{id}         - Detalhes do projeto
   POST   /api/v1/projects/{id}/refine  - Refinar/ajustar imagem
   DELETE /api/v1/projects/{id}         - Deletar projeto
   PATCH  /api/v1/projects/{id}/images/{image_id}/select - Marcar favorita
   ```

### 4.2 Frontend (React)

#### 4.2.1 Estrutura de Componentes

```
App
├── Router
    ├── HomePage
    │   └── Cards de ação (Criar, Listar)
    │
    ├── NewProjectPage
    │   ├── ProgressBar (passo a passo)
    │   ├── Step1: FurnitureSelector
    │   ├── Step2: RoomSelector
    │   ├── Step3: StyleSelector
    │   └── Step4: DetailsForm
    │
    ├── ProjectListPage
    │   └── ProjectCard[] (grid de projetos)
    │
    └── ProjectDetailPage
        ├── ImageViewer (principal + thumbnails)
        ├── ProjectInfo (detalhes)
        └── RefineForm (ajustes)
```

#### 4.2.2 Serviços (API Client)

**api.js**
- Cliente Axios configurado
- Funções para cada endpoint
- Tratamento centralizado de erros

#### 4.2.3 Estado e Gerenciamento
- **Local State** (useState): Estado de componentes individuais
- **Navigation State** (React Router): Rotas e navegação
- **Sem Redux:** Aplicação simples não necessita estado global complexo

---

## 5. DESIGN DE INTERFACE (IHC - Interação Humano-Computador)

### 5.1 Princípios de Design Aplicados

#### 5.1.1 Design Centrado no Usuário
**Persona:** Marceneiro artesão, 40-60 anos, sem conhecimento técnico

**Características:**
- Acostumado com trabalho manual
- Pode ter dificuldade com tecnologia
- Precisa de feedback visual constante
- Aprende melhor com exemplos visuais

#### 5.1.2 Heurísticas de Nielsen Aplicadas

1. **Visibilidade do Status do Sistema**
   - Barra de progresso mostra etapa atual (1 de 4)
   - Loading spinners durante processamento
   - Mensagens de sucesso/erro claras

2. **Correspondência entre Sistema e Mundo Real**
   - Ícones reconhecíveis: 🪑🛋️🚪📚
   - Linguagem cotidiana (não técnica)
   - Perguntas diretas e simples

3. **Controle e Liberdade do Usuário**
   - Botão "Voltar" em cada etapa
   - Confirmação antes de deletar
   - Pode refinar/ajustar imagens

4. **Consistência e Padrões**
   - Cores consistentes (wood-600 para ações primárias)
   - Botões sempre no mesmo local
   - Layout previsível

5. **Prevenção de Erros**
   - Validação em tempo real
   - Botões desabilitados quando não aplicável
   - Confirmações para ações destrutivas

6. **Reconhecimento em vez de Memorização**
   - Opções mostradas visualmente (não precisa lembrar)
   - Histórico de projetos visível
   - Thumbnails para identificação rápida

7. **Flexibilidade e Eficiência de Uso**
   - Campos opcionais claramente marcados
   - Pode pular detalhes e criar rápido
   - Pode adicionar detalhes para melhor resultado

8. **Design Estético e Minimalista**
   - Uma pergunta por tela
   - Espaço em branco adequado
   - Sem informações desnecessárias

9. **Ajudar Usuários a Reconhecer, Diagnosticar e Recuperar Erros**
   - Mensagens de erro em português claro
   - Sugestões de solução
   - Botão para tentar novamente

10. **Ajuda e Documentação**
    - Dicas contextuais (💡)
    - Placeholders descritivos
    - Exemplos em campos de texto

### 5.2 Paleta de Cores

**Tema "Madeira" (acolhedor, artesanal):**
```
wood-50:  #faf8f5  (background claro)
wood-100: #f5f0e8
wood-200: #e8dcc8
wood-300: #d4bd9a
wood-400: #c19b6b
wood-500: #a67c52
wood-600: #8b6240  (primário)
wood-700: #6e4e33  (header)
wood-800: #563d28
wood-900: #44311f
```

### 5.3 Tipografia

- **Fonte:** System fonts (sans-serif nativo do SO)
- **Tamanhos:**
  - Título: 3xl-4xl (grandes e legíveis)
  - Corpo: lg-xl (confortável)
  - Botões: lg-2xl (fácil de ler)

### 5.4 Elementos de UI

**Botões:**
- Grandes (py-4 px-8 mínimo)
- Ícones + texto
- States visuais (hover, disabled)
- Sombras para profundidade

**Cards de Opção:**
- Ícone grande (text-5xl)
- Label claro
- Border destacado quando selecionado
- Hover feedback

**Formulários:**
- Labels descritivos
- Placeholders com exemplos
- Campos grandes (py-3)
- Focus states claros

---

## 6. INTEGRAÇÃO COM SISTEMAS EXTERNOS

### 6.1 OpenAI API (DALL-E 3)

**Endpoint:** `https://api.openai.com/v1/images/generations`

**Autenticação:** Bearer Token (API Key)

**Payload:**
```json
{
  "model": "dall-e-3",
  "prompt": "string (max 4000 chars)",
  "n": 1,
  "size": "1024x1024",
  "quality": "standard",
  "response_format": "url"
}
```

**Response:**
```json
{
  "data": [
    {
      "url": "https://...",
      "revised_prompt": "string"
    }
  ]
}
```

**Tratamento de Erros:**
- 401: API key inválida
- 429: Rate limit excedido (retry com backoff)
- 400: Prompt inválido (validar conteúdo)

**Custos:**
- Standard 1024x1024: $0.040/imagem
- HD 1024x1024: $0.080/imagem

### 6.2 MinIO (Object Storage)

**Protocolo:** S3-compatible API

**Operações:**
- `put_object`: Upload de imagens
- `get_object`: Download
- `remove_object`: Deleção
- `presigned_get_object`: URLs temporárias

**Configuração de Bucket:**
- Nome: `project-images`
- Política: Leitura pública
- Organização: `projects/{uuid}.png`

---

## 7. SEGURANÇA

### 7.1 Autenticação e Autorização

**Status Atual:** Não implementado (MVP)

**Planejamento Futuro:**
- JWT tokens
- Login com email/senha
- Projetos privados por usuário

### 7.2 Proteção de Dados Sensíveis

1. **API Keys:**
   - Armazenadas em variáveis de ambiente
   - Não versionadas no Git (.gitignore)
   - Não expostas no frontend

2. **CORS:**
   - Configurado para aceitar apenas origens permitidas
   - Produção: domínio específico

3. **Validação de Inputs:**
   - Pydantic schemas no backend
   - Validação de tipos
   - Sanitização de strings

4. **SQL Injection:**
   - Prevenido pelo ORM SQLAlchemy
   - Prepared statements

### 7.3 Limitações de Taxa (Rate Limiting)

**Planejamento:** Implementar limite por IP/usuário
- 10 criações de projeto por hora
- 20 refinamentos por hora

---

## 8. DESEMPENHO

### 8.1 Métricas de Performance

| Operação | Tempo Esperado | Observações |
|----------|----------------|-------------|
| Carregar homepage | < 1s | Cache de assets |
| Criar projeto | 20-40s | Limitado pela API OpenAI |
| Listar projetos | < 500ms | Paginação aplicada |
| Refinar imagem | 20-40s | Chamada OpenAI |
| Carregar imagem | < 2s | Depende da rede |

### 8.2 Otimizações Implementadas

1. **Backend:**
   - Connection pooling (SQLAlchemy)
   - Async/await para I/O operations
   - Lazy loading de relacionamentos ORM

2. **Frontend:**
   - Code splitting (React Router)
   - Lazy loading de componentes
   - Caching de imagens pelo navegador

3. **Infraestrutura:**
   - MinIO para servir imagens (não backend)
   - Nginx como reverse proxy (planejado)
   - Compressão Gzip

### 8.3 Escalabilidade

**Horizontal (Multi-instância):**
- Backend stateless (pode rodar N réplicas)
- Load balancer (planejado)

**Vertical (Recursos):**
- PostgreSQL: Aumentar memória/CPU
- MinIO: Adicionar disks

---

## 9. TESTES

### 9.1 Estratégia de Testes

| Tipo | Ferramentas | Status |
|------|-------------|--------|
| Unitários | pytest | Planejado |
| Integração | pytest + httpx | Planejado |
| E2E | Cypress/Playwright | Planejado |
| Manual | Desenvolvedor | ✅ Executado |

### 9.2 Casos de Teste Principais

**Fluxo Completo (Manual):**
1. ✅ Criar projeto com dados mínimos
2. ✅ Criar projeto com dados completos
3. ✅ Visualizar lista de projetos
4. ✅ Abrir detalhes do projeto
5. ✅ Refinar imagem existente
6. ✅ Deletar projeto

**Health Checks:**
1. ✅ API está acessível
2. ✅ Banco de dados conecta
3. ✅ MinIO está acessível
4. ⚠️ OpenAI key válida (requer configuração)

---

## 10. DEPLOYMENT (IMPLANTAÇÃO)

### 10.1 Ambiente de Desenvolvimento

**Pré-requisitos:**
- Docker 20+
- Docker Compose 2+
- OpenAI API Key

**Comando:**
```bash
docker-compose up --build
```

**Serviços:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- PostgreSQL: localhost:5432
- MinIO: http://localhost:9000 (API) e :9001 (console)

### 10.2 Ambiente de Produção (Planejado)

**Opções:**
1. **Cloud (AWS/GCP/Azure):**
   - ECS/EKS para containers
   - RDS para PostgreSQL
   - S3 para imagens (substituir MinIO)

2. **PaaS (Heroku, Railway, Render):**
   - Deploy simplificado
   - Managed database
   - Auto-scaling

**Requisitos Mínimos:**
- CPU: 2 cores
- RAM: 4GB
- Disk: 20GB (+ storage para imagens)

### 10.3 CI/CD (Planejado)

**Pipeline:**
```
git push → GitHub Actions
    ├─ Testes unitários
    ├─ Build Docker images
    ├─ Push para registry
    └─ Deploy automático
```

---

## 11. MANUTENÇÃO E EVOLUÇÃO

### 11.1 Monitoramento

**Planejado:**
- Logs centralizados (ELK Stack)
- Métricas (Prometheus + Grafana)
- Alertas (downtime, erros, custos OpenAI)

### 11.2 Backup

**Estratégia:**
1. **Banco de Dados:**
   - Backup diário automático
   - Retenção: 30 dias
   - Restore testado mensalmente

2. **Imagens (MinIO):**
   - Replicação para S3 (opcional)
   - Versionamento ativado

### 11.3 Roadmap de Features Futuras

**Curto Prazo (1-3 meses):**
- [ ] Sistema de autenticação/login
- [ ] Exportar projeto para PDF
- [ ] Compartilhamento via link
- [ ] Testes automatizados

**Médio Prazo (3-6 meses):**
- [ ] Templates de prompts reutilizáveis
- [ ] Integração com WhatsApp
- [ ] Sistema de orçamento baseado no projeto
- [ ] Multi-idioma (PT/EN)

**Longo Prazo (6-12 meses):**
- [ ] Mobile app (React Native)
- [ ] Integração com ferramentas de CAD
- [ ] Marketplace de marceneiros
- [ ] IA para sugerir materiais e custos

---

## 12. CONCLUSÃO

### 12.1 Objetivos Alcançados

✅ **Técnicos:**
- Sistema full-stack funcional
- Arquitetura escalável e bem estruturada
- Interface responsiva e acessível
- Integração com IA de ponta (DALL-E 3)

✅ **Acadêmicos:**
- Aplicação de competências do curso (IHC, Requisitos, Gerência de Projetos)
- Documentação completa (SDS)
- Metodologia PDCA aplicada
- Alinhamento com ODS

✅ **Sociais:**
- Democratização de tecnologia para artesãos
- Impacto cultural positivo
- Solução de problema real

### 12.2 Lições Aprendidas

1. **Design para Não-Técnicos é Crucial:**
   - Ícones e linguagem simples fazem toda diferença
   - Feedback constante aumenta confiança do usuário

2. **Automação de Prompts é Poderosa:**
   - Engine de geração economiza tempo do usuário
   - Resultados consistentemente melhores

3. **Arquitetura Modular Facilita Evolução:**
   - Separação clara de responsabilidades
   - Fácil adicionar features

### 12.3 Referências

1. BENYON, David. **Interação humano-computador**. 2.ed. São Paulo: Pearson, 2011.
2. SEGURAGO, Valquíria Santos. **Projeto de interface com o usuário**. São Paulo: Pearson, 2017.
3. OpenAI. **DALL-E 3 API Documentation**. Disponível em: https://platform.openai.com/docs
4. FastAPI. **Documentation**. Disponível em: https://fastapi.tiangolo.com
5. React. **Documentation**. Disponível em: https://react.dev

---

**Documento elaborado por:**
Diego Jaques Tinoco
RA: 38182672
Polo Anhanguera Nova Odessa
Projeto de Extensão II - CST em Análise e Desenvolvimento de Sistemas
