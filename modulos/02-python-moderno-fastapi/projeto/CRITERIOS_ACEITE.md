# Critérios de Aceite — Módulo 02

Itens marcados **[OBRIGATÓRIO]** bloqueiam aprovação. Os demais contam como nota, não bloqueiam.

- [ ] **[OBRIGATÓRIO] Request/response tipados**: `POST /classificar` usa `BaseModel` Pydantic
  tanto pra request quanto pra response — sem `dict` solto ou `Any`.
- [ ] **[OBRIGATÓRIO] Validação automática funciona**: corpo malformado (campo faltando ou tipo
  errado) retorna `422` sem código de validação manual escrito à mão.
- [ ] **[OBRIGATÓRIO] Dependency Injection real**: o cliente/config do provedor de LLM é
  injetado via `Depends`, não instanciado direto dentro da função de rota — deve dar pra
  substituir por um fake em teste via `app.dependency_overrides`.
- [ ] **[OBRIGATÓRIO] Erro do provedor tratado**: falha simulada do LLM retorna `502` com corpo
  JSON explicando o erro, nunca `500`/stack trace vazando pro cliente.
- [ ] **[OBRIGATÓRIO] `/health` não depende do provedor**: responde `200` mesmo sem
  `ANTHROPIC_API_KEY`/equivalente configurada.
- [ ] **[OBRIGATÓRIO] Testes sem rede real**: `TestClient`/`httpx.AsyncClient` cobre caminho
  feliz, 422, 502 e /health; roda sem chamar a API do provedor de verdade.
- [ ] Documentação automática (`/docs`) reflete os schemas corretamente (checável rodando local).
- [ ] README de entrega documenta como rodar `uvicorn` e um exemplo de `curl` funcional.
- [ ] Código legível: rota fina, lógica de negócio fora do handler HTTP.
