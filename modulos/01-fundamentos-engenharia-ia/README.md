# Módulo 01 — Fundamentos da Engenharia de IA

## Objetivo

Sair do "notebook que chama uma API de LLM" pra código de produção: configuração segura,
tratamento de erro, saída validada e testável. Engenharia de IA começa aqui, antes de RAG ou
agentes — se a fundação (config, retry, validação, teste) não é sólida, nada que vem depois
segura.

## Pré-requisitos

Python intermediário (funções, módulos, venv). Não precisa saber nada de IA ainda.

## Conceitos-chave

- Gestão de configuração e segredo (nunca hardcoded, sempre variável de ambiente)
- Chamada de LLM como dependência externa não confiável: timeout, retry com backoff, rate limit
- Saída estruturada e validada (não confiar em texto livre de um LLM sem parsing/validação)
- Testes que não dependem de bater na API real toda hora (mock da chamada)
- Avaliação básica: como medir se as respostas do modelo estão "boas o suficiente"

## Recursos gratuitos

- [Anthropic API — Getting Started](https://docs.claude.com/en/docs/get-started) (docs oficiais, tem free tier de créditos pra testar)
- [Ollama](https://ollama.com) — roda modelo local de graça, sem precisar de API key, alternativa pra quem quer zero custo
- [Prompt Engineering Guide](https://www.promptingguide.ai/) — referência livre e completa
- [Pydantic — Validators](https://docs.pydantic.dev/latest/concepts/validators/) (docs oficiais, output estruturado)
- [Real Python — Python Environment Variables](https://realpython.com/python-dotenv/)
- [tenacity](https://tenacity.readthedocs.io/) — lib de retry com backoff, docs oficiais
- [The Twelve-Factor App — Config](https://12factor.net/config) — por que config nunca é hardcoded
- [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) (curso curto, gratuito)

## O que você vai construir

Um CLI em Python que classifica o sentimento de um lote de textos usando um LLM (Claude API,
OpenAI, ou Ollama local — sua escolha, desde que documentada), com engenharia de verdade por
trás: sem chave hardcoded, retry com backoff em falha de API, saída validada por Pydantic
(nunca texto solto), testes que rodam sem depender da API real, e um script de avaliação que
compara a saída do modelo contra um pequeno gabarito rotulado à mão.

Ver `projeto/ENUNCIADO.md` pro enunciado completo e `projeto/CRITERIOS_ACEITE.md` pra rubrica.

## Como é avaliado

Ao abrir o PR com a solução neste repo, rode a skill `revisar-modulo-agient`. Ela
aciona o subagente `python-reviewer` sobre o diff, usando `projeto/CRITERIOS_ACEITE.md` como
rubrica, posta o resultado como comentário no PR e grava `reviews/01-fundamentos-engenharia-ia.json`.
