# Módulo 06 — Graph RAG e Knowledge Graphs

## Objetivo

Busca vetorial não capta relação estrutural ("quem depende de quem", "o que causa o quê"). Grafo
de conhecimento captura isso. Este módulo ensina quando vale a pena adicionar essa camada e como
construir uma sem virar projeto de doutorado.

## Pré-requisitos

Módulo 04.

## Fundamentos

**Extração de entidades e relações com LLM.** Antes do LLM, extrair "João trabalha na Empresa X"
de um texto livre exigia NLP especializado (NER treinado, parsing sintático). Hoje um LLM com
prompt bem desenhado extrai entidade (nó) e relação (aresta) direto do texto não estruturado —
mais flexível, mas também menos determinístico: o mesmo texto pode gerar extrações levemente
diferentes em execuções diferentes, o que precisa ser considerado na avaliação.

**Modelagem de grafo: nó, aresta, propriedade.** Um nó representa uma entidade (pessoa, projeto,
conceito); uma aresta representa uma relação nomeada e direcionada entre dois nós ("depende de",
"causa", "trabalha em"); propriedades são atributos extras em nó ou aresta (data, peso,
confiança da extração). Modelar bem significa escolher que relações importam pro seu domínio —
um grafo com toda relação possível vira ruído tão inútil quanto nenhum grafo.

**Quando Graph RAG bate RAG vetorial puro.** Busca vetorial responde bem "o que é parecido com
X" mas não responde nativamente "o que conecta A a C". Pergunta multi-hop ("qual módulo depende
de algo que foi alterado por essa mudança?") exige navegar relação explícita — é exatamente onde
um grafo estruturado ganha da similaridade semântica sozinha. Para pergunta que é só "encontre
algo parecido", grafo é complexidade sem retorno.

**Consulta híbrida: grafo + vetor.** Os dois não competem, se complementam: vetor encontra o
ponto de entrada relevante por similaridade semântica, grafo navega a partir dali pelas relações
estruturais que o vetor sozinho não capta. Um pipeline maduro geralmente usa busca vetorial pra
achar candidatos e depois expande via grafo pra trazer contexto relacionado.

## Documentação de referência

- [Neo4j — GraphAcademy](https://graphacademy.neo4j.com/) — cursos gratuitos oficiais, comece
  pelo módulo de fundamentos de grafo antes de partir pra consulta Cypher.
- [Neo4j — documentação oficial](https://neo4j.com/docs/) — tier community free, referência de
  Cypher (linguagem de consulta) usada no projeto.
- [Microsoft Research — GraphRAG](https://microsoft.github.io/graphrag/) — paper e repositório
  oficial da abordagem que popularizou o termo "Graph RAG"; leia o resumo da metodologia antes
  de implementar a sua versão simplificada.
- [LangChain — Graph documentação oficial](https://python.langchain.com/docs/how_to/graph_constructing/)
  — como construir grafo a partir de texto usando LLM via LangChain, se optar por essa rota em
  vez de extração manual.

## O que você vai construir

Extração automática de entidades/relações de um conjunto pequeno de documentos (ex.: notas
técnicas de um projeto seu), carga num grafo (Neo4j community local via Docker, ou networkx pra
uma versão mais leve), e uma consulta multi-hop que RAG vetorial puro erraria, com comparação
lado a lado documentada.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-rag-pipeline-engineer`.
