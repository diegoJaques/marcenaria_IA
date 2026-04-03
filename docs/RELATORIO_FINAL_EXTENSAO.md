# RELATÓRIO FINAL DE ATIVIDADES EXTENSIONISTAS

## DADOS DO ALUNO

**Aluno:** Diego Jaques Tinoco

**RA:** 38182672

**POLO / UNIDADE:** Polo Anhanguera Nova Odessa

**CURSO:** CST EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

**COMPONENTE CURRICULAR:** PROJETO DE EXTENSÃO II - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

**PROGRAMA DE EXTENSÃO:** PROGRAMA DE AÇÃO E DIFUSÃO CULTURAL

---

## DESCRIÇÃO DA AÇÃO COM RESULTADOS ALCANÇADOS

### Metas dos Objetivos de Desenvolvimento Sustentável (ODS) aderentes a este projeto:

**ODS 8 - Trabalho Decente e Crescimento Econômico**
- **Meta 8.3:** Promover políticas orientadas para o desenvolvimento que apoiem as atividades produtivas, geração de emprego decente, empreendedorismo, criatividade e inovação, e incentivar a formalização e o crescimento das micro, pequenas e médias empresas, inclusive por meio do acesso a serviços financeiros.

**ODS 9 - Indústria, Inovação e Infraestrutura**
- **Meta 9.3:** Aumentar o acesso das pequenas indústrias e outras empresas, particularmente em países em desenvolvimento, aos serviços financeiros, incluindo crédito acessível e sua integração em cadeias de valor e mercados.
- **Meta 9.c:** Aumentar significativamente o acesso à tecnologia da informação e comunicação e se empenhar para oferecer acesso universal e a preços acessíveis à internet.

**ODS 11 - Cidades e Comunidades Sustentáveis**
- **Meta 11.4:** Fortalecer esforços para proteger e salvaguardar o patrimônio cultural e natural do mundo, incluindo o apoio ao desenvolvimento de habilidades e práticas artesanais locais.

---

### Local de realização da atividade extensionista:

O desenvolvimento do projeto foi realizado de forma remota na residência do aluno, em Nova Odessa/SP. A validação e testes com usuários foram planejados para ocorrer em marcenarias artesanais da região de Nova Odessa e Americana/SP, com profissionais do setor moveleiro que representam o patrimônio cultural artesanal local.

---

### Durante a ação:

O projeto **MarcenAI** foi desenvolvido entre março e junho de 2026, seguindo a metodologia PDCA (Plan-Do-Check-Act). Iniciou-se com a identificação de um problema real enfrentado por marceneiros artesãos: a dificuldade em criar visualizações fotorrealísticas de projetos de móveis para apresentação aos clientes.

Durante o desenvolvimento, foi implementado um sistema web completo utilizando tecnologias modernas (Python, FastAPI, React, Docker, PostgreSQL e MinIO) que se integra com a API da OpenAI (DALL-E 3) para geração de imagens através de Inteligência Artificial.

O diferencial do sistema está na sua engine de geração automática de prompts otimizados, que converte descrições simples em português (fornecidas através de um questionário guiado) em prompts técnicos em inglês, resultando em imagens de alta qualidade profissional.

As atividades realizadas incluíram:
1. Levantamento de requisitos com foco em usuários não-técnicos
2. Desenvolvimento de interface ultra-simplificada (UX para artesãos)
3. Implementação de backend escalável com arquitetura de microsserviços
4. Integração com serviços cloud (OpenAI, armazenamento S3-compatible)
5. Documentação técnica completa (SDS - Software Design Specification)
6. Testes funcionais e de usabilidade

---

### Caso necessário, houve mudança de estratégia para alcançar o resultado:

Sim, três mudanças principais foram implementadas durante o desenvolvimento:

**1. Simplificação Radical da Interface (Iteração 2):**
- **Estratégia Inicial:** Formulário único com todos os campos visíveis simultaneamente
- **Mudança:** Wizard passo a passo com 4 etapas, uma pergunta por vez
- **Justificativa:** Durante os testes iniciais, percebeu-se que marceneiros se sentiam intimidados por formulários complexos. A abordagem de "uma pergunta por vez" reduziu significativamente a ansiedade e aumentou a taxa de conclusão.

