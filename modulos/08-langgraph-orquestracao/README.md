# Módulo 08 — LangGraph: orquestração real

## Objetivo

Agente único vira frágil rápido quando a tarefa tem ramificação, retry condicional, ou precisa
de aprovação humana no meio. LangGraph modela isso como grafo de estado explícito em vez de
cadeia linear escondida numa lib de agente.

## Pré-requisitos

Módulo 07.

## Conceitos-chave

- Grafo de estado: nó, aresta condicional, estado compartilhado tipado
- Checkpointing e retomada de execução (pausar, esperar aprovação humana, continuar)
- Ciclos controlados (loop com condição de saída explícita, não implícita)
- Streaming de estado intermediário pra UI acompanhar o progresso em tempo real

## Recursos gratuitos

- [LangGraph — documentação oficial](https://langchain-ai.github.io/langgraph/)
- [LangGraph — tutoriais oficiais](https://langchain-ai.github.io/langgraph/tutorials/)
- [LangChain Academy — Introduction to LangGraph (curso gratuito oficial)](https://academy.langchain.com/courses/intro-to-langgraph)

## O que você vai construir

Reescreva o agente do Módulo 07 como grafo LangGraph com pelo menos um nó condicional (decide
caminho A ou B conforme resultado anterior), um checkpoint com pausa pra aprovação humana antes
de uma ação "irreversível" simulada, e streaming do estado pro terminal em tempo real.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-multi-agent-systems-architect`.
