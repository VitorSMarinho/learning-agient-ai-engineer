# Projeto — Graph RAG contra RAG Vetorial Puro

## Contexto

A prova de que grafo vale a pena não é teórica — é uma pergunta que RAG vetorial puro erra e
Graph RAG acerta, lado a lado, no mesmo conjunto de dados.

## Tarefa

1. Escolha um conjunto pequeno de documentos com relações explícitas entre entidades (ex.:
   notas técnicas de um projeto seu descrevendo "serviço A depende do serviço B", "módulo X foi
   substituído por Y" — relações reais, não inventadas pra caber no exercício).
2. Extraia entidades e relações desses documentos usando um LLM (prompt estruturado pedindo
   `{entidade_origem, relacao, entidade_destino}`), com validação da saída (schema, igual ao
   padrão do Módulo 01).
3. Carregue essas relações num grafo (Neo4j Community local via Docker, ou `networkx` se quiser
   uma versão mais leve sem infra extra — documente a escolha).
4. Formule pelo menos 3 perguntas multi-hop que exigem navegar 2+ relações pra responder (ex.:
   "o que depende, mesmo que indiretamente, do serviço A?").
5. Responda essas 3 perguntas de duas formas: (a) usando só o RAG vetorial do Módulo 04 sobre os
   mesmos documentos, (b) usando consulta ao grafo. Documente em `COMPARACAO.md` onde o vetor
   puro erra ou fica incompleto e o grafo acerta.

## Restrições técnicas

Neo4j Community (Docker) ou `networkx`. Extração de entidade/relação via LLM local ou API.

## Entrega

PR neste repo com `modulos/06-graph-rag-knowledge-graphs/projeto/entrega/`: script de extração,
script de carga no grafo, script de consulta multi-hop, `COMPARACAO.md` com as 3 perguntas e as
duas respostas lado a lado. Depois rode a skill `revisar-modulo-agient`.
