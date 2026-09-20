# Módulo 09 — Multi-Agent Systems

## Objetivo

Um agente generalista faz tudo mal. Múltiplos agentes especialistas coordenados fazem cada
parte bem — se a coordenação for desenhada certo. Este módulo cobre topologia (quem fala com
quem), não só "múltiplos prompts".

## Pré-requisitos

Módulo 08.

## Conceitos-chave

- Topologias: supervisor/worker, pipeline sequencial, peer-to-peer
- Protocolo de handoff entre agentes (o que passa de um pro outro, e o que NÃO passa)
- Falha em cascata: um agente errado derrubando o sistema inteiro, e como conter isso
- Observabilidade multi-agente: rastrear qual agente fez o quê, quando algo dá errado

## Recursos gratuitos

- [Anthropic — Building Effective Agents (seção de multi-agente)](https://www.anthropic.com/research/building-effective-agents)
- [LangGraph — Multi-agent documentação oficial](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
- [AutoGen — documentação oficial (Microsoft)](https://microsoft.github.io/autogen/)

## O que você vai construir

Um sistema com 2-3 agentes especialistas coordenados por um supervisor (ex.: um agente
pesquisa/recupera, outro escreve, o supervisor decide quando está bom o suficiente pra entregar),
com log estruturado do handoff entre eles e um teste que injeta falha proposital num agente pra
provar que o sistema não trava/quebra silenciosamente.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-multi-agent-systems-architect`.
