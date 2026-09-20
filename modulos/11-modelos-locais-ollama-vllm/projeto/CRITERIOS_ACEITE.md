# Critérios de Aceite — Módulo 11

Itens **1-5 são obrigatórios**. Item 6 é qualidade/extra.

- [ ] **(obrigatório) Rota FastAPI real**: `POST /gerar` (ou nome equivalente) com request/response
  tipados por Pydantic, chamando o Ollama local por trás.
- [ ] **(obrigatório) Benchmark com 3 níveis de concorrência**: script mede tokens/segundo e
  latência em pelo menos 3 níveis de concorrência distintos, com números reais (não estimados).
- [ ] **(obrigatório) Resultados documentados**: README da entrega tem tabela com hardware,
  modelo usado, e os números dos 3 níveis de concorrência.
- [ ] **(obrigatório) Testes sem exigir Ollama rodando**: `pytest` passa com o cliente Ollama
  mockado — não é obrigatório ter Ollama instalado pra rodar a suite de testes.
- [ ] **(obrigatório) Config por variável de ambiente**: URL/modelo do Ollama configurável via
  env var, não hardcoded.
- [ ] Comparação opcional com API paga (latência/qualidade) — não bloqueia aprovação se ausente.

**Veredito**: `aprovado` se os 5 itens obrigatórios atendem; `precisa_ajuste` caso contrário.
