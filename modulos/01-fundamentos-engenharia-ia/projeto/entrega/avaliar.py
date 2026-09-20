"""Compara resultados.csv contra gabarito.csv rotulado a mao e imprime acuracia.

Uso:
    python avaliar.py --resultados resultados.csv --gabarito gabarito.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def carregar_mapa(caminho: Path, coluna_classe: str) -> dict[str, str]:
    with caminho.open(newline="", encoding="utf-8") as f:
        return {linha["texto"]: linha[coluna_classe] for linha in csv.DictReader(f)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--resultados", required=True, type=Path)
    parser.add_argument("--gabarito", required=True, type=Path)
    args = parser.parse_args()

    if not args.resultados.exists() or not args.gabarito.exists():
        print("erro: resultados.csv ou gabarito.csv nao encontrado", file=sys.stderr)
        return 1

    previstos = carregar_mapa(args.resultados, "classificacao")
    esperados = carregar_mapa(args.gabarito, "classificacao_esperada")

    comparaveis = [t for t in esperados if t in previstos]
    if not comparaveis:
        print("erro: nenhum texto do gabarito encontrado nos resultados", file=sys.stderr)
        return 1

    acertos = sum(1 for t in comparaveis if previstos[t] == esperados[t])
    acuracia = acertos / len(comparaveis)

    print(f"comparados: {len(comparaveis)}")
    print(f"acertos: {acertos}")
    print(f"acuracia: {acuracia:.2%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
