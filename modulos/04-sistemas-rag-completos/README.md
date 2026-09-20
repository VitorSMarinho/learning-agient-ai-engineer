# Módulo 04 — Sistemas RAG completos

## Objetivo

RAG de verdade não é "jogar tudo num vector store e perguntar pro LLM". É um pipeline com
decisões em cada etapa: como você corta o documento, o que você indexa, o que você recupera,
e como você prova que a resposta ficou melhor. Este módulo cobre o pipeline inteiro.

## Pré-requisitos

Módulo 03 (banco vetorial já rodando).

## Conceitos-chave

- Estratégias de chunking (fixo, semântico, por estrutura de documento) e o efeito no recall
- Recuperação: top-k, re-ranking, filtros de metadado
- Geração aumentada: como montar o prompt final sem estourar contexto nem "afogar" o modelo
- Avaliação de RAG: faithfulness, relevância de contexto, correção de resposta — não é só "vibe"
- Failure modes clássicos: alucinação mesmo com contexto certo, contexto certo mas ignorado

## Recursos gratuitos

- [LangChain — RAG documentação oficial](https://python.langchain.com/docs/tutorials/rag/)
- [LlamaIndex — documentação oficial](https://docs.llamaindex.ai/en/stable/)
- [Anthropic — Contextual Retrieval (artigo técnico)](https://www.anthropic.com/news/contextual-retrieval)
- [Ragas — framework de avaliação de RAG, documentação oficial](https://docs.ragas.io/)
- [DeepLearning.AI — Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) (curso curto gratuito)

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
