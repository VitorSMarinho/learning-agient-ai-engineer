"""CLI de classificacao de sentimento em lote, com engenharia de producao por tras.

Uso:
    python sentiment_cli.py --input dados_exemplo.csv --output resultados.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from llm_client import FALHAS_RECUPERAVEIS_API, RespostaLLMInvalida, classificar_sentimento


def processar_arquivo(caminho_entrada: Path, caminho_saida: Path) -> int:
    if not caminho_entrada.exists():
        print(f"erro: arquivo de entrada nao encontrado: {caminho_entrada}", file=sys.stderr)
        return 1

    with caminho_entrada.open(newline="", encoding="utf-8") as f_in:
        linhas = list(csv.DictReader(f_in))

    if not linhas or "texto" not in linhas[0]:
        print("erro: CSV de entrada precisa de uma coluna 'texto'", file=sys.stderr)
        return 1

    resultados = []
    falhas = 0
    for linha in linhas:
        texto = linha["texto"]
        try:
            sentimento = classificar_sentimento(texto)
            resultados.append(
                {
                    "texto": texto,
                    "classificacao": sentimento.classificacao,
                    "justificativa": sentimento.justificativa,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
            )
        except RespostaLLMInvalida as exc:
            falhas += 1
            print(f"aviso: resposta invalida do modelo pra {texto!r}: {exc}", file=sys.stderr)
        except (*FALHAS_RECUPERAVEIS_API, RuntimeError) as exc:
            falhas += 1
            print(f"aviso: falha ao classificar {texto!r}: {exc}", file=sys.stderr)

    with caminho_saida.open("w", newline="", encoding="utf-8") as f_out:
        campos = ["texto", "classificacao", "justificativa", "timestamp"]
        writer = csv.DictWriter(f_out, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)

    print(f"processados: {len(resultados)}, falhas: {falhas}, saida: {caminho_saida}")
    return 0


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Classificador de sentimento em lote")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    return processar_arquivo(args.input, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
