# Critérios de Aceite — Módulo 12

Itens **1-6 são obrigatórios** (nota: item 4 exige análise honesta, não necessariamente
melhora — um resultado negativo bem documentado ATENDE este critério).

- [ ] **(obrigatório) Dataset de treino específico**: 50-100 exemplos versionados
  (`dataset_treino.json` ou similar), formato/domínio claramente definido no README.
- [ ] **(obrigatório) Conjunto de teste separado**: 10-15 exemplos que não entraram no treino,
  versionados separadamente (`dataset_teste.json`).
- [ ] **(obrigatório) Avaliação do modelo base registrada**: resultado do modelo SEM
  fine-tuning no conjunto de teste, com número (quantos exemplos acertou o formato/domínio
  esperado).
- [ ] **(obrigatório) Avaliação do modelo fine-tunado registrada**: mesmo teste, mesmo
  conjunto, modelo COM fine-tuning LoRA aplicado.
- [ ] **(obrigatório) Comparação com análise honesta**: README compara os dois números e
  explica o resultado — se não melhorou, o porquê é discutido (dataset, hiperparâmetro, tarefa
  mal definida), não só reportado sem análise.
- [ ] **(obrigatório) Notebook com saídas visíveis**: o `.ipynb` da entrega tem as células
  rodadas com output visível (não é só código sem execução).

**Veredito**: `aprovado` se os 6 itens obrigatórios atendem (o critério 5 é sobre honestidade e
qualidade da análise, não sobre o fine-tuning ter "dado certo"); `precisa_ajuste` caso
contrário.
