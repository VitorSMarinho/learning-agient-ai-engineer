# Módulo 05 — RAG Agents: LangChain vs LlamaIndex

## Objetivo

RAG estático (uma pergunta, uma recuperação, uma resposta) não resolve pergunta complexa. RAG
agêntico decide sozinho se precisa buscar de novo, com outra query, em outra fonte. Este módulo
compara os dois frameworks dominantes construindo o mesmo agente nos dois.

## Pré-requisitos

Módulo 04.

## Conceitos-chave

- Query transformation e decomposição de pergunta complexa em sub-perguntas
- Tool-calling aplicado à recuperação (o agente escolhe a fonte/ferramenta certa)
- Roteamento entre múltiplos índices/fontes
- Onde LangChain (LCEL, mais controle explícito) e LlamaIndex (abstrações de índice/query engine
  mais prontas) cada um vence, na prática, não em marketing

## Recursos gratuitos

- [LangChain — Agents documentação oficial](https://python.langchain.com/docs/concepts/agents/)
- [LlamaIndex — Agents documentação oficial](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
- [LangGraph — documentação oficial](https://langchain-ai.github.io/langgraph/) (usado como runtime de agente em ambos os ecossistemas hoje)

## O que você vai construir

O mesmo agente de perguntas-e-respostas sobre a base do Módulo 04, implementado duas vezes: uma
em LangChain, outra em LlamaIndex. Documento comparativo curto (`COMPARACAO.md`) com latência,
linhas de código, e qual framework você recomendaria pra qual cenário — com dado, não opinião.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-rag-pipeline-engineer`.
