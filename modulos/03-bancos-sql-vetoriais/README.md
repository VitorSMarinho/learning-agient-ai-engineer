# Módulo 03 — Bancos SQL + Vetoriais

## Objetivo

Toda aplicação de IA séria mistura dado relacional (usuário, pedido, permissão) com dado
vetorial (embedding pra busca semântica). Este módulo ensina os dois lados vivendo juntos,
com indexação correta — não só "funciona no notebook com 50 linhas".

## Pré-requisitos

Módulo 02. SQL básico (SELECT/JOIN) ajuda mas não é obrigatório.

## Fundamentos

**Modelagem relacional aplicada a domínio real.** Normalizar até a 3ª forma normal é regra de
livro-texto; normalizar até onde o domínio de verdade exige é engenharia. O objetivo não é
seguir a forma normal por dogma, é evitar duas armadilhas opostas: dado duplicado que diverge
com o tempo (sub-normalização) e JOIN de 6 tabelas pra responder uma pergunta simples
(sobre-normalização). Modele pelo que a aplicação vai consultar, não só pelo que ela vai gravar.

**Embeddings: o que são e por que têm dimensão.** Um embedding é um vetor de números que
representa o "significado" de um texto (ou imagem) num espaço onde proximidade geométrica
aproxima proximidade semântica. A dimensionalidade (384, 768, 1536...) é definida pelo modelo
que gerou o embedding — não é um parâmetro que você escolhe livremente, é uma característica do
modelo, e todo vetor no seu índice precisa ter vindo do mesmo modelo pra comparação fazer
sentido.

**Índices vetoriais e o trade-off recall vs. latência.** Busca vetorial exata (comparar a query
contra TODO vetor do banco) é lenta em escala. Índices como HNSW e IVFFlat trocam exatidão
garantida por velocidade: eles aproximam o "top-k mais próximo" sem varrer tudo, e você ajusta
parâmetros (ex.: `ef_search` no HNSW) pra decidir o quanto está disposto a perder de recall em
troca de latência menor. Não existe configuração "certa" universal — depende do tamanho dos
dados e da tolerância da aplicação.

**`pgvector`: por que não precisa de banco vetorial dedicado pra começar.** Se você já tem
Postgres rodando pro dado relacional, `pgvector` adiciona busca vetorial como uma extensão —
sem outro serviço pra operar, outro backup pra configurar, outra rede pra proteger. Um banco
vetorial dedicado (Pinecone, Weaviate, Qdrant) só compensa quando a escala/performance vetorial
específica justifica o custo operacional extra. Comece simples, meça, só então migre se precisar.

**Busca híbrida: full-text + vetorial.** Busca vetorial captura similaridade semântica ("carro"
encontra "veículo"), mas é ruim pra correspondência exata (código de produto, nome próprio,
número). Full-text search (ex.: `tsvector` do Postgres) é o oposto. Busca híbrida combina os
dois scores — geralmente vence os dois métodos isolados, porque cobre os casos onde cada um
falha sozinho.

## Documentação de referência

- [pgvector — repositório e documentação oficial](https://github.com/pgvector/pgvector) — leia a
  seção de tipos de índice (HNSW vs IVFFlat) antes de escolher um pro projeto.
- [PostgreSQL — documentação oficial](https://www.postgresql.org/docs/current/index.html) —
  seções de índices (`CREATE INDEX`) e full-text search (`tsvector`/`tsquery`) pra busca híbrida.
- [Databricks — Vector Search documentação oficial](https://docs.databricks.com/en/generative-ai/vector-search.html)
  — referência de como um provedor gerenciado resolve o mesmo problema em escala; útil pra
  entender pra que serve um banco vetorial dedicado versus `pgvector`.
- [Use The Index, Luke](https://use-the-index-luke.com/) — guia gratuito clássico sobre como
  índice SQL funciona de verdade, base pra entender o trade-off de qualquer índice, vetorial ou
  não.

## O que você vai construir

Um schema Postgres (local via Docker, ou Supabase free tier) com tabela relacional de
documentos + coluna `pgvector` de embedding, índice HNSW configurado, e uma função de busca
híbrida (filtro relacional + similaridade vetorial) exposta via script Python testável.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-database-optimizer`.
