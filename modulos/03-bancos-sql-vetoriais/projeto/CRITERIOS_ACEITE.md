# Critérios de Aceite — Módulo 03

Itens marcados **[OBRIGATÓRIO]** bloqueiam aprovação. Os demais contam como nota, não bloqueiam.

- [ ] **[OBRIGATÓRIO] Schema correto**: tabela `documentos` com coluna relacional de categoria
  E coluna `vector` de embedding, schema em `schema.sql` versionado.
- [ ] **[OBRIGATÓRIO] Embeddings reais**: pelo menos 20 documentos com embedding gerado por um
  modelo de verdade (local ou via API) — não vetor aleatório/mockado no dado de carga.
- [ ] **[OBRIGATÓRIO] Índice HNSW criado**: `schema.sql` ou script de setup cria o índice
  vetorial explicitamente, não depende de scan sequencial.
- [ ] **[OBRIGATÓRIO] Busca híbrida funcional**: `busca_hibrida()` combina filtro relacional
  (`WHERE categoria = ...`) com ordenação por similaridade vetorial na mesma consulta.
- [ ] **[OBRIGATÓRIO] Comparação prova o filtro**: `comparar.py` demonstra, com saída real,
  que resultados mudam com/sem filtro de categoria — não é só afirmação no README.
- [ ] **[OBRIGATÓRIO] Sem segredo hardcoded**: string de conexão do banco e eventual API key de
  embedding vêm de variável de ambiente.
- [ ] Testes de integração cobrem a função de busca contra um banco real (Docker), documentados
  no README de como rodar.
- [ ] README documenta setup do zero (subir Postgres+pgvector, rodar carga, rodar busca).
- [ ] Código legível: separação clara entre schema/carga/busca.
