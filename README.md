#  MarcenAI

**Sistema Inteligente de Geração de Projetos de Marcenaria com IA**

Projeto de Extensão II - Análise e Desenvolvimento de Sistemas
Aluno: Diego Jaques Tinoco (RA: 38182672)
Polo: Anhanguera Nova Odessa

---

##  Sobre o Projeto

MarcenAI é uma aplicação que auxilia marceneiros a gerar visualizações fotorrealísticas de projetos de móveis usando Inteligência Artificial. O sistema foi desenvolvido pensando em profissionais que não têm conhecimento técnico, oferecendo uma interface extremamente simples e intuitiva.

### O Problema

Marceneiros frequentemente precisam mostrar aos clientes como ficará o móvel antes de produzi-lo. Muitos usam ferramentas de IA como ChatGPT, mas:
- Escrevem prompts curtos e genéricos
- Precisam de muitas tentativas para chegar no resultado
- Perdem muito tempo no processo iterativo
- Clientes muitas vezes não sabem descrever o que querem

### A Solução

MarcenAI resolve isso através de:
1. **Questionário guiado** com perguntas simples em linguagem cotidiana
2. **Geração automática de prompts otimizados** (invisível para o usuário)
3. **Integração com DALL-E** para criar imagens profissionais
4. **Refinamento iterativo** com linguagem natural ("adicionar gavetas", "mudar cor")
5. **Histórico de projetos** para reutilização

---

##  Arquitetura

```
┌─────────────────────────────────────┐
│   Frontend (React + TailwindCSS)    │
│   - Interface super simples         │
│   - Mobile-first                     │
│   - Linguagem não técnica           │
└──────────────┬──────────────────────┘
               │ REST API
┌──────────────▼──────────────────────┐
│   Backend (FastAPI + Python)        │
│   - Engine de prompts                │
│   - Integração OpenAI                │
│   - Lógica de negócio               │
└─────┬────────────────┬──────────────┘
      │                │
┌─────▼─────┐    ┌─────▼─────┐
│PostgreSQL │    │   MinIO   │
│ (Projetos)│    │ (Imagens) │
└───────────┘    └───────────┘
```

**Tudo orquestrado com Docker Compose!**

---

##  Como Rodar

### Pré-requisitos

- Docker e Docker Compose instalados
- Chave de API do OpenAI ([obtenha aqui](https://platform.openai.com/api-keys))

### Passo a Passo

1. **Clone o repositório (ou navegue até a pasta)**
   ```bash
   cd marcenai
   ```

2. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   ```

   Edite o arquivo `.env` e adicione sua chave do OpenAI:
   ```
   OPENAI_API_KEY=sk-sua-chave-aqui
   ```

3. **Inicie os serviços com Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Aguarde a inicialização** (primeira vez pode demorar ~2-3 minutos)

5. **Acesse a aplicação:**
   - **Frontend:** http://localhost:3000
   - **API (Docs):** http://localhost:8000/docs
   - **MinIO Console:** http://localhost:9001 (minioadmin / minioadmin123)

---

##  Serviços

| Serviço | Porta | Descrição |
|---------|-------|-----------|
| Frontend | 3000 | Interface React do usuário |
| Backend API | 8000 | API REST FastAPI |
| PostgreSQL | 5432 | Banco de dados |
| MinIO API | 9000 | Object storage (S3-compatible) |
| MinIO Console | 9001 | Interface web do MinIO |

---

## 🎯 Funcionalidades

### ✅ Implementadas

- [x] Criação de projetos com questionário guiado
- [x] Geração automática de prompts otimizados
- [x] Integração com DALL-E 3 para gerar imagens
- [x] Upload automático para MinIO
- [x] Histórico de projetos
- [x] Visualização de detalhes do projeto
- [x] Refinamento de imagens com linguagem natural
- [x] Seleção de imagem favorita
- [x] Deleção de projetos

### 🚧 Próximas Features (Futuras)

- [ ] Exportar projeto para PDF
- [ ] Compartilhamento via link
- [ ] Sistema de templates de prompts
- [ ] Integração com WhatsApp
- [ ] Orçamento automático baseado no projeto

---

## 🛠️ Stack Tecnológica

### Backend
- **Python 3.11** - Linguagem
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados relacional
- **MinIO** - Object storage (S3-compatible)
- **OpenAI API** - DALL-E 3 para geração de imagens

### Frontend
- **React 18** - Library UI
- **Vite** - Build tool rápido
- **TailwindCSS** - Framework CSS utility-first
- **Axios** - Cliente HTTP

### DevOps
- **Docker** - Containerização
- **Docker Compose** - Orquestração multi-container

---

## 📚 Documentação

### API Documentation

A documentação interativa da API está disponível em:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Principais Endpoints

```
POST   /api/v1/projects              - Criar novo projeto + gerar imagem
GET    /api/v1/projects              - Listar todos os projetos
GET    /api/v1/projects/{id}         - Buscar projeto específico
POST   /api/v1/projects/{id}/refine  - Refinar imagem existente
DELETE /api/v1/projects/{id}         - Deletar projeto
GET    /health                        - Health check
```

---

## 🧪 Testando a API

### Criar um Projeto

```bash
curl -X POST http://localhost:8000/api/v1/projects \
  -H "Content-Type: application/json" \
  -d '{
    "furniture_type": "armario",
    "room": "cozinha",
    "style": "moderno",
    "size": "grande",
    "material": "MDF branco",
    "color": "branco com detalhes pretos",
    "special_features": "3 gavetas, 2 portas com vidro",
    "client_name": "João da Silva"
  }'
```

### Listar Projetos

```bash
curl http://localhost:8000/api/v1/projects
```

---

## 🎨 Design Principles

### UX para Não-Técnicos

O projeto foi desenvolvido considerando que o usuário final (marceneiro) **NÃO tem conhecimento técnico**:

1. **Linguagem Simples** - Zero jargões técnicos
2. **Ícones Visuais** - 🪑🛋️🚪 para facilitar identificação
3. **Passo a Passo Guiado** - Uma pergunta por vez
4. **Feedback Constante** - "Estou criando seu projeto..."
5. **Erros Amigáveis** - Mensagens em português claro

---


