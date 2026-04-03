# TEMPLATE PDCA - PROJETO MARCENAI

**ALUNO:** Diego Jaques Tinoco
**RA:** 38182672
**CURSO:** CST EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
**COMPONENTE CURRICULAR:** PROJETO DE EXTENSÃO II
**PROGRAMA DE EXTENSÃO:** PROGRAMA DE AÇÃO E DIFUSÃO CULTURAL

---

## METAS DOS ODS ADERENTES AO PROJETO

**ODS 8 - Trabalho Decente e Crescimento Econômico**
- Meta 8.3: Promover políticas orientadas para o desenvolvimento que apoiem as atividades produtivas, geração de emprego decente, empreendedorismo, criatividade e inovação, e incentivar a formalização e o crescimento das micro, pequenas e médias empresas, inclusive por meio do acesso a serviços financeiros.

**ODS 9 - Indústria, Inovação e Infraestrutura**
- Meta 9.3: Aumentar o acesso das pequenas indústrias e outras empresas, particularmente em países em desenvolvimento, aos serviços financeiros, incluindo crédito acessível e sua integração em cadeias de valor e mercados.
- Meta 9.c: Aumentar significativamente o acesso à tecnologia da informação e comunicação e se empenhar para oferecer acesso universal e a preços acessíveis à internet.

**ODS 11 - Cidades e Comunidades Sustentáveis**
- Meta 11.4: Fortalecer esforços para proteger e salvaguardar o patrimônio cultural e natural do mundo, incluindo o apoio às atividades artesanais e culturais locais.

---

## 1. PLANEJAMENTO (PLAN)

### DEFINIÇÃO DA PROPOSTA

**Nome do Projeto:** MarcenAI - Sistema Inteligente de Geração de Projetos de Marcenaria com IA

**Descrição:**
Desenvolvimento de uma aplicação web que auxilia marceneiros artesãos na criação de visualizações fotorrealísticas de projetos de móveis utilizando Inteligência Artificial. O sistema transforma descrições simples em prompts otimizados para geração de imagens profissionais através da tecnologia DALL-E da OpenAI, democratizando o acesso à tecnologia avançada para profissionais sem conhecimento técnico.

**Justificativa:**
Marceneiros artesãos enfrentam dificuldades em apresentar aos clientes visualizações realistas de como ficará o móvel antes de produzi-lo. Muitos tentam usar ferramentas de IA de forma ineficiente, com prompts genéricos que resultam em múltiplas tentativas até alcançar o resultado desejado, desperdiçando tempo e recursos. Além disso, clientes frequentemente não conseguem descrever claramente o que desejam, dificultando o processo criativo.

---

### IMERSÃO

#### 1. Problemas Identificados

**Principal problema:** Marceneiros perdem tempo e eficiência ao tentar usar IA (ChatGPT/DALL-E) para gerar imagens de projetos, pois:
- Utilizam prompts curtos e genéricos
- Necessitam de 5-10 iterações para resultados satisfatórios
- Não conhecem técnicas de "prompt engineering"
- Gastam tempo valioso que poderiam dedicar ao trabalho manual

**Problemas secundários:**
- Clientes não sabem descrever o que querem
- Dificuldade em apresentar conceitos visuais antes da produção
- Concorrência com marcenarias que usam tecnologia
- Custos elevados de softwares de design 3D profissionais

#### 1.1. Articulação com o Programa/Conteúdo

✅ **SIM.** O projeto está totalmente articulado com:
- **Ação e Difusão Cultural:** Auxilia artesãos (marceneiros) que fazem parte do patrimônio cultural artesanal
- **Conteúdos do curso:**
  - Interação Humano-Computador (IHC) - interface para não-técnicos
  - Engenharia de Requisitos - levantamento de necessidades reais
  - Processo de software - desenvolvimento estruturado
  - Gerência de projetos - uso de metodologia PDCA

#### 1.2. Viabilidade no Prazo

