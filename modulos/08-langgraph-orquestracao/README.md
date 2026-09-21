# Módulo 08 — LangGraph: orquestração real

## Objetivo

Agente único vira frágil rápido quando a tarefa tem ramificação, retry condicional, ou precisa
de aprovação humana no meio. LangGraph modela isso como grafo de estado explícito em vez de
cadeia linear escondida numa lib de agente.

## Pré-requisitos

Módulo 07.

## Fundamentos

**Grafo de estado, não cadeia linear.** Uma chain tradicional é uma sequência fixa: passo 1,
passo 2, passo 3. Um grafo de estado é outra coisa — cada nó é uma função que recebe o estado
atual e devolve uma atualização dele, e as arestas decidem pra qual nó ir a seguir com base
nesse estado. A diferença prática: numa chain, ramificação é `if` espalhado no código chamador;
num grafo, ramificação é uma aresta condicional de primeira classe, visível na topologia. Isso
importa porque tarefa real quase nunca é linear — ela bifurca, repete, e às vezes precisa parar
no meio.

**Checkpointing e retomada.** Se o seu agente decide fazer algo caro ou irreversível (mandar
email, cobrar cartão, deletar dado), você não quer que isso aconteça sem revisão. Checkpointing
é a capacidade de o grafo pausar num ponto específico, persistir o estado, esperar uma decisão
externa (aprovação humana, por exemplo), e continuar de onde parou — sem re-executar tudo desde
o início. Sem isso, "aprovação humana no meio do fluxo" vira gambiarra de polling ou webhook
solto.

**Ciclos controlados.** Um grafo pode ter um nó que aponta de volta pra um nó anterior — isso é
um ciclo, e é exatamente o que você precisa pra "tentar de novo com plano diferente" ou "refinar
até bater um critério". O risco óbvio é loop infinito. Um ciclo controlado tem uma condição de
saída explícita e visível na definição do grafo (ex.: contador de tentativas, campo de estado
`aprovado: bool`) — não escondida num `while True` com `break` perdido no meio da função.

**Streaming de estado intermediário.** Numa execução que leva segundos (ou minutos, com
múltiplas chamadas de LLM encadeadas), esperar o resultado final em silêncio é uma péssima
experiência — e pior, torna difícil debugar onde travou. Streaming de estado é expor cada
atualização de nó conforme ela acontece, não só o resultado final. Pra você, agora, isso vira
log em tempo real no terminal; em produção, vira progresso numa UI.

## Documentação de referência

- [LangGraph — documentação oficial](https://langchain-ai.github.io/langgraph/) — comece pela
  seção de conceitos (`StateGraph`, nós, arestas) antes de ir direto pro código.
- [LangGraph — tutoriais oficiais](https://langchain-ai.github.io/langgraph/tutorials/) — tem
  exemplo de human-in-the-loop (checkpointing) que é literalmente o que este módulo pede.
- [LangChain Academy — Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) —
  curso gratuito oficial, cobre grafo de estado, checkpoint e streaming em sequência didática.

## O que você vai construir

Reescreva o agente do Módulo 07 como grafo LangGraph com pelo menos um nó condicional (decide
caminho A ou B conforme resultado anterior), um checkpoint com pausa pra aprovação humana antes
de uma ação "irreversível" simulada, e streaming do estado pro terminal em tempo real.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-multi-agent-systems-architect`.
