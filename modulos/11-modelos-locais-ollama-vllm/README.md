# Módulo 11 — Modelos Locais: Ollama e vLLM

## Objetivo

Nem toda aplicação pode (ou deve) depender de API externa: custo, latência, dado sensível que
não pode sair da rede. Este módulo ensina a rodar e servir modelo open-weight localmente, com
throughput de verdade, não só "rodei um chat no terminal".

## Pré-requisitos

Módulo 02.

## Fundamentos

**Testar local vs servir em produção.** Ollama é otimizado pra "eu quero rodar um modelo agora,
sem configurar nada" — ótimo pra desenvolvimento e teste. vLLM é otimizado pro problema
diferente de "várias requisições simultâneas precisam de resposta rápida" — ele faz *continuous
batching*, que agrupa requisições concorrentes de forma inteligente pra usar a GPU com
eficiência bem maior que processar uma de cada vez. Confundir os dois é comum: alguém testa com
Ollama, gosta da latência, e se surpreende quando o mesmo modelo "trava" com 10 requisições
simultâneas — porque Ollama não foi desenhado pra esse cenário.

**Quantização.** Um modelo treinado em precisão total (FP16/FP32) ocupa muita memória. Quantização
reduz a precisão numérica dos pesos (pra INT8, INT4, etc.) — o modelo fica bem menor e mais
rápido, com alguma perda de qualidade que varia conforme o quanto você reduz. GGUF (formato
usado pelo Ollama/llama.cpp) e AWQ são esquemas de quantização diferentes, com trade-offs
próprios de velocidade vs qualidade vs compatibilidade de hardware. Na prática: quantização é o
que permite rodar um modelo de 7B+ parâmetros numa GPU de consumidor, ou até numa CPU decente.

**Escolha de modelo pro hardware.** O número de parâmetros de um modelo (7B, 13B, 70B) se
traduz quase diretamente em quanta memória ele precisa pra rodar — regra grosseira: ~2GB de
VRAM/RAM por bilhão de parâmetros em FP16, bem menos com quantização agressiva. Escolher um
modelo maior do que seu hardware aguenta não dá erro elegante — trava, ou roda absurdamente
lento trocando memória com disco. Parte do trabalho de engenharia aqui é escolher o maior
modelo que SEU hardware específico realmente sustenta.

**Benchmark real.** "Parece rápido" não é dado. As métricas que importam: tokens por segundo
(throughput sustentado), latência até o primeiro token (importa pra experiência percebida, mesmo
que o throughput total seja bom), e como essas duas mudam sob carga concorrente — um sistema que
é rápido com 1 requisição e degrada terrivelmente com 5 simultâneas tem um problema real de
capacidade, não só uma otimização perdida.

## Documentação de referência

- [Ollama — documentação oficial](https://ollama.com) — foque na seção de modelfile e
  parâmetros de contexto/memória.
- [vLLM — documentação oficial](https://docs.vllm.ai/) — leia especialmente a seção de
  continuous batching, é o conceito central que diferencia vLLM de "só rodar um modelo".
- [Hugging Face — Quantization (documentação oficial)](https://huggingface.co/docs/transformers/quantization) —
  explica GGUF, AWQ, GPTQ e os trade-offs entre eles de forma comparável.

## O que você vai construir

Um modelo open-weight rodando local via Ollama, exposto atrás de uma rota FastAPI (reaproveita
o Módulo 02), com um script de benchmark que mede tokens/segundo e latência sob 3 níveis de
concorrência, documentando o hardware usado e os resultados.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-ai-engineer`.
