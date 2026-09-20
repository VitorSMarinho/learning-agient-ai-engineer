# Projeto — O Mesmo Agente em LangChain e LlamaIndex

## Contexto

Escolher framework por marketing/hype é como escolher ferramenta sem medir. Este projeto força
uma comparação com dado real: mesmo caso de uso, implementado duas vezes, medido.

## Tarefa

1. Defina UM caso de uso de agente de perguntas-e-respostas sobre a base do Módulo 04 que exija
   pelo menos decomposição de pergunta complexa (ex.: "compare o que o documento X diz sobre A
   com o que o documento Y diz sobre B" — não dá pra responder com uma recuperação só).
2. Implemente esse agente em **LangChain** (LCEL + tool-calling sobre o retriever).
3. Implemente o **mesmo** agente em **LlamaIndex** (query engine/agent nativo da lib).
4. Rode as mesmas 5 perguntas de teste nas duas implementações, medindo: tempo de resposta
   (latência), número de linhas de código de cada implementação, e se a resposta ficou correta
   (comparado a um gabarito seu).
5. Escreva `COMPARACAO.md` com uma tabela desses números e uma recomendação — pra que tipo de
   cenário cada framework faz mais sentido, baseado no que você mediu, não em opinião genérica.

## Restrições técnicas

LangChain + LlamaIndex (as duas libs, é o ponto do módulo). LLM local ou via API.

## Entrega

PR neste repo com `modulos/05-rag-agents-langchain-llamaindex/projeto/entrega/`: pasta
`langchain/` e pasta `llamaindex/` com as duas implementações, `perguntas_teste.json`,
`COMPARACAO.md`, e um script `benchmark.py` que roda as duas e gera os números. Depois rode a
skill `revisar-modulo-agient`.
