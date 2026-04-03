# MarcenAI Frontend - Dockerfile
FROM node:18-alpine

# Diretório de trabalho
WORKDIR /app

# Copiar package files
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar código
COPY . .

# Expor porta
EXPOSE 3000

# Comando padrão
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