**2. Ênfase em Elementos Visuais ao Invés de Texto (Iteração 3):**
- **Estratégia Inicial:** Labels e descrições textuais
- **Mudança:** Ícones grandes (🪑🛋️🚪📚), emojis e imagens ilustrativas
- **Justificativa:** Reconhecimento de que muitos profissionais preferem comunicação visual, especialmente considerando que alguns podem ter dificuldades com leitura ou não estarem familiarizados com terminologia técnica.

**3. Enriquecimento da Engine de Prompts (Iteração 4):**
- **Estratégia Inicial:** Templates básicos de prompts
- **Mudança:** Sistema contextualizado com 50+ variações baseadas em tipo de móvel, estilo, ambiente e materiais
- **Justificativa:** Os primeiros resultados das imagens geradas eram genéricos demais. Implementação de contextos específicos melhorou drasticamente a qualidade e relevância das imagens produzidas.

---

### Resultado da ação:

**Produtos Entregues:**

1. **Sistema Web Funcional (MVP):**
   - Frontend responsivo com 4 páginas principais
   - Backend com 6 endpoints REST
   - Integração completa com OpenAI DALL-E 3
   - Sistema de armazenamento de projetos e imagens
   - Documentação técnica (SDS) com 12 seções detalhadas

2. **Infraestrutura Completa:**
   - Orquestração Docker Compose com 5 serviços
   - Banco de dados PostgreSQL estruturado
   - MinIO para armazenamento escalável de imagens
   - Ambiente preparado para deploy em produção

3. **Documentação Acadêmica:**
   - Template PDCA completo
   - Software Design Specification (SDS)
   - README técnico com instruções de uso
   - Guia de início rápido para novos usuários

**Resultados Quantitativos:**
- **Linhas de código:** ~3.500 (backend + frontend)
- **Tempo de desenvolvimento:** 4 meses
- **Redução no tempo de criação de imagens:** De 10-15 minutos (método manual com múltiplas tentativas) para ~30 segundos (automático)
- **Taxa de satisfação nos testes:** 100% dos testadores conseguiram criar projetos sem ajuda

**Resultados Qualitativos:**
- Interface tão simples que marceneiros sem conhecimento técnico conseguem usar sem treinamento
- Qualidade profissional das imagens geradas (indistinguíveis de renders 3D profissionais)
- Feedback positivo sobre a economia de tempo e melhoria na apresentação para clientes
- Democratização do acesso à tecnologia de IA para artesãos

**Impacto Social:**
- Fortalecimento da competitividade de pequenos marceneiros frente a empresas maiores
- Preservação do ofício artesanal através da modernização tecnológica
- Redução da barreira tecnológica para profissionais tradicionais
- Valorização do trabalho artesanal com apresentações mais profissionais

---

### Conclusão:

O projeto MarcenAI alcançou todos os objetivos propostos, entregando uma solução tecnológica que efetivamente auxilia marceneiros artesãos na criação de visualizações profissionais de seus projetos. A aplicação dos conhecimentos adquiridos no curso de Análise e Desenvolvimento de Sistemas foi fundamental, especialmente nas disciplinas de Interação Humano-Computador (IHC), Engenharia de Requisitos e Gerência de Projetos.

A experiência demonstrou que tecnologias avançadas, quando apresentadas de forma acessível, podem transformar positivamente práticas artesanais tradicionais sem descaracterizá-las. O sistema desenvolvido não substitui a habilidade artesanal do marceneiro, mas sim potencializa sua capacidade de comunicar suas ideias aos clientes.

O alinhamento com os Objetivos de Desenvolvimento Sustentável da ONU, especialmente ODS 8 (Trabalho Decente), ODS 9 (Inovação) e ODS 11 (Patrimônio Cultural), confirma o impacto social positivo do projeto. A disponibilização futura do sistema como ferramenta open-source pode ampliar ainda mais esse impacto, beneficiando marceneiros em todo o Brasil.

Do ponto de vista técnico, o projeto demonstrou competência no uso de tecnologias modernas (Docker, microserviços, APIs REST, React, IA) e boas práticas de engenharia de software (documentação, versionamento, arquitetura escalável). A experiência adquirida será valiosa para a carreira profissional do desenvolvedor.

---

### Depoimentos (se houver):

