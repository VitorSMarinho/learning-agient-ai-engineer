# Módulo 07 — Sistemas de Agentes de IA

## Objetivo

Diferença entre "chamar um LLM com tools" e um sistema de agente de verdade: loop de
raciocínio, memória de estado entre passos, limite de iteração, e principalmente contenção —
o agente não pode ter permissão pra fazer mais do que a tarefa exige.

## Pré-requisitos

Módulos 01-02.

## Fundamentos

**Padrão ReAct.** Em vez do modelo responder direto, ReAct intercala "pensamento" (raciocínio em
texto sobre o que fazer) com "ação" (chamar uma ferramenta) e "observação" (o resultado da
ferramenta), repetindo esse ciclo até ter o suficiente pra responder. Isso torna o processo de
decisão do agente auditável — você lê o log e entende POR QUE ele chamou cada ferramenta, em vez
de só ver o resultado final caindo do nada.

**Tool-calling: schema, validação, falha.** Uma ferramenta bem definida tem um schema explícito
de argumento (o modelo só pode chamar com os parâmetros certos, no tipo certo). Validar esse
argumento ANTES de executar a ferramenta evita que um argumento malformado vire exceção crua no
meio da execução — vira, em vez disso, uma observação de erro que o próprio agente pode
reagir e tentar de outro jeito. Ferramenta que falha (rede caiu, API retornou erro) também
precisa virar observação tratada, nunca um crash do processo inteiro.

**Memória de curto prazo vs. persistente.** A janela de contexto do modelo é a memória de curto
prazo — tudo que ele "lembra" nessa execução, e que desaparece quando a conversa/execução
termina. Memória persistente (banco, arquivo, vector store) sobrevive entre execuções — é o que
permite um agente "lembrar" de uma interação de ontem. Confundir as duas é um erro comum: parte
do estado que devia persistir fica preso só na janela de contexto e se perde.

**Limites de segurança.** Um agente com ferramenta poderosa e sem limite é um risco, não uma
feature. Allowlist de ferramentas define explicitamente o que o agente PODE usar nessa execução
(nunca "todas as ferramentas disponíveis" por padrão). Limite de iteração evita loop
infinito/custo infinito. Human-in-the-loop pra ação irreversível (deletar, pagar, publicar)
significa que o agente propõe e um humano aprova antes da ação acontecer de verdade — contenção
que não depende do modelo "se comportar bem" sozinho.

## Documentação de referência

- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
  — artigo técnico oficial sobre quando um agente é a ferramenta certa (e quando é
  complexidade desnecessária) e como estruturar um bem.
- [Anthropic — Tool use, documentação oficial](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)
  — schema de ferramenta, formato de chamada e resposta, exatamente o que o projeto deste módulo
  usa.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
  — paper original do padrão ReAct; leia a seção de exemplos pra ver o formato
  pensamento/ação/observação na prática.
- [LangGraph — documentação oficial](https://langchain-ai.github.io/langgraph/) — se optar por
  implementar o loop do agente com um framework em vez de escrever o loop manualmente.

## O que você vai construir

Um agente com no mínimo 3 ferramentas reais (ex.: buscar na base RAG do Módulo 04, consultar o
banco do Módulo 03, chamar uma API pública gratuita), loop de raciocínio com limite de
iterações, log estruturado de cada passo (pensamento → ação → observação), e um guardrail
explícito que bloqueia uma ação fora da allowlist.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-multi-agent-systems-architect`.
