# Critérios de Aceite — Módulo 07

Itens marcados **[OBRIGATÓRIO]** bloqueiam aprovação. Os demais contam como nota, não bloqueiam.

- [ ] **[OBRIGATÓRIO] 3 ferramentas reais funcionando**: busca RAG, consulta a banco, e chamada
  de API externa, todas de fato executáveis (não stub que retorna dado fixo).
- [ ] **[OBRIGATÓRIO] Validação de argumento por ferramenta**: schema Pydantic valida o
  argumento antes da execução; argumento inválido vira observação de erro, não exceção crua.
- [ ] **[OBRIGATÓRIO] Limite de iteração respeitado**: teste prova que o agente para após o
  limite configurado, mesmo forçando um cenário que tenderia a loop.
- [ ] **[OBRIGATÓRIO] Guardrail de allowlist testado**: existe teste que tenta usar ferramenta
  fora da allowlist e confirma que foi bloqueada E logada como bloqueio (não silenciosa).
- [ ] **[OBRIGATÓRIO] Log estruturado por passo**: cada ciclo pensamento/ação/observação fica
  registrado de forma auditável (arquivo ou saída estruturada), não só print solto.
- [ ] **[OBRIGATÓRIO] Falha de ferramenta não derruba o processo**: teste simula exceção numa
  tool e confirma que o agente trata como observação e continua.
- [ ] Exemplo de execução end-to-end real anexado como evidência (log completo de uma tarefa
  resolvida usando pelo menos 2 das 3 ferramentas).
- [ ] README explica a arquitetura (framework escolhido, por quê) e como rodar do zero.
