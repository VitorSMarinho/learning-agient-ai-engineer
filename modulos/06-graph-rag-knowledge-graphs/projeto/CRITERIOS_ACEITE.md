# Critérios de Aceite — Módulo 06

Itens marcados **[OBRIGATÓRIO]** bloqueiam aprovação. Os demais contam como nota, não bloqueiam.

- [ ] **[OBRIGATÓRIO] Extração validada**: saída do LLM pra entidade/relação passa por
  validação de schema antes de virar aresta no grafo (não confia em JSON solto sem checar).
- [ ] **[OBRIGATÓRIO] Grafo carregado de verdade**: relações extraídas estão persistidas num
  grafo consultável (Neo4j ou networkx), não só numa lista em memória descartada.
- [ ] **[OBRIGATÓRIO] Perguntas genuinamente multi-hop**: as 3 perguntas de teste exigem
  navegar 2+ relações — uma pergunta respondível com 1 hop não conta.
- [ ] **[OBRIGATÓRIO] Comparação lado a lado real**: as mesmas 3 perguntas foram de fato
  rodadas contra RAG vetorial puro E contra o grafo, com as respostas registradas em
  `COMPARACAO.md` (não é uma alegação, é a saída real das duas execuções).
- [ ] Consulta ao grafo implementada em script reutilizável (não só via console interativo do
  Neo4j).
- [ ] README documenta setup (Docker do Neo4j, ou instalação do networkx) e como rodar do zero.