✅ **SIM.** O projeto pode ser desenvolvido no prazo do componente curricular (aproximadamente 4 meses):
- Infraestrutura pronta: Docker, bibliotecas open-source
- Tecnologias dominadas: Python, React
- API externa disponível: OpenAI DALL-E
- Escopo bem definido (MVP focado)

#### 1.3. Benefício à Comunidade

✅ **SIM.** A solução auxilia:
- **Diretamente:** Marceneiros artesãos que precisam apresentar projetos visualmente
- **Indiretamente:** Clientes que terão melhor visualização antes de decidir
- **Comunidade:** Preservação do ofício artesanal através de modernização tecnológica

#### 2. Pessoas Envolvidas

- **Desenvolvedor:** Diego Jaques Tinoco (aluno)
- **Beneficiário direto:** Marceneiros artesãos locais
- **Beneficiários indiretos:** Clientes dos marceneiros
- **Orientação acadêmica:** Professores do curso de ADS

#### 3. Local de Realização

- **Desenvolvimento:** Remoto (residência do aluno)
- **Testes e validação:** Com marceneiros da região de Nova Odessa/SP
- **Implantação:** Sistema web acessível de qualquer local com internet

#### 4. Limitações e Restrições

- **Acesso:** Nenhuma restrição - sistema web público
- **Técnicas:** Necessita conexão com internet
- **Financeiras:** Custos mínimos de API OpenAI (~$5-10 para testes)

#### 5. Pessoas Beneficiadas Diretamente

- Marceneiros artesãos (pequenos empresários do setor moveleiro)
- Estimativa: Potencial de alcançar centenas de profissionais
- Perfil: Artesãos sem formação técnica em informática, idade 30-65 anos

#### 6. Recursos Necessários

**Financeiros:** Mínimos
- API OpenAI: ~$10 USD para testes iniciais
- Infraestrutura: Gratuita (Docker local, GitHub)

**Técnicos:**
- Computador pessoal
- Conhecimentos em Python, React, Docker
- Acesso à internet

#### 7. Agendamento

- **Necessário:** Não (desenvolvimento autônomo)
- **Testes com usuários:** Flexível, conforme disponibilidade dos marceneiros

#### 8. Período de Realização

- **Duração total:** Março a Junho de 2026 (4 meses)
- **Dias da semana:** Segunda a sexta (período noturno) + finais de semana
- **Horário:** Flexível, conforme cronograma acadêmico

---

### IDEAÇÃO

#### Soluções Consideradas

**1. Sistema Web Completo com IA (ESCOLHIDA)**
- Interface simplificada para não-técnicos
- Geração automática de prompts otimizados
- Integração com DALL-E
- Armazenamento de projetos
- **Vantagem:** Resolve o problema na raiz, automatizando a complexidade

**2. Tutorial/Manual de Como Usar IA**
- Guia ensinando técnicas de prompt
- **Desvantagem:** Requer que o marceneiro aprenda e execute manualmente

**3. Template de Prompts Prontos**
- Biblioteca de prompts pré-escritos
- **Desvantagem:** Limitado, não atende casos específicos

**Decisão:** Opção 1 - Desenvolvimento do sistema automatizado MarcenAI

#### Funcionalidades Principais

1. **Questionário Guiado**
   - Perguntas simples em português
   - Ícones visuais para facilitar compreensão
   - Wizard passo a passo (4 etapas)

2. **Engine de Geração de Prompts**
   - Tradução automática para inglês técnico
   - Enriquecimento com parâmetros profissionais
   - Contextualização baseada em tipo/estilo de móvel

3. **Integração com IA**
   - Chamadas à API OpenAI DALL-E 3
   - Download e armazenamento automático
   - Tratamento de erros amigável

4. **Gerenciamento de Projetos**
   - Histórico completo
   - Refinamento iterativo
   - Seleção de favoritos

5. **Interface Ultra-Simplificada**
   - Linguagem não-técnica
   - Feedback visual constante
   - Mobile-first (funciona no celular)

---

### PROTOTIPAÇÃO

#### Tecnologias Selecionadas

