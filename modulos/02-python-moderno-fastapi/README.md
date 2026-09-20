# Módulo 02 — Python Moderno e FastAPI

## Objetivo

Sair do script solto e construir um serviço web de verdade: tipagem estrita, validação de
entrada/saída, dependência injetada, documentação automática. FastAPI é o padrão de fato pra
servir modelos/agentes de IA em produção.

## Pré-requisitos

Módulo 01 (fundamentos: config, retry, validação).

## Conceitos-chave

- Type hints modernos (`|`, `TypedDict`, `Protocol`) e por que eles importam pra manutenção
- Pydantic v2 como camada de validação de request/response
- Dependency Injection do FastAPI (`Depends`) pra config, auth, conexão de banco
- Async/await: quando FastAPI ganha (I/O bound) e quando não ajuda (CPU bound)
- Documentação automática (OpenAPI/Swagger) como contrato vivo da API

## Recursos gratuitos

- [FastAPI — documentação oficial](https://fastapi.tiangolo.com/) (tutorial completo, gratuito)
- [Pydantic v2 — documentação oficial](https://docs.pydantic.dev/latest/)
- [Real Python — FastAPI](https://realpython.com/fastapi-python-web-apis/)
- [Real Python — Async IO in Python](https://realpython.com/async-io-python/)
- [mypy — documentação oficial](https://mypy.readthedocs.io/) (checagem de tipo estática)

## O que você vai construir

Uma API FastAPI que expõe o classificador de sentimento do Módulo 01 como serviço HTTP: rota
`POST /classificar` com request/response tipados por Pydantic, injeção de dependência pra
configuração do provedor de LLM, tratamento de erro HTTP correto (4xx pra input inválido, 5xx
pra falha do provedor), e testes com `TestClient`.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`fastapi-reviewer`.
