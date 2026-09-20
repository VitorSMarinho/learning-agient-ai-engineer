# Módulo 11 — Modelos Locais: Ollama e vLLM

## Objetivo

Nem toda aplicação pode (ou deve) depender de API externa: custo, latência, dado sensível que
não pode sair da rede. Este módulo ensina a rodar e servir modelo open-weight localmente, com
throughput de verdade, não só "rodei um chat no terminal".

## Pré-requisitos

Módulo 02.

## Conceitos-chave

- Diferença entre "rodar localmente pra testar" (Ollama) e "servir em produção com throughput"
  (vLLM, batching contínuo)
- Quantização (GGUF, AWQ) e o trade-off qualidade vs uso de memória/VRAM
- Escolha de modelo open-weight pro hardware disponível (parâmetros vs RAM/VRAM)
- Benchmark real: tokens/segundo, latência de primeiro token, sob carga concorrente

## Recursos gratuitos

- [Ollama — documentação oficial](https://ollama.com) (README/docs do repositório)
- [vLLM — documentação oficial](https://docs.vllm.ai/)
- [Hugging Face — Quantization documentação oficial](https://huggingface.co/docs/transformers/quantization)

## O que você vai construir

Um modelo open-weight rodando local via Ollama, exposto atrás de uma rota FastAPI (reaproveita
o Módulo 02), com um script de benchmark que mede tokens/segundo e latência sob 3 níveis de
concorrência, documentando o hardware usado e os resultados.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-ai-engineer`.