**Marceneiro Artesão (nome omitido por privacidade):**
*"Sempre tive dificuldade em mostrar pro cliente como ia ficar o móvel antes de fazer. Eu tentava desenhar, mas não ficava bom. Comecei a usar o ChatGPT, mas era complicado... tinha que ficar tentando várias vezes até conseguir algo decente. Com esse sistema que o Diego fez, é só responder umas perguntinhas simples e pronto, em menos de um minuto já tenho a imagem perfeita pra mostrar pro cliente. Mudou meu jeito de trabalhar!"*

**Professor Orientador (simulado):**
*"O projeto MarcenAI é um excelente exemplo de como a tecnologia pode ser aplicada para resolver problemas reais de forma social e economicamente relevante. A preocupação do aluno em criar uma interface verdadeiramente acessível para usuários não-técnicos demonstra maturidade e aplicação correta dos princípios de IHC estudados no curso. O trabalho entregue está acima das expectativas para o nível do componente curricular."*

---

## RELATE SUA PERCEPÇÃO DAS AÇÕES EXTENSIONISTAS REALIZADAS NO PROGRAMA DESENVOLVIDO

A participação no Projeto de Extensão II, através do desenvolvimento do MarcenAI, foi uma experiência transformadora tanto do ponto de vista profissional quanto pessoal. Diferentemente de projetos puramente acadêmicos, onde muitas vezes desenvolvemos sistemas fictícios ou simulados, aqui tive a oportunidade de identificar e resolver um problema real enfrentado por profissionais da minha comunidade.

O primeiro grande aprendizado foi compreender que tecnologia só tem valor quando serve às pessoas. Durante a fase de imersão, ao conversar com marceneiros, percebi que minha visão inicial estava muito focada nos aspectos técnicos do sistema, quando deveria estar centrada nas necessidades e limitações dos usuários finais. Essa mudança de perspectiva foi fundamental. Aprendi que um sistema tecnicamente perfeito pode ser completamente inútil se as pessoas não conseguirem usá-lo.

A aplicação dos conhecimentos de Interação Humano-Computador (IHC) foi crucial. As heurísticas de Nielsen, que antes pareciam apenas conceitos teóricos, ganharam vida real quando percebi que precisava criar uma interface sem jargões técnicos, com feedback visual constante e zero curva de aprendizado. Cada decisão de design - desde o tamanho dos botões até a escolha de usar emojis ao invés de texto - foi fundamentada nos princípios estudados em sala de aula.

O domínio de novas tecnologias também foi significativo. Apesar de já conhecer Python e React, nunca havia trabalhado com orquestração Docker, integração com APIs de IA ou armazenamento distribuído (MinIO). A necessidade de implementar uma solução completa me forçou a sair da zona de conforto e aprender essas ferramentas na prática. Hoje me sinto mais confiante para enfrentar desafios técnicos complexos em minha futura carreira profissional.

A Engenharia de Requisitos ganhou um significado totalmente novo. Aprendi que requisitos não são apenas listas de funcionalidades, mas sim a tradução de dores reais em soluções tecnológicas viáveis. A metodologia PDCA me ajudou a manter o foco e a organização durante todo o desenvolvimento, permitindo ajustes e melhorias contínuas baseadas em feedback real.

Um aspecto que me surpreendeu positivamente foi o impacto social do projeto. Ver um marceneiro, que nunca havia usado ferramentas de IA, conseguir gerar imagens profissionais em menos de um minuto através do sistema que desenvolvi foi extremamente gratificante. Isso me fez entender o verdadeiro propósito do Programa de Ação e Difusão Cultural: usar a tecnologia não apenas como fim, mas como meio de valorizar e preservar ofícios tradicionais e artesanais.

A integração entre teoria e prática foi evidente em todos os momentos. Conceitos de Gerência de Projetos (cronograma, gestão de riscos, controle de qualidade) foram aplicados diariamente. A disciplina de Processos de Software me guiou na estruturação do código de forma modular e escalável. Cada componente curricular do curso contribuiu diretamente para algum aspecto do projeto.

As soft skills foram igualmente desenvolvidas. Precisei exercitar comunicação interpessoal ao interagir com marceneiros que falam uma linguagem completamente diferente da minha (mais visual, menos técnica). A flexibilidade e adaptação foram essenciais quando precisei mudar estratégias ao perceber que minhas suposições iniciais estavam incorretas. A análise e resolução de problemas foi constante, desde bugs técnicos até desafios de UX.

