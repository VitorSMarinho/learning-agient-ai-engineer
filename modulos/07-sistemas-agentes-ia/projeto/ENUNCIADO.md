# Projeto — Agente com Ferramentas, Log e Guardrail

## Contexto

"Chamar um LLM com tools" e "sistema de agente" não são a mesma coisa. O que separa os dois é
contenção: limite de iteração, log de cada decisão, e uma allowlist que o agente não pode
furar — mesmo que o modelo "decida" tentar.

## Tarefa

1. Implemente um agente com padrão ReAct (pensamento → ação → observação, repetido) com no
   mínimo 3 ferramentas reais: (a) busca na base RAG do Módulo 04, (b) consulta ao banco do
   Módulo 03, (c) chamada a uma API pública gratuita (ex.: uma API de clima, câmbio, ou similar
   sem necessidade de chave paga).
2. Cada chamada de ferramenta passa por validação de argumento (schema Pydantic) antes de
   executar — argumento inválido vira observação de erro pro agente, não exceção não tratada.
3. Implemente limite de iterações (ex.: máximo 8 ciclos pensamento-ação) — se estourar, o agente
   para e retorna o que tem, não entra em loop infinito.
4. Implemente uma **allowlist explícita** de ferramentas permitidas por execução, e um teste que
   prova que uma tentativa de usar ferramenta fora da allowlist é bloqueada (não silenciosamente
   ignorada — precisa logar/retornar que foi bloqueada).
5. Log estruturado (JSON ou similar) de cada passo: o que o agente "pensou", qual ferramenta
   chamou, com qual argumento, e qual foi a observação — dá pra auditar a execução inteira
   depois, sem re-rodar.
6. Teste de falha de ferramenta: simule uma ferramenta que lança exceção e prove que o agente
   trata isso como observação de erro e continua (não crasha o processo inteiro).

## Restrições técnicas

LangGraph, ou implementação direta do loop ReAct sem framework — documente a escolha. LLM local
ou via API.

## Entrega

PR neste repo com `modulos/07-sistemas-agentes-ia/projeto/entrega/`: código do agente, as 3
ferramentas, testes (incluindo o teste de guardrail e o de falha de ferramenta), README
explicando a arquitetura e como rodar um exemplo end-to-end com log completo anexado como
evidência (`exemplo_execucao.log` ou similar). Depois rode a skill `revisar-modulo-agient`.