**Frontend:**
- React 18 (interface dinâmica)
- Vite (build rápido)
- TailwindCSS (design responsivo)
- Axios (comunicação HTTP)

**Backend:**
- Python 3.11
- FastAPI (API REST moderna)
- SQLAlchemy (ORM)
- OpenAI SDK (integração DALL-E)

**Infraestrutura:**
- Docker + Docker Compose (orquestração)
- PostgreSQL 15 (banco de dados)
- MinIO (armazenamento de imagens S3-compatible)

**Justificativa das Escolhas:**
- **Docker:** Facilita implantação em qualquer ambiente
- **FastAPI:** Alta performance, documentação automática
- **React:** Interface moderna e responsiva
- **PostgreSQL:** Confiável, open-source, gratuito
- **MinIO:** Armazenamento escalável de imagens

#### Arquitetura do Sistema

```
Cliente (Navegador)
    ↓ HTTP/REST
Backend (FastAPI)
    ├→ PostgreSQL (dados)
    ├→ MinIO (imagens)
    └→ OpenAI API (geração)
```

#### Protótipo Desenvolvido

✅ **MVP Funcional Completo:**
- 4 páginas frontend (Home, Criar, Listar, Detalhes)
- 6 endpoints backend (CRUD + refinamento)
- Engine de prompts com 50+ templates contextualizados
- Integração OpenAI funcionando
- Sistema de armazenamento operacional

---

### IDEIAS E ANOTAÇÕES

**Aprendizados durante o planejamento:**
- A complexidade técnica deve ser invisível para o usuário final
- Prompts para IA exigem vocabulário técnico em inglês
- Marceneiros preferem visual a texto
- Mobile-first é essencial (muitos usam apenas celular)

**Decisões de design:**
- Usar emojis e ícones grandes (🪑🛋️🚪)
- Uma pergunta por vez (não sobrecarregar)
- Progress bar sempre visível
- Feedback em cada ação ("Criando mágica...")

---

## 2. REALIZAÇÃO (DO)

### CRONOGRAMA

| ATIVIDADES | PERÍODO 1 (Mar) | PERÍODO 2 (Abr) | PERÍODO 3 (Mai) | PERÍODO 4 (Jun) |
|------------|-----------------|-----------------|-----------------|-----------------|
| Planejamento e Imersão | ✅ Concluído | | | |
| Pesquisa de tecnologias | ✅ Concluído | | | |
| Setup infraestrutura (Docker) | ✅ Concluído | | | |
| Desenvolvimento Backend | ✅ Concluído | | | |
| Engine de Prompts | ✅ Concluído | | | |
| Integração OpenAI | ✅ Concluído | | | |
| Desenvolvimento Frontend | | ✅ Concluído | | |
| Testes e ajustes | | ✅ Em andamento | | |
| Validação com usuários | | | ⏳ Planejado | |
| Documentação (SDS) | | ✅ Concluído | | |
| Relatório Final | | | ✅ Em andamento | |
| Ajustes finais | | | | ⏳ Planejado |

**Legenda:**
- ✅ Concluído
- ⏳ Planejado
- 🔄 Em andamento

---

## 3. VERIFICAÇÃO (CHECK)

### Planejamento

**Imersão realizada?**
✅ SIM
- Identificação clara do problema
- Análise de soluções existentes
- Definição de escopo viável

**Ideação realizada?**
✅ SIM
- Brainstorming de soluções
- Avaliação de alternativas
- Decisão fundamentada

**Prototipação realizada?**
✅ SIM
- Wireframes conceituais
- Protótipo funcional (MVP)
- Arquitetura definida

**Planejamento está ok?**
✅ SIM
- Cronograma realista
- Recursos disponíveis
- Alinhado com objetivos do curso

---

### Realização

**Cronograma realizado?**
✅ SIM (80% concluído até Abril/2026)
- Desenvolvimento conforme planejado
- Pequenos atrasos compensados em seguida
- MVP funcional entregue

