# Critérios de Aceite — Módulo 09

Itens **1-6 são obrigatórios**. Item 7 é qualidade.

- [ ] **(obrigatório) 3 papéis distintos**: existem Pesquisador, Redator e Supervisor como
  unidades separadas (funções/classes/agentes claramente distintos), cada um com responsabilidade
  única — não é um agente só fingindo 3 papéis num único prompt gigante.
- [ ] **(obrigatório) Handoff explícito e testável**: o Redator recebe os pontos do Pesquisador
  (não a pergunta original direto), e isso é verificável no código/teste — o dado que passa de
  um agente pro outro é claro.
- [ ] **(obrigatório) Supervisor decide de verdade**: existe lógica real de aprovação (critérios
  checáveis, não um `return True` fixo) e um caminho de `pedir_revisao` que de fato volta pro
  Redator com limite de 2 rodadas.
- [ ] **(obrigatório) Log estruturado do handoff**: cada passagem entre agentes é registrada
  (quem/quando/o quê) de forma estruturada (lista de dicts, JSON, etc.), não só `print()`.
- [ ] **(obrigatório) Falha injetada não derruba o sistema**: existe um teste que força o Redator
  a falhar, e o sistema captura isso, registra no log, e retorna erro estruturado — sem
  stack trace vazando pro usuário final e sem o processo travar/crashar sem tratamento.
- [ ] **(obrigatório) Testes rodam sem custo obrigatório**: `pytest` passa sem depender de
  chamada de API paga real (mock se usar LLM).
- [ ] Exemplo de log real de uma execução incluído na entrega (`exemplo_log.json` ou similar).

**Veredito**: `aprovado` se os 6 itens obrigatórios atendem; `precisa_ajuste` caso contrário.
