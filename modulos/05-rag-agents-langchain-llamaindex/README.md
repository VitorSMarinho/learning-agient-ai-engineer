# Módulo 05 — RAG Agents: LangChain vs LlamaIndex

## Objetivo

RAG estático (uma pergunta, uma recuperação, uma resposta) não resolve pergunta complexa. RAG
agêntico decide sozinho se precisa buscar de novo, com outra query, em outra fonte. Este módulo
compara os dois frameworks dominantes construindo o mesmo agente nos dois.

## Pré-requisitos

Módulo 04.

## Fundamentos

**Query transformation e decomposição.** Uma pergunta complexa do usuário raramente casa bem
com uma única busca vetorial. Query transformation reescreve a pergunta original numa (ou
várias) mais fáceis de recuperar — por exemplo, decompondo "compare X e Y" em "busca sobre X" +
"busca sobre Y" separadas, e só depois juntando os resultados na geração. Isso recupera melhor
do que jogar a pergunta composta inteira direto no índice.

**Tool-calling aplicado à recuperação.** Em vez de sempre buscar do mesmo jeito, um agente com
tool-calling decide, pergunta a pergunta, qual ferramenta de busca usar (banco vetorial A,
banco B, busca web, SQL direto) e com qual query. Isso transforma "RAG" de um pipeline fixo pra
uma decisão dinâmica — o custo é que agora o comportamento depende do modelo escolher a
ferramenta certa, o que precisa ser testado, não assumido.

**Roteamento entre múltiplos índices.** Quando existe mais de uma fonte de dado (documentação
técnica, base de FAQ, base de código), roteamento decide qual índice consultar antes de gastar
uma chamada de busca — seja por classificação da pergunta, seja deixando o próprio agente
escolher via tool-calling. Buscar no índice errado custa tempo e pode trazer contexto irrelevante
que confunde a geração.

**LangChain vs. LlamaIndex: onde cada um vence na prática.** LangChain (via LCEL) dá controle
explícito sobre cada etapa do pipeline — mais código, mais visibilidade do que está acontecendo
em cada passo. LlamaIndex oferece abstrações de índice/query engine mais prontas — menos código
pra um caso comum, menos controle fino quando o caso foge do padrão. Nenhum dos dois é
estritamente melhor; a escolha certa depende de quanto controle o seu caso de uso exige.

## Documentação de referência

- [LangChain — Agents documentação oficial](https://python.langchain.com/docs/concepts/agents/)
  — conceitos de agente no ecossistema LangChain, base pra metade do exercício.
- [LlamaIndex — Agents documentação oficial](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
  — o mesmo conceito, abstrações diferentes; compare a quantidade de código pra fazer a mesma
  coisa.
- [LangGraph — documentação oficial](https://langchain-ai.github.io/langgraph/) — runtime de
  agente usado hoje em ambos os ecossistemas; vale entender antes do Módulo 08, que aprofunda
  nele.

## O que você vai construir

O mesmo agente de perguntas-e-respostas sobre a base do Módulo 04, implementado duas vezes: uma
em LangChain, outra em LlamaIndex. Documento comparativo curto (`COMPARACAO.md`) com latência,
linhas de código, e qual framework você recomendaria pra qual cenário — com dado, não opinião.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-rag-pipeline-engineer`.
