# 🚀 GUIA DE INÍCIO RÁPIDO - MarcenAI

## Passo a Passo para Rodar o Projeto

### 1️⃣ Pré-requisitos

Você precisa ter instalado:
- **Docker** (https://www.docker.com/get-started)
- **Docker Compose** (geralmente já vem com o Docker)
- **Chave de API do OpenAI** (veja abaixo como obter)

### 2️⃣ Obter Chave da OpenAI

1. Acesse: https://platform.openai.com/signup
2. Crie uma conta (se não tiver)
3. Vá em: https://platform.openai.com/api-keys
4. Clique em "Create new secret key"
5. Copie a chave (começa com `sk-...`)
6. **IMPORTANTE:** Você precisa adicionar créditos na conta OpenAI para usar a API

### 3️⃣ Configurar o Projeto

1. **Navegue até a pasta do projeto:**
   ```bash
   cd "C:\Users\Diego\OneDrive\Área de Trabalho\Facul\Projeto Expansão 2\marcenai"
   ```

2. **Copie o arquivo de exemplo de variáveis de ambiente:**
   ```bash
   copy .env.example .env
   ```

3. **Edite o arquivo `.env` e adicione sua chave do OpenAI:**

   Abra o arquivo `.env` com um editor de texto (Bloco de Notas, VS Code, etc.) e substitua:

   ```
   OPENAI_API_KEY=sk-your-openai-api-key-here
   ```

   Por:

   ```
   OPENAI_API_KEY=sk-suachaveverdadeira123456...
   ```

### 4️⃣ Iniciar o Sistema

1. **Abra um terminal na pasta do projeto**

2. **Execute o comando:**
   ```bash
   docker-compose up --build
   ```

3. **Aguarde** a inicialização (pode demorar 2-5 minutos na primeira vez)

4. **Você verá várias mensagens no terminal. Quando aparecer:**
   ```
   ✅ Tabelas do banco de dados criadas/verificadas
   🚀 Iniciando MarcenAI...
   ```

   **O sistema está pronto!**

### 5️⃣ Acessar o Sistema

Abra seu navegador e acesse:

- **Aplicação (Frontend):** http://localhost:3000
- **API (Documentação):** http://localhost:8000/docs
- **MinIO Console:** http://localhost:9001

### 6️⃣ Usar o Sistema

1. Na tela inicial, clique em **"Criar Novo Projeto"**
2. Responda as perguntas simples (tipo de móvel, ambiente, estilo)
3. Aguarde a IA criar a imagem (leva ~20-30 segundos)
4. Veja o resultado! Se quiser ajustar, clique em **"Ajustar Imagem"**

---

## 🛑 Parar o Sistema

No terminal onde está rodando, pressione:
```
Ctrl + C
```

Para parar e remover tudo:
```bash
docker-compose down
```

---

## 🔄 Rodar Novamente (Próximas Vezes)

```bash
cd "C:\Users\Diego\OneDrive\Área de Trabalho\Facul\Projeto Expansão 2\marcenai"
docker-compose up
```

Sem o `--build`, inicia mais rápido!

---

## ❗ Resolução de Problemas

### Erro: "API Key inválida"
- Verifique se copiou a chave corretamente no arquivo `.env`
- Verifique se tem créditos na sua conta OpenAI

### Erro: "Porta já em uso"
- Algum outro programa está usando a porta 3000, 8000, 5432, 9000 ou 9001
- Solução: Feche o programa ou mude a porta no `docker-compose.yml`

### Erro: "Docker não encontrado"
- Instale o Docker Desktop: https://www.docker.com/get-started

### Banco de dados não conecta
```bash
docker-compose down -v
docker-compose up --build
```

Isso recria tudo do zero.

---

## 📱 Testando a API Diretamente

Você pode testar a API acessando:
http://localhost:8000/docs

Lá você consegue testar todos os endpoints interativamente!

---

## 📊 Verificar Se Tudo Está Funcionando

1. **Health Check:**
   http://localhost:8000/health

   Deve retornar status "healthy" ou "degraded" (se não configurou OpenAI ainda)

2. **Ping:**
   http://localhost:8000/ping

   Deve retornar "pong"

3. **Frontend:**
   http://localhost:3000

   Deve mostrar a tela inicial do MarcenAI

---

## 💡 Dicas

1. **Primeira execução demora mais** - Docker baixa as imagens necessárias
2. **Mantenha o terminal aberto** - Para ver os logs do sistema
3. **Cada imagem custa ~$0.04** - Fique de olho nos créditos da OpenAI
4. **Para desenvolvimento:** O código atualiza automaticamente (hot reload)

---

## 📞 Precisa de Ajuda?

- Veja os logs no terminal
- Acesse http://localhost:8000/docs para testar a API
- Verifique se todos os containers estão rodando: `docker-compose ps`

---

**Pronto! Agora é só usar! 🎉🪵**
