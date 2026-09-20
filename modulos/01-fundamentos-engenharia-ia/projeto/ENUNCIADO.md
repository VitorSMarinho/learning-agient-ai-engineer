# Projeto — Classificador de Sentimento com Engenharia de Verdade

## Contexto

Times de produto recebem review de cliente sem parar (WhatsApp, avaliação de app, comentário de
suporte). Classificar o sentimento manualmente não escala. Mas "só chama a API do LLM" também
não é solução de produção: cai, demora, erra formato, custa dinheiro se você reprocessa tudo
numa falha boba. Este projeto força as duas metades: usar um LLM E tratar ele como uma
dependência externa não confiável.

## Tarefa

Construa um CLI Python (`sentiment_cli.py` ou equivalente) que:

1. Recebe um arquivo de entrada (`.csv` ou `.jsonl`) com uma coluna/campo de texto. Use uma
   base pública gratuita como fonte de exemplo (ex.: um subconjunto pequeno do
   [IMDB Reviews](https://ai.stanford.edu/~amaas/data/sentiment/) ou textos que você mesmo
   escrever — não precisa dataset gigante, 15-30 linhas já bastam pra provar o pipeline).
2. Pra cada texto, chama um LLM (Claude API, OpenAI, ou um modelo local via Ollama — sua
   escolha, documentada no README do projeto) pedindo classificação em `positivo` / `negativo`
   / `neutro`.
3. Valida a resposta do modelo com um schema Pydantic (`Sentiment: Literal["positivo",
   "negativo", "neutro"]` + campo de confiança/justificativa opcional). Se o modelo devolver
   algo fora do schema, trata como erro recuperável, não crasha o programa.
4. Implementa retry com backoff exponencial (biblioteca `tenacity` ou equivalente) em falha de
   rede/timeout/rate limit da API — no mínimo 3 tentativas.
5. Nenhuma chave de API hardcoded no código. Lê de variável de ambiente (`.env` +
   `python-dotenv`, ou equivalente), com um `.env.example` no repo (sem valor real).
6. Grava o resultado num arquivo de saída (`resultados.csv` ou `.jsonl`) com texto original +
   classificação + timestamp.
7. Inclui um script de avaliação (`avaliar.py`) que compara os resultados contra um pequeno
   gabarito rotulado à mão por você (`gabarito.csv`, mínimo 10 linhas) e imprime acurácia.
8. Testes automatizados (`pytest`) que **mockam** a chamada ao LLM — os testes precisam passar
   sem bater na API real e sem gastar crédito.

## Restrições técnicas

- Python 3.11+, dependências em `requirements.txt` ou `pyproject.toml`.
- Sem segredo em texto plano em nenhum arquivo versionado.
- Código roda com um único comando documentado no README do projeto
  (ex.: `python sentiment_cli.py --input dados.csv --output resultados.csv`).

## Entrega

Abra um PR neste repo com a pasta do seu projeto dentro de `modulos/01-fundamentos-engenharia-ia/projeto/entrega/`
(crie essa subpasta), incluindo código, `requirements.txt`, `.env.example`, `README.md` de uso,
testes, `gabarito.csv` e os resultados gerados. Depois rode a skill `revisar-modulo-agient`
apontando pro PR.