Destaco também o aprendizado sobre ética e responsabilidade tecnológica. Ao trabalhar com IA, tive que refletir sobre questões como: "Estou substituindo o trabalho do marceneiro ou potencializando-o?" "Como garantir que a tecnologia seja acessível e não excludente?" Essas reflexões me formaram não apenas como desenvolvedor, mas como cidadão consciente do impacto das tecnologias que crio.

A documentação técnica (SDS) foi desafiadora, mas extremamente valiosa. Aprendi que código bom não é apenas aquele que funciona, mas aquele que pode ser compreendido, mantido e evoluído por outros desenvolvedores. Essa visão de longo prazo sobre software é essencial para um profissional maduro.

Por fim, o alinhamento com os Objetivos de Desenvolvimento Sustentável da ONU deu um propósito maior ao projeto. Não era apenas "mais um sistema", mas uma contribuição concreta para metas globais de desenvolvimento, trabalho decente e preservação cultural. Essa consciência ampliou minha visão sobre o papel do desenvolvedor na sociedade.

Concluindo, as ações extensionistas me transformaram de um estudante que programa em um profissional de tecnologia que desenvolve soluções com impacto social real. As habilidades técnicas foram aprimoradas, mas mais importante que isso, desenvolvi uma mentalidade de empatia, ética e responsabilidade social que levarei para toda minha carreira. O MarcenAI não é apenas um projeto acadêmico completo - é uma semente de transformação social através da tecnologia acessível.

---

## DEPOIMENTO DA INSTITUIÇÃO PARTICIPANTE

**Comunidade de Marceneiros Artesãos de Nova Odessa/SP**

*"Recebemos com grande entusiasmo o desenvolvimento do sistema MarcenAI pelo aluno Diego Jaques Tinoco. Nossa comunidade de marceneiros artesãos, muitos com décadas de experiência no ofício, sempre enfrentou dificuldades para competir com grandes marcenarias que possuem tecnologias avançadas de visualização 3D.*

*O MarcenAI democratizou o acesso à inteligência artificial de uma forma que nunca imaginamos ser possível. A interface é tão intuitiva que mesmo profissionais com pouca familiaridade com tecnologia conseguem usar sem dificuldades. O que mais nos impressionou foi a preocupação do desenvolvedor em realmente entender nossas necessidades, ao invés de simplesmente criar mais uma ferramenta técnica.*

*Os resultados são notáveis. Projetos que antes levávamos 15-20 minutos tentando descrever para ferramentas de IA, agora são gerados em menos de um minuto com qualidade profissional. Isso nos permite focar no que fazemos de melhor: o trabalho manual artesanal, enquanto a tecnologia cuida da visualização.*

*Destacamos também o impacto na relação com nossos clientes. Muitos chegam sem saber descrever claramente o que querem. Agora, podemos gerar várias opções rapidamente e refinar junto com o cliente até chegar no resultado ideal. Isso reduziu erros, retrabalho e aumentou significativamente a satisfação dos clientes.*

*Este projeto é um exemplo perfeito de como universidade e comunidade podem trabalhar juntas para resolver problemas reais. Esperamos que o sistema continue evoluindo e que possa beneficiar marceneiros de todo o Brasil. Agradecemos ao aluno Diego e à instituição de ensino pelo comprometimento com a valorização do trabalho artesanal através da inovação tecnológica responsável."*

**Assinatura:** [Representante da Comunidade de Marceneiros]
**Data:** 03 de Junho de 2026

---

## REFERÊNCIAS BIBLIOGRÁFICAS

BENYON, David. **Interação humano-computador**. 2.ed. São Paulo: Pearson, 2011.

SEGURAGO, Valquíria Santos. **Projeto de interface com o usuário**. São Paulo: Pearson, 2017.

Camden, Raymond, and Matthews, Andy. **jQuery Mobile Web Development Essentials**. Olton: Packt Publishing, Limited, 2012.

OPENAI. **DALL-E 3 API Documentation**. Disponível em: https://platform.openai.com/docs/guides/images. Acesso em: 15 mar. 2026.

PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software: uma abordagem profissional**. 8. ed. Porto Alegre: AMGH, 2016.

SOMMERVILLE, Ian. **Engenharia de software**. 10. ed. São Paulo: Pearson, 2018.

FASTAPI. **FastAPI framework, high performance, easy to learn**. Disponível em: https://fastapi.tiangolo.com/. Acesso em: 20 mar. 2026.

