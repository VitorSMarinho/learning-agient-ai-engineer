# Módulo 09 — Multi-Agent Systems

## Objetivo

Um agente generalista faz tudo mal. Múltiplos agentes especialistas coordenados fazem cada
parte bem — se a coordenação for desenhada certo. Este módulo cobre topologia (quem fala com
quem), não só "múltiplos prompts".

## Pré-requisitos

Módulo 08.

## Fundamentos

**Topologias.** Não existe "o jeito certo" de conectar múltiplos agentes — existem formatos com
trade-offs diferentes. Supervisor/worker é um agente central que decide qual especialista chamar
e quando parar — bom quando a tarefa tem uma ordem clara de decisão. Pipeline sequencial é
A→B→C fixo, sem decisão de roteamento — mais simples, mais previsível, menos flexível.
Peer-to-peer é agentes se comunicando entre si sem um coordenador central — mais flexível, mais
difícil de debugar quando algo sai errado. Escolher a topologia errada pro problema é a causa
mais comum de sistema multi-agente que "parece mágico até você tentar debugar".

**Protocolo de handoff.** Quando o Agente A termina sua parte e passa pro Agente B, o que
exatamente atravessa essa fronteira? Se for "todo o histórico de conversa do A", o B fica
sobrecarregado de contexto irrelevante. Se for "só a resposta final do A", o B perde nuance
importante. Handoff bem desenhado é explícito sobre o contrato: que campos de estado passam,
em que formato, e — igualmente importante — o que fica de fora de propósito.

**Falha em cascata.** Num sistema de agente único, uma falha é um erro. Num sistema
multi-agente, uma falha de um agente pode virar input ruim pro próximo, que produz output ruim
pro seguinte — o erro se propaga e amplifica em vez de ficar contido. Conter isso significa: cada
agente valida o que recebe antes de agir sobre ele, e o sistema tem um jeito de detectar "isso
não está convergindo" e parar, em vez de deixar a cascata rodar até o fim.

**Observabilidade multi-agente.** Quando um sistema de um agente só erra, você olha um log.
Quando um sistema de três agentes erra, a pergunta muda pra "qual dos três, com qual input,
decidiu o quê, e em que ordem?". Sem log estruturado por agente (não um log genérico
misturado), debugar isso é tentativa e erro às cegas.

## Documentação de referência

- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) —
  a fonte primária sobre quando (e quando NÃO) usar múltiplos agentes em vez de um agente com
  mais ferramentas.
- [LangGraph — Multi-agent (documentação oficial)](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) —
  como implementar supervisor/worker e handoff de estado na prática com LangGraph.
- [AutoGen — documentação oficial (Microsoft)](https://microsoft.github.io/autogen/) — referência
  de uma abordagem diferente (conversação entre agentes peer-to-peer), útil pra comparar com a
  topologia supervisor que você vai implementar.

## O que você vai construir

Um sistema com 2-3 agentes especialistas coordenados por um supervisor (ex.: um agente
pesquisa/recupera, outro escreve, o supervisor decide quando está bom o suficiente pra entregar),
com log estruturado do handoff entre eles e um teste que injeta falha proposital num agente pra
provar que o sistema não trava/quebra silenciosamente.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-multi-agent-systems-architect`.
