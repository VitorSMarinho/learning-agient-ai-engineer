# Critérios de Aceite — Módulo 08

Itens **1-6 são obrigatórios** (bloqueiam aprovação se não atendidos). Itens 7-8 são qualidade.

- [ ] **(obrigatório) Grafo de estado real**: existe um `StateGraph` (ou equivalente) do
  LangGraph com estado tipado, não uma sequência de funções chamadas na mão disfarçada de grafo.
- [ ] **(obrigatório) Aresta condicional funcional**: existe pelo menos uma aresta condicional
  que de fato desvia o fluxo (`baixo_risco` vs `alto_risco`) com base no estado, testável com
  um caso de cada.
- [ ] **(obrigatório) Pausa/checkpoint real**: o caminho de alto risco pausa a execução usando o
  mecanismo de interrupt/checkpoint do LangGraph (não um `input()` bloqueante simples) e é
  possível retomar de fora com uma decisão (`aprovar`/`rejeitar`).
- [ ] **(obrigatório) Ciclo com saída garantida**: o ciclo de dado incompleto tem contador de
  tentativas e sai do loop após o limite, marcando `precisa_revisao_manual` — testado com um
  caso que força as 3 tentativas.
- [ ] **(obrigatório) Testes cobrindo os 3 caminhos**: `pytest` roda e cobre baixo risco, alto
  risco com pausa+retomada, e ciclo saindo por limite de tentativas.
- [ ] **(obrigatório) Sem custo obrigatório pra rodar os testes**: testes não dependem de
  chamada de API paga real (se usar LLM em algum ponto, a chamada é mockável/opcional).
- [ ] Streaming de estado visível no terminal durante a execução (não precisa de teste
  automatizado pra isso, é ok verificar manualmente).
- [ ] README da entrega documenta como rodar, incluindo como retomar um grafo pausado.

**Veredito**: `aprovado` se os 6 itens obrigatórios atendem; `precisa_ajuste` caso contrário.
