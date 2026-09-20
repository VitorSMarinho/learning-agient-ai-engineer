# Projeto — API do Classificador de Sentimento

## Contexto

Um script que roda no seu terminal não serve outro sistema. Pra qualquer time (ou você mesmo,
depois) usar o classificador do Módulo 01, ele precisa virar um serviço HTTP com contrato
estável: tipos claros na entrada/saída, erro previsível, documentação que não fica desatualizada
sozinha.

## Tarefa

1. Crie uma API FastAPI que expõe o classificador de sentimento do Módulo 01 (pode reaproveitar
   `llm_client.py`/`classificar_sentimento` da entrega anterior, ou reescrever).
2. Rota `POST /classificar` recebendo `{"texto": "..."}` (Pydantic `BaseModel` de request) e
   devolvendo `{"classificacao": "...", "justificativa": "..."}` (Pydantic `BaseModel` de
   response). Corpo inválido (campo faltando, tipo errado) deve retornar `422` automático do
   FastAPI, sem código extra seu.
3. Use `Depends` pra injetar a configuração do provedor de LLM (não instancie o cliente direto
   dentro da rota) — isso deve permitir trocar o provedor real por um fake nos testes sem
   monkeypatch de módulo inteiro.
4. Trate erro do provedor (falha de API, resposta inválida) retornando `502` com corpo JSON
   `{"detail": "..."}` explicando o problema — nunca um 500 genérico nem stack trace pro cliente.
5. Adicione rota `GET /health` retornando `200 {"status": "ok"}`, sem depender do provedor de
   LLM (não pode falhar só porque a API key não está configurada).
6. Escreva testes com `TestClient` (ou `httpx.AsyncClient`) cobrindo: caminho feliz, corpo
   inválido (422), falha do provedor (502), e o `/health`. Nenhum teste bate na API real.

## Restrições técnicas

FastAPI + Pydantic v2. Pode usar qualquer provedor de LLM (Anthropic, OpenAI, Ollama local) —
documente a escolha. Python 3.11+.

## Entrega

PR neste repo com o código em `modulos/02-python-moderno-fastapi/projeto/entrega/` (código da
API, `requirements.txt`, testes, README de como rodar `uvicorn` localmente e exemplo de `curl`).
Depois rode a skill `revisar-modulo-agient`.
