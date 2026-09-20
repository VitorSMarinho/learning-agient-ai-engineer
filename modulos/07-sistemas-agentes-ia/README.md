# Módulo 07 — Sistemas de Agentes de IA

## Objetivo

Diferença entre "chamar um LLM com tools" e um sistema de agente de verdade: loop de
raciocínio, memória de estado entre passos, limite de iteração, e principalmente contenção —
o agente não pode ter permissão pra fazer mais do que a tarefa exige.

## Pré-requisitos

Módulos 01-02.

## Conceitos-chave

- Padrão ReAct (raciocínio + ação intercalados) e variações
- Tool-calling: schema de ferramenta, validação de argumento, tratamento de falha de execução
- Memória de curto prazo (janela de contexto) vs memória persistente entre sessões
- Limites de segurança: allowlist de ferramentas, limite de iteração, human-in-the-loop pra ação
  irreversível

## Recursos gratuitos

- [Anthropic — Building Effective Agents (artigo técnico oficial)](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Tool use documentação oficial](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)
- [ReAct: Synergizing Reasoning and Acting in Language Models (paper original, arXiv)](https://arxiv.org/abs/2210.03629)
- [LangGraph — documentação oficial](https://langchain-ai.github.io/langgraph/)

## O que você vai construir

Um agente com no mínimo 3 ferramentas reais (ex.: buscar na base RAG do Módulo 04, consultar o
banco do Módulo 03, chamar uma API pública gratuita), loop de raciocínio com limite de
iterações, log estruturado de cada passo (pensamento → ação → observação), e um guardrail
explícito que bloqueia uma ação fora da allowlist.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-multi-agent-systems-architect`.
