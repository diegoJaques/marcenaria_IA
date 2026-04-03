-- Script de inicialização do banco de dados MarcenAI
-- Executado automaticamente na primeira inicialização do PostgreSQL

-- Criar extensão para UUIDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Comentários sobre o schema
COMMENT ON DATABASE marcenai_db IS 'Banco de dados do sistema MarcenAI - Gerador de projetos de marcenaria com IA';

-- Criar schema principal (as tabelas serão criadas pelo SQLAlchemy)
-- Este arquivo garante que o database está pronto para receber as migrations

SELECT 'Database MarcenAI inicializado com sucesso!' as status;
