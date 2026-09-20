# Módulo 12 — Fine-Tuning: LoRA, PEFT, Unsloth

## Objetivo

Módulo de fechamento da trilha: quando prompt engineering e RAG não bastam (formato muito
específico, domínio muito nichado, custo de contexto longo repetido), fine-tuning eficiente é
a próxima ferramenta. Aqui você faz de verdade, não só lê sobre.

## Pré-requisitos

Módulos 01, 02, 11 (já sabe servir modelo local).

## Conceitos-chave

- Por que fine-tuning completo é caro/raro e LoRA/QLoRA resolve 90% dos casos com fração do
  custo
- PEFT (Parameter-Efficient Fine-Tuning): o que exatamente é treinado vs congelado
- Preparação de dataset de fine-tuning (formato, tamanho mínimo viável, qualidade > quantidade)
- Avaliação pré/pós fine-tuning no mesmo conjunto de teste — prova objetiva de que melhorou

## Recursos gratuitos

- [Hugging Face — PEFT documentação oficial](https://huggingface.co/docs/peft/index)
- [Unsloth — documentação e notebooks oficiais gratuitos](https://docs.unsloth.ai/) (fine-tuning otimizado, roda em GPU gratuita do Google Colab)
- [Hugging Face — LoRA conceitos (documentação oficial)](https://huggingface.co/docs/peft/conceptual_guides/lora)
- [Google Colab](https://colab.research.google.com/) (GPU gratuita pra rodar o treino)

## O que você vai construir

Fine-tuning LoRA de um modelo pequeno open-weight (via Unsloth, no Colab gratuito) num dataset
pequeno e específico que você mesmo monta (ex.: 50-100 exemplos de um formato de resposta bem
definido), com avaliação antes/depois no mesmo conjunto de teste documentando a melhora (ou
honestamente documentando que não melhorou, e por quê).

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-ai-engineer`.
