# Critérios de Aceite — Módulo 01

Rubrica usada pelo subagente `python-reviewer` ao revisar o PR. Cada item é avaliado como
atende / não atende, com comentário.

- [ ] **Sem segredo hardcoded**: nenhuma API key em texto plano em código ou em arquivo
  versionado; existe `.env.example` sem valor real.
- [ ] **Config por variável de ambiente**: chave/URL/modelo configuráveis via env var, não
  constante fixa no código.
- [ ] **Saída validada por schema**: resposta do LLM passa por um modelo Pydantic (ou
  equivalente) antes de ser usada; resposta fora do schema é tratada como erro recuperável, não
  derruba o programa.
- [ ] **Retry com backoff**: existe lógica de nova tentativa em falha de rede/timeout/rate
  limit, com espera crescente entre tentativas (mínimo 3 tentativas).
- [ ] **Tratamento de erro real**: erros de I/O (arquivo não encontrado, linha malformada) não
  derrubam o processo inteiro — o programa reporta e segue ou falha com mensagem clara.
- [ ] **Testes sem dependência de rede**: `pytest` roda e passa sem chamar a API real (chamada
  ao LLM é mockada); cobre pelo menos o caminho feliz e um caminho de erro (resposta inválida
  do modelo, ou falha simulada de API).
- [ ] **Script de avaliação funcional**: `avaliar.py` roda, lê `gabarito.csv` + resultados, e
  imprime uma métrica de acurácia coerente com os dados.
- [ ] **Reprodutibilidade**: README do projeto documenta o comando exato pra rodar do zero
  (instalar dependências, configurar `.env`, executar CLI, executar avaliação).
- [ ] **Código legível**: nomes de função/variável claros, sem duplicação óbvia, sem
  complexidade desnecessária pra o escopo do exercício.

**Veredito final**: `aprovado` se todos os itens obrigatórios (os 6 primeiros) atendem;
`precisa_ajuste` caso contrário, com a lista específica do que falta.
