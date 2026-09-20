# Projeto — Pipeline RAG com Avaliação

## Contexto

"Funcionou uma vez no notebook" não é RAG em produção. Este projeto exige que você meça se o
seu pipeline recupera a fonte certa e cita ela — não só que ele "parece responder bem".

## Tarefa

1. Escolha uma base de documentos real (10-30 documentos: pode ser a documentação de um projeto
   seu, um conjunto de artigos técnicos, ou PDFs públicos).
2. Implemente ingestão + chunking documentado (explique no README a estratégia escolhida e por
   quê — tamanho fixo, por parágrafo, por seção).
3. Indexe os chunks no banco do Módulo 03 (reaproveite o schema/índice, ou monte um equivalente
   se optou por outro store no módulo anterior — documente a escolha).
4. Implemente recuperação com re-ranking simples (pode ser um segundo passo com o próprio LLM
   pontuando relevância dos top-N candidatos, ou um método mais simples documentado).
5. Implemente geração da resposta final que **cita explicitamente** qual chunk/documento
   fundamentou cada afirmação (não é opcional — é o item mais importante deste módulo).
6. Crie um conjunto de avaliação com no mínimo 10 perguntas + gabarito (qual documento/trecho
   deveria ser citado pra cada uma) e um script `avaliar_rag.py` que roda as 10 perguntas e
   reporta: taxa de citação correta, e quantas respostas citaram fonte errada ou nenhuma fonte.

## Restrições técnicas

Pode usar LangChain, LlamaIndex, ou implementação direta (sem framework) — documente a escolha
e por quê. LLM local (Ollama) ou via API, sempre com fallback documentado se não tiver budget.

## Entrega

PR neste repo com o código em `modulos/04-sistemas-rag-completos/projeto/entrega/`: pipeline de
ingestão, módulo de retrieval+geração, `perguntas_gabarito.json` (ou `.csv`), `avaliar_rag.py`,
README explicando a estratégia de chunking e os resultados da avaliação. Depois rode a skill
`revisar-modulo-agient`.
