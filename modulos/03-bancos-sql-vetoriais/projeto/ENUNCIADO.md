# Projeto — Busca Híbrida com Postgres + pgvector

## Contexto

Busca vetorial pura ignora filtro de negócio óbvio ("só documentos ativos", "só do meu time").
Busca relacional pura não entende similaridade semântica. Sistema real usa os dois juntos —
este projeto força você a montar essa combinação, não só um dos dois isolado.

## Tarefa

1. Suba Postgres com a extensão `pgvector` (Docker local com imagem `pgvector/pgvector`, ou
   projeto free do Supabase — documente a escolha).
2. Crie uma tabela `documentos` com pelo menos: `id`, `titulo`, `conteudo`, `categoria` (coluna
   relacional pra filtro), `embedding vector(N)` (dimensão de acordo com o modelo de embedding
   escolhido).
3. Popule com no mínimo 20 documentos reais (pode ser texto seu, de um projeto, ou de uma fonte
   pública) distribuídos em pelo menos 3 categorias diferentes, com embedding gerado de verdade
   (Ollama local com modelo de embedding, ou API de embedding de algum provedor — não vale
   vetor aleatório).
4. Crie um índice HNSW na coluna de embedding (`CREATE INDEX ... USING hnsw`).
5. Escreva uma função/script Python `busca_hibrida(query: str, categoria: str | None) -> list`
   que: gera o embedding da query, filtra por `categoria` quando informado (SQL `WHERE`), ordena
   por similaridade vetorial (`<->`), e retorna os top-5.
6. Escreva um script comparativo `comparar.py` que roda a mesma query com e sem o filtro de
   categoria e imprime a diferença nos resultados — prova de que o filtro relacional está
   funcionando de verdade, não só decorativo.
7. Testes que validam a função de busca contra o banco (pode ser teste de integração que sobe
   o Postgres via Docker, documentado no README de como rodar).

## Restrições técnicas

Postgres + pgvector (não vale trocar por um vector DB dedicado tipo Pinecone/Weaviate — o
objetivo do módulo é aprender pgvector especificamente). Python 3.11+, `psycopg` ou `asyncpg`.

## Entrega

PR neste repo com o código em `modulos/03-bancos-sql-vetoriais/projeto/entrega/`: schema SQL
(`schema.sql`), script de carga, `busca_hibrida.py`, `comparar.py`, testes, README com passo a
passo de setup (Docker compose ou instruções Supabase) e como rodar tudo do zero. Depois rode a
skill `revisar-modulo-agient`.
