# Projeto — Agente de Aprovação de Reembolso com LangGraph

## Contexto

Um agente que decide sozinho e age direto é assustador quando a ação é irreversível (enviar
dinheiro, cancelar um pedido, deletar um registro). Na prática, você quer um fluxo com
ramificação (o caso é simples? complexo?), um ponto de pausa pra aprovação humana antes da ação
irreversível, e visibilidade de onde o processo está enquanto roda. LangGraph modela isso como
grafo de estado explícito, não como uma cadeia de `if` escondida dentro de um agente.

## Tarefa

Construa (em Python, usando `langgraph`) um grafo que decide aprovação de reembolso:

1. **Nó de análise**: recebe um pedido de reembolso (valor + motivo, pode ser um dict/JSON de
   entrada simples) e classifica como `baixo_risco` (valor abaixo de um limite configurável, ex.
   R$100) ou `alto_risco` (acima do limite, ou motivo contém palavra de alerta tipo "fraude",
   "duplicado").
2. **Aresta condicional**: `baixo_risco` vai direto pro nó de aprovação automática.
   `alto_risco` vai pro nó de pausa para aprovação humana.
3. **Checkpoint com pausa humana**: no caminho de alto risco, o grafo **pausa de verdade**
   (usando o mecanismo de interrupt/checkpoint do LangGraph, não um `input()` simples) esperando
   uma decisão externa (`aprovar` ou `rejeitar`) antes de continuar. Documente como retomar a
   execução depois da pausa.
4. **Ciclo controlado**: se o pedido de reembolso vier com dado incompleto (falta valor ou
   motivo), o grafo volta pro nó de análise pedindo o dado faltante, com um contador de
   tentativas — depois de 3 tentativas sem sucesso, sai do ciclo e marca como `precisa_revisao_manual`
   em vez de loopar pra sempre.
5. **Streaming de estado**: rode o grafo em modo streaming e imprima no terminal, em tempo real,
   qual nó está executando e o estado relevante naquele ponto (não precisa ser bonito, precisa
   ser visível).

## Restrições técnicas

- Python 3.11+, `langgraph` (e `langchain-core` se precisar de tipos). Não precisa de LLM de
  verdade nessa entrega — a classificação de risco pode ser lógica determinística (regras), o
  foco do módulo é o grafo/orquestração, não geração de texto. Se quiser usar LLM pra
  classificar o motivo, tudo bem, mas documente e use Ollama local ou deixe mockável — sem
  custo obrigatório pra rodar os testes.
- Dependências em `requirements.txt`.
- Roda com um único comando documentado no README.

## Entrega

PR neste repo com o código em `modulos/08-langgraph-orquestracao/projeto/entrega/`, incluindo
código, `requirements.txt`, testes (`pytest`) cobrindo pelo menos: caminho baixo risco (auto
aprovado), caminho alto risco (pausa e retoma com aprovação/rejeição), e o ciclo de dado
incompleto saindo após 3 tentativas. Depois rode a skill `revisar-modulo-agient`.
