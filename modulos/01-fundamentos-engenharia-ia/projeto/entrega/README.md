# Entrega — Módulo 01 — Classificador de Sentimento

Provedor escolhido: **Anthropic API** (Claude), configurável via `ANTHROPIC_MODEL`.

## Como rodar do zero

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edite .env e coloque sua ANTHROPIC_API_KEY

python sentiment_cli.py --input dados_exemplo.csv --output resultados.csv
python avaliar.py --resultados resultados.csv --gabarito gabarito.csv
```

## Testes (não batem na API real)

```bash
pytest
```

## Estrutura

- `sentiment_cli.py` — CLI principal, orquestra leitura/escrita/erro
- `llm_client.py` — isola a chamada de rede (retry, validação, exceção própria)
- `avaliar.py` — compara `resultados.csv` contra `gabarito.csv`
- `tests/` — testes com a chamada de LLM mockada