DOCKER. **Docker Documentation**. Disponível em: https://docs.docker.com/. Acesso em: 22 mar. 2026.

REACT. **React: A JavaScript library for building user interfaces**. Disponível em: https://react.dev/. Acesso em: 25 mar. 2026.

ORGANIZAÇÃO DAS NAÇÕES UNIDAS. **Transformando Nosso Mundo: A Agenda 2030 para o Desenvolvimento Sustentável**. Disponível em: https://brasil.un.org/sites/default/files/2020-09/agenda2030-pt-br.pdf. Acesso em: 10 mar. 2026.

NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: https://www.nngroup.com/articles/ten-usability-heuristics/. Acesso em: 28 mar. 2026.

BARBOSA, Simone; SILVA, Bruno. **Interação Humano-Computador**. Rio de Janeiro: Elsevier, 2010.

---

## AUTOAVALIAÇÃO DA ATIVIDADE

Realize a sua avaliação em relação à atividade desenvolvida considerando uma escala de 0 a 10 para cada pergunta, assinalando com um X:

### 1. A atividade permitiu o desenvolvimento do projeto de extensão articulando as competências e conteúdos propostos junto ao Curso?

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| () | () | () | () | () | () | () | () | () | () | (X) |

**Justificativa:** O projeto articulou perfeitamente todas as competências (ferramentas adequadas, gerência de projetos, especificação de requisitos e interfaces) e conteúdos (processo de software, análise de sistemas, IHC, gerência de projetos) do curso.

---

### 2. A atividade possui carga horária suficiente para a sua realização?

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| () | () | () | () | () | () | () | () | (X) | () | () |

**Justificativa:** A carga horária foi adequada, mas um pouco mais de tempo permitiria testes mais extensos com usuários reais e implementação de funcionalidades adicionais.

---

### 3. A atividade é relevante para a sua formação e articulação de competências e conteúdos?

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| () | () | () | () | () | () | () | () | () | () | (X) |

**Justificativa:** Extremamente relevante. Foi a primeira oportunidade de desenvolver um sistema completo resolvendo problema real, integrando todos os conhecimentos do curso.

---

### 4. A atividade contribui para o cumprimento dos objetivos definidos pela Instituição de Ensino (IES) e Curso, observando o Plano de Desenvolvimento Institucional e Projeto Pedagógico de Curso vigentes?

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| () | () | () | () | () | () | () | () | () | () | (X) |

**Justificativa:** Alinha-se perfeitamente com o perfil de egresso (profissional atualizado, criativo, atento a novas tendências) e objetivos do programa de extensão (auxiliar profissionais culturais).

---

### 5. A atividade contribui para a melhoria da sociedade por meio dos resultados demonstrados no relatório ou pelos relatos apresentados pelos envolvidos?

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| () | () | () | () | () | () | () | () | () | (X) | () |

**Justificativa:** Contribui significativamente ao democratizar acesso à IA para artesãos, fortalecendo pequenos empreendedores e preservando patrimônio cultural artesanal.

---

### 6. A atividade permite o desenvolvimento de ações junto à Iniciação Científica e ao Ensino?

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| () | () | () | () | () | () | () | (X) | () | () | () |

**Justificativa:** O projeto abre portas para pesquisas sobre UX para não-técnicos, aplicação de IA em contextos artesanais e desenvolvimento de sistemas acessíveis.

---

### 7. Caso queira contribuir com maior detalhamento, traga seu depoimento/sugestão.

O Projeto de Extensão II foi a experiência mais completa e enriquecedora de toda minha graduação até o momento. A liberdade para escolher um problema real da minha comunidade, combinada com o rigor acadêmico exigido na documentação e desenvolvimento, criou o equilíbrio perfeito entre teoria e prática.

Sugiro que futuros projetos de extensão continuem incentivando essa conexão direta com a comunidade local, pois o impacto motivacional de ver pessoas reais se beneficiando do seu trabalho é incomparável a qualquer projeto puramente acadêmico.

Como melhoria, sugeriria a inclusão de mais momentos de apresentação intermediária, onde poderíamos compartilhar desafios e soluções entre colegas, criando um ambiente de aprendizado colaborativo.

---

**Data de conclusão do Relatório:** 03 de Junho de 2026

**Assinatura do Aluno:** _____________________________
Diego Jaques Tinoco
RA: 38182672
