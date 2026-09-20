# Critérios de Aceite — Módulo 04

Itens marcados **[OBRIGATÓRIO]** bloqueiam aprovação. Os demais contam como nota, não bloqueiam.

- [ ] **[OBRIGATÓRIO] Chunking documentado**: estratégia de corte explicada no README com a
  razão da escolha, não só "usei o default da lib".
- [ ] **[OBRIGATÓRIO] Indexação funcional**: chunks indexados de forma recuperável (banco
  vetorial rodando, busca retorna candidatos reais pra uma query de teste).
- [ ] **[OBRIGATÓRIO] Resposta cita fonte**: toda resposta gerada indica explicitamente qual
  documento/chunk fundamentou a afirmação — sem citação não atende este critério.
- [ ] **[OBRIGATÓRIO] Conjunto de avaliação real**: mínimo 10 perguntas com gabarito de qual
  fonte deveria ser citada, versionado no repo.
- [ ] **[OBRIGATÓRIO] Script de avaliação roda e reporta métrica**: `avaliar_rag.py` executa as
  10 perguntas e imprime taxa de citação correta (não é manual/visual).
- [ ] Re-ranking implementado e documentado (mesmo que simples).
- [ ] README explica os failure modes observados durante os testes (ex.: alucinação, contexto
  ignorado) — mostra que você testou de verdade, não só o caminho feliz.
- [ ] Código legível: ingestão, retrieval e geração em módulos separados, não um script único
  enorme.
