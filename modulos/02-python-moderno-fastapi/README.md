# Módulo 02 — Python Moderno e FastAPI

## Objetivo

Sair do script solto e construir um serviço web de verdade: tipagem estrita, validação de
entrada/saída, dependência injetada, documentação automática. FastAPI é o padrão de fato pra
servir modelos/agentes de IA em produção.

## Pré-requisitos

Módulo 01 (fundamentos: config, retry, validação).

## Fundamentos

**Type hints modernos (`|`, `TypedDict`, `Protocol`).** Tipo em Python é opcional em runtime,
mas isso não o torna decorativo. `int | None` em vez de `Optional[int]`, `TypedDict` pra
dicionário com forma conhecida, `Protocol` pra "qualquer objeto com este método" sem herança
forçada — isso é o que permite o editor e o `mypy` pegarem um erro de tipo antes de rodar, e é
o que faz um FastAPI gerar documentação automática correta. Sem tipo, a API vira uma caixa preta
que só se sabe o formato lendo o código-fonte.

**Pydantic v2 como camada de validação.** FastAPI não valida nada sozinho — quem valida é o
Pydantic. Um `BaseModel` declara a forma exata do request e do response; se o cliente manda
campo errado ou tipo errado, o Pydantic rejeita antes do seu código de negócio rodar. Isso
elimina uma classe inteira de bug ("e se vier `None` onde eu esperava string?") na borda da
aplicação, não espalhado em `if` por todo o código.

**Dependency Injection via `Depends`.** Em vez de cada rota instanciar sua própria config,
conexão de banco ou verificação de auth, você declara essas coisas como dependências que o
FastAPI resolve e injeta. Isso separa "o que a rota faz" de "o que ela precisa pra funcionar" —
e torna trivial substituir uma dependência real por uma fake em teste, sem mockar biblioteca
nenhuma.

**Async/await: quando ganha e quando não ajuda.** `async def` só destrava concorrência real
quando o gargalo é espera de I/O (chamada de rede, disco, banco) — o event loop aproveita esse
tempo de espera pra atender outra requisição. Se o gargalo é CPU (processamento pesado), async
não ajuda nada, porque a CPU continua ocupada do mesmo jeito; nesse caso o ganho vem de
paralelismo real (multiprocessing), não de `async`.

**Documentação automática como contrato vivo.** FastAPI gera OpenAPI/Swagger a partir dos
próprios type hints e modelos Pydantic — a documentação não pode ficar desatualizada porque ela
É o código, não um comentário ao lado dele. Isso é diferente de escrever doc manual que
descreve uma API e confiar que alguém vai lembrar de atualizar os dois lugares.

## Documentação de referência

- [FastAPI — documentação oficial](https://fastapi.tiangolo.com/) — leia especialmente as
  seções de "Path Operations", "Dependencies" e "Testing" (`TestClient`), que são exatamente o
  que o projeto deste módulo usa.
- [Pydantic v2 — documentação oficial](https://docs.pydantic.dev/latest/) — foque em "Models" e
  "Validators", a base de como o request/response tipado funciona.
- [mypy — documentação oficial](https://mypy.readthedocs.io/) — checagem de tipo estática; útil
  pra pegar erro de tipo antes mesmo de rodar o teste.
- [Real Python — Async IO in Python](https://realpython.com/async-io-python/) — explica o
  modelo de concorrência por trás do `async`/`await` com mais profundidade que a doc oficial do
  FastAPI sozinha.

## O que você vai construir

Uma API FastAPI que expõe o classificador de sentimento do Módulo 01 como serviço HTTP: rota
`POST /classificar` com request/response tipados por Pydantic, injeção de dependência pra
configuração do provedor de LLM, tratamento de erro HTTP correto (4xx pra input inválido, 5xx
pra falha do provedor), e testes com `TestClient`.

## Como é avaliado

Ao abrir o PR com a solução neste repo, rode a skill `revisar-modulo-agient`. Ela
aciona o subagente `fastapi-reviewer` sobre o diff, usando `projeto/CRITERIOS_ACEITE.md`
como rubrica, posta o resultado como comentário no PR e grava
`reviews/02-python-moderno-fastapi.json`.
