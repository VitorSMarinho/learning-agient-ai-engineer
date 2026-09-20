# Critérios de Aceite — Módulo 05

Itens marcados **[OBRIGATÓRIO]** bloqueiam aprovação. Os demais contam como nota, não bloqueiam.

- [ ] **[OBRIGATÓRIO] Mesmo caso de uso nas duas libs**: implementação LangChain e LlamaIndex
  resolvem exatamente o mesmo problema (mesmas perguntas de teste funcionam nas duas).
- [ ] **[OBRIGATÓRIO] Exige decomposição real**: pelo menos uma das perguntas de teste não é
  respondível com uma única recuperação simples — precisa de sub-perguntas/múltiplas buscas.
  Documente por quê no `COMPARACAO.md`.
- [ ] **[OBRIGATÓRIO] Benchmark roda de verdade**: `benchmark.py` executa as duas
  implementações e produz os números (latência, linhas de código) — não são números estimados
  de cabeça.
- [ ] **[OBRIGATÓRIO] `COMPARACAO.md` com dado, não opinião**: cada afirmação de "framework X é
  melhor pra Y" precisa apontar pro número que sustenta ela.
- [ ] Gabarito de correção das 5 perguntas de teste versionado, usado no benchmark.
- [ ] Código das duas implementações organizado em pastas separadas, sem mistura.
- [ ] README explica setup de cada uma (dependências podem divergir entre as duas libs).
