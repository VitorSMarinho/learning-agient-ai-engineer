# Projeto — Time Pesquisador + Redator + Supervisor

## Contexto

Um agente generalista tentando pesquisar E escrever bem ao mesmo tempo costuma fazer as duas
coisas de forma mediana. Especializar por papel, com um supervisor decidindo quando o resultado
está bom o suficiente, costuma produzir resultado melhor — mas só se o "handoff" entre agentes
for desenhado com cuidado sobre o que passa adiante e o que não passa.

## Tarefa

Construa um sistema com **3 agentes** colaborando numa tarefa de "responder uma pergunta com
uma resposta redigida e fundamentada":

1. **Agente Pesquisador**: recebe uma pergunta, produz uma lista de pontos/fatos relevantes
   (pode ser busca simulada numa base de texto local sua, ou uma chamada real de LLM/busca — sua
   escolha, desde que documentada e sem custo obrigatório pra rodar os testes).
2. **Agente Redator**: recebe os pontos do Pesquisador (não a pergunta original diretamente —
   force a passagem pelo handoff) e produz um rascunho de resposta em texto corrido.
3. **Agente Supervisor**: recebe o rascunho, avalia contra critérios simples (tamanho mínimo,
   cobre os pontos do pesquisador, não contém frases vazias tipo "é importante notar que"), e
   decide: `aprovar` (entrega o rascunho) ou `pedir_revisao` (manda de volta pro Redator com
   feedback específico, no máximo 2 rodadas de revisão antes de entregar o que tiver mesmo
   assim, marcado como `entregue_sem_aprovacao_total`).
4. **Log estruturado do handoff**: cada passagem de um agente pro outro é registrada (quem
   enviou, quem recebeu, timestamp, o payload) numa lista/arquivo, não só print solto.
5. **Teste de falha injetada**: crie um cenário de teste onde o Agente Redator "quebra"
   (levanta exceção ou devolve lixo) de propósito, e prove que o sistema não trava nem derruba o
   processo inteiro — ele detecta a falha, registra no log, e retorna um erro estruturado em vez
   de crashar sem explicação.

## Restrições técnicas

- Python 3.11+. Pode usar LangGraph, um framework de multi-agente, ou implementar a orquestração
  você mesmo com classes/funções — o que importa é a topologia (supervisor coordenando,
  handoff explícito), não a biblioteca.
- Se usar LLM real em algum agente, ofereça um modo mockável pros testes (sem custo obrigatório
  pra rodar `pytest`).
- Dependências em `requirements.txt`.

## Entrega

PR neste repo com o código em `modulos/09-multi-agent-systems/projeto/entrega/`, testes cobrindo
o caminho feliz (pesquisa → redação → aprovação) e o caminho de falha injetada, e um exemplo do
log de handoff gerado numa execução real (pode ser um arquivo `exemplo_log.json` na entrega).
Depois rode a skill `revisar-modulo-agient`.
