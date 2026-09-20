# Projeto — Fine-Tuning LoRA com Antes/Depois Documentado

## Contexto

Módulo de fechamento da trilha. Prompt engineering e RAG resolvem a maioria dos casos, mas
formato muito específico ou domínio muito nichado às vezes precisa de fine-tuning. LoRA torna
isso barato o suficiente pra rodar numa GPU gratuita do Colab — mas o valor do exercício está em
provar, com número, que o fine-tuning melhorou algo, não em "eu rodei um notebook".

## Tarefa

1. Escolha um formato/domínio bem específico pra ensinar ao modelo (ex.: responder sempre num
   formato JSON rígido específico seu, um tom de voz muito particular, classificar textos numa
   taxonomia customizada que o modelo base não conhece — a escolha é sua, mas precisa ser
   verificável objetivamente se o modelo aprendeu ou não).
2. Monte um dataset pequeno e específico: 50-100 exemplos (par entrada/saída) nesse formato,
   documentando como você criou/coletou esses exemplos.
3. Separe um **conjunto de teste** (10-15 exemplos que NÃO entram no treino) pra avaliação
   antes/depois.
4. Rode o modelo BASE (sem fine-tuning) no conjunto de teste e registre o resultado (quantos
   exemplos ele acerta o formato/domínio esperado).
5. Faça fine-tuning LoRA (via Unsloth, no Google Colab gratuito com GPU) de um modelo pequeno
   open-weight no seu dataset de treino.
6. Rode o modelo FINE-TUNADO no MESMO conjunto de teste e registre o resultado.
7. Compare os dois resultados com um número (ex.: "modelo base acertou 3/12, fine-tunado
   acertou 10/12") — se não melhorou, documente honestamente por quê (dataset pequeno demais?
   tarefa mal definida? hiperparâmetro errado?). Um resultado negativo bem documentado e
   analisado vale tanto quanto um positivo aqui.

## Restrições técnicas

- Google Colab gratuito (GPU T4 grátis) + Unsloth. Modelo pequeno open-weight (ex.: Llama
  3.2 1B/3B, Qwen 2.5 0.5B/1.5B — algo que caiba na GPU gratuita).
- Entrega inclui o notebook (`.ipynb`) usado no Colab, exportado com as saídas/resultados
  visíveis (não só o código sem rodar).
- Dataset de treino e teste versionados como arquivos (JSON/CSV) na entrega.

## Entrega

PR neste repo com `modulos/12-fine-tuning-lora-peft-unsloth/projeto/entrega/`, incluindo o
notebook exportado com saídas, `dataset_treino.json`, `dataset_teste.json`, e um README com a
tabela antes/depois e a análise honesta do resultado. Depois rode a skill
`revisar-modulo-agient`.
