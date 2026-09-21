# Módulo 04 — Sistemas RAG completos

## Objetivo

RAG de verdade não é "jogar tudo num vector store e perguntar pro LLM". É um pipeline com
decisões em cada etapa: como você corta o documento, o que você indexa, o que você recupera,
e como você prova que a resposta ficou melhor. Este módulo cobre o pipeline inteiro.

## Pré-requisitos

Módulo 03 (banco vetorial já rodando).

## Fundamentos

**Estratégias de chunking e o efeito no recall.** Cortar documento em pedaço fixo de N
caracteres é o jeito mais simples e o mais ingênuo — ele corta no meio de uma ideia com a mesma
frequência que corta numa fronteira natural. Chunking semântico (cortar onde o significado muda)
ou por estrutura (respeitar seção/parágrafo/heading do documento original) recupera melhor
porque cada pedaço recuperado faz sentido sozinho. O tamanho do chunk também importa: pequeno
demais perde contexto, grande demais dilui a relevância do trecho específico que responde a
pergunta.

**Recuperação: top-k, re-ranking, filtros.** Buscar "os k vetores mais próximos" é só a primeira
passada — k alto demais traz ruído, k baixo demais perde a resposta certa. Re-ranking adiciona
uma segunda passada mais cara (geralmente um modelo especializado) que reordena os candidatos do
top-k por relevância real, não só proximidade vetorial. Filtro de metadado (data, categoria,
permissão) restringe o espaço de busca antes mesmo da comparação vetorial acontecer.

**Geração aumentada: montar o prompt sem afogar o modelo.** Colocar contexto demais no prompt
não é sempre melhor — modelo tem "lost in the middle", tendência a ignorar informação no meio de
um contexto longo mesmo que ela esteja tecnicamente lá. O trabalho de engenharia é escolher o
contexto mais relevante possível dentro de um orçamento de tokens, não simplesmente empilhar
tudo que a busca retornou.

**Avaliação de RAG: além da vibe.** "A resposta parece boa" não escala e não é reproduzível.
Faithfulness mede se a resposta é sustentada pelo contexto recuperado (não inventada).
Relevância de contexto mede se o que foi recuperado realmente tem a ver com a pergunta.
Correção de resposta mede se a resposta final está certa. São três métricas distintas porque um
sistema pode falhar em qualquer uma delas independentemente das outras duas.

**Failure modes clássicos.** Alucinação mesmo com contexto certo acontece quando o modelo ignora
o contexto fornecido e responde do seu conhecimento paramétrico (errado ou desatualizado).
Contexto certo mas ignorado acontece quando a informação está no prompt mas o modelo não a usa
(geralmente por estar mal posicionada ou soterrada em ruído). Diagnosticar qual dos dois está
acontecendo muda completamente o que você conserta.

## Documentação de referência

- [LangChain — RAG documentação oficial](https://python.langchain.com/docs/tutorials/rag/) —
  tutorial ponta a ponta do pipeline que este módulo pede pra construir.
- [LlamaIndex — documentação oficial](https://docs.llamaindex.ai/en/stable/) — abstrações de
  índice/query engine prontas; útil pra comparar com a implementação mais manual via LangChain.
- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) —
  artigo técnico sobre como melhorar chunking/recuperação anexando contexto extra a cada chunk
  antes de indexar.
- [Ragas — documentação oficial](https://docs.ragas.io/) — framework de avaliação que implementa
  faithfulness/relevância/correção como métricas calculáveis, não só conceito.
- [OpenAI — RAG e busca de embeddings, guia oficial](https://platform.openai.com/docs/guides/embeddings)
  — se optar por embeddings da OpenAI em vez de Anthropic/local, essa é a referência de geração
  de embedding e uso em busca.

## O que você vai construir

Um pipeline RAG completo sobre uma base de documentos real (ex.: a própria documentação de um
projeto seu, ou um conjunto de PDFs públicos): ingestão + chunking documentado, indexação no
banco do Módulo 03, recuperação com re-ranking simples, geração com citação de fonte, e um
script de avaliação com pelo menos 10 perguntas/gabarito medindo se a resposta cita a fonte
certa.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-rag-pipeline-engineer`.
