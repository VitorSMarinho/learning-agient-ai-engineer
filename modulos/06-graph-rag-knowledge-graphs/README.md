# Módulo 06 — Graph RAG e Knowledge Graphs

## Objetivo

Busca vetorial não capta relação estrutural ("quem depende de quem", "o que causa o quê"). Grafo
de conhecimento captura isso. Este módulo ensina quando vale a pena adicionar essa camada e como
construir uma sem virar projeto de doutorado.

## Pré-requisitos

Módulo 04.

## Conceitos-chave

- Extração de entidades e relações a partir de texto não estruturado (com LLM)
- Modelagem de grafo: nó, aresta, propriedade
- Quando Graph RAG bate RAG vetorial puro (pergunta multi-hop, "conecte A com C via B") e quando
  é overkill
- Consulta híbrida: grafo pra estrutura, vetor pra similaridade semântica

## Recursos gratuitos

- [Neo4j — GraphAcademy (cursos gratuitos oficiais)](https://graphacademy.neo4j.com/)
- [Microsoft Research — GraphRAG (paper + repo oficial)](https://microsoft.github.io/graphrag/)
- [LangChain — Graph documentação oficial](https://python.langchain.com/docs/how_to/graph_constructing/)
- [Neo4j — documentação oficial](https://neo4j.com/docs/) (tier free/community disponível)

## O que você vai construir

Extração automática de entidades/relações de um conjunto pequeno de documentos (ex.: notas
técnicas de um projeto seu), carga num grafo (Neo4j community local via Docker, ou networkx pra
uma versão mais leve), e uma consulta multi-hop que RAG vetorial puro erraria, com comparação
lado a lado documentada.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-rag-pipeline-engineer`.
