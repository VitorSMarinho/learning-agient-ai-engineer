# Módulo 03 — Bancos SQL + Vetoriais

## Objetivo

Toda aplicação de IA séria mistura dado relacional (usuário, pedido, permissão) com dado
vetorial (embedding pra busca semântica). Este módulo ensina os dois lados vivendo juntos,
com indexação correta — não só "funciona no notebook com 50 linhas".

## Pré-requisitos

Módulo 02. SQL básico (SELECT/JOIN) ajuda mas não é obrigatório.

## Conceitos-chave

- Modelagem relacional aplicada a um domínio real (normalização até onde faz sentido)
- Embeddings: o que são, como são gerados, dimensionalidade
- Índices vetoriais (HNSW, IVFFlat) e o trade-off recall vs latência
- `pgvector` como extensão do Postgres — por que não precisa de um banco vetorial dedicado pra
  começar
- Busca híbrida (full-text + vetorial) e quando cada uma vence sozinha

## Recursos gratuitos

- [pgvector — repositório e documentação oficial](https://github.com/pgvector/pgvector)
- [Supabase — Vector/Embeddings docs](https://supabase.com/docs/guides/ai) (Postgres gerenciado com pgvector, tier free)
- [PostgreSQL — documentação oficial](https://www.postgresql.org/docs/current/index.html)
- [Pinecone Learning Center — Vector Database fundamentals](https://www.pinecone.io/learn/vector-database/) (conceitual, vendor-neutro o suficiente pra fundamentos)
- [Use The Index, Luke](https://use-the-index-luke.com/) (guia gratuito clássico de indexação SQL)

## O que você vai construir

Um schema Postgres (local via Docker, ou Supabase free tier) com tabela relacional de
documentos + coluna `pgvector` de embedding, índice HNSW configurado, e uma função de busca
híbrida (filtro relacional + similaridade vetorial) exposta via script Python testável.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-database-optimizer`.