**Cronograma atende a realização do projeto?**
✅ SIM
- Tempo suficiente para desenvolvimento
- Margem para ajustes e testes
- Documentação contemplada

---

### Verificação

**Cronograma atende a realização do projeto?**
✅ SIM
- Projeto desenvolvido dentro do prazo
- Qualidade mantida
- Funcionalidades principais implementadas

**Projeto atende a proposta da instituição escolhida?**
✅ SIM
- Auxilia profissional de atividade cultural (marceneiro artesão)
- Promove difusão cultural através da tecnologia
- Democratiza acesso à IA para artesãos

**Houve necessidade de mudança de estratégia?**
✅ SIM

**Mudanças realizadas:**

1. **Simplificação ainda maior da interface:**
   - **Original:** Formulário com todos os campos em uma página
   - **Mudança:** Wizard passo a passo (4 etapas)
   - **Motivo:** Feedback de que formulário único era intimidador

2. **Ajuste na integração com MinIO:**
   - **Original:** URLs internas do Docker
   - **Mudança:** Tradução para localhost nas URLs públicas
   - **Motivo:** Navegador não conseguia acessar URLs internas

3. **Expansão da engine de prompts:**
   - **Original:** Templates básicos
   - **Mudança:** Contextos específicos por tipo/estilo/ambiente
   - **Motivo:** Resultados genéricos não satisfaziam

---

## 4. AÇÃO (ACT)

### AÇÕES PROPOSTAS

Com base nas verificações realizadas, as seguintes ações de melhoria são propostas:

#### Curto Prazo (Próximas 2 semanas)

1. **Validação com Usuários Reais**
   - Testar sistema com 3-5 marceneiros da região
   - Coletar feedback sobre usabilidade
   - Identificar pontos de dificuldade

2. **Ajustes de UX**
   - Aumentar ainda mais o tamanho de botões
   - Adicionar mais tooltips explicativas
   - Melhorar mensagens de erro

3. **Otimização de Custos**
   - Implementar cache de imagens geradas
   - Evitar regenerações desnecessárias

#### Médio Prazo (1-2 meses)

1. **Sistema de Autenticação**
   - Permitir que cada marceneiro tenha conta própria
   - Privacidade de projetos

2. **Exportação PDF**
   - Gerar apresentação com imagem + especificações
   - Facilitar envio ao cliente

3. **Galeria de Exemplos**
   - Mostrar projetos bem-sucedidos
   - Inspirar outros marceneiros

#### Longo Prazo (3-6 meses)

1. **Versão Mobile Nativa**
   - App Android/iOS
   - Maior facilidade de uso

2. **Integração WhatsApp**
   - Enviar projetos direto para clientes
   - Facilitar comunicação

3. **Sistema de Precificação**
   - Sugerir preços baseados em materiais/tamanho
   - Auxiliar na elaboração de orçamentos

---

## REFERÊNCIAS BIBLIOGRÁFICAS

BENYON, David. **Interação humano-computador**. 2.ed. São Paulo: Pearson, 2011.

SEGURAGO, Valquíria Santos. **Projeto de interface com o usuário**. São Paulo: Pearson, 2017.

Camden, Raymond, and Matthews, Andy. **jQuery Mobile Web Development Essentials**. Olton: Packt Publishing, Limited, 2012.

OPENAI. **DALL-E 3 API Documentation**. Disponível em: https://platform.openai.com/docs/guides/images. Acesso em: 15 mar. 2026.

PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software: uma abordagem profissional**. 8. ed. Porto Alegre: AMGH, 2016.

SOMMERVILLE, Ian. **Engenharia de software**. 10. ed. São Paulo: Pearson, 2018.

ORGANIZAÇÃO DAS NAÇÕES UNIDAS. **Agenda 2030 para o Desenvolvimento Sustentável**. Disponível em: https://brasil.un.org/pt-br/sdgs. Acesso em: 10 mar. 2026.

---

**Data de conclusão do Template PDCA:** 03 de abril de 2026
**Assinatura:** Diego Jaques Tinoco
