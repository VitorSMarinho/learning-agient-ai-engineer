import csv
from unittest.mock import patch

import pytest

import llm_client
import sentiment_cli
from llm_client import RespostaLLMInvalida, Sentimento, classificar_sentimento


def test_classificar_sentimento_caminho_feliz(monkeypatch):
    monkeypatch.setattr(
        llm_client,
        "_chamar_api_anthropic",
        lambda texto: '{"classificacao": "positivo", "justificativa": "elogio direto"}',
    )
    resultado = classificar_sentimento("Adorei o produto!")
    assert resultado == Sentimento(classificacao="positivo", justificativa="elogio direto")


def test_classificar_sentimento_resposta_invalida(monkeypatch):
    monkeypatch.setattr(llm_client, "_chamar_api_anthropic", lambda texto: "isso nao e json")
    with pytest.raises(RespostaLLMInvalida):
        classificar_sentimento("texto qualquer")


def test_processar_arquivo_gera_saida(tmp_path, monkeypatch):
    entrada = tmp_path / "entrada.csv"
    saida = tmp_path / "saida.csv"
    entrada.write_text("texto\nAdorei!\nPessimo servico\n", encoding="utf-8")

    respostas = iter(
        [
            '{"classificacao": "positivo", "justificativa": "ok"}',
            '{"classificacao": "negativo", "justificativa": "ok"}',
        ]
    )
    monkeypatch.setattr(llm_client, "_chamar_api_anthropic", lambda texto: next(respostas))

    codigo = sentiment_cli.processar_arquivo(entrada, saida)
    assert codigo == 0

    with saida.open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    assert [l["classificacao"] for l in linhas] == ["positivo", "negativo"]


def test_processar_arquivo_entrada_inexistente(tmp_path):
    codigo = sentiment_cli.processar_arquivo(tmp_path / "nao-existe.csv", tmp_path / "saida.csv")
    assert codigo == 1


def test_processar_arquivo_continua_apos_falha_individual(tmp_path, monkeypatch):
    entrada = tmp_path / "entrada.csv"
    saida = tmp_path / "saida.csv"
    entrada.write_text("texto\nOk\nFalha\n", encoding="utf-8")

    respostas = iter(["nao e json valido", '{"classificacao": "neutro", "justificativa": "ok"}'])
    monkeypatch.setattr(llm_client, "_chamar_api_anthropic", lambda texto: next(respostas))

    codigo = sentiment_cli.processar_arquivo(entrada, saida)
    assert codigo == 0

    with saida.open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    assert len(linhas) == 1
    assert linhas[0]["classificacao"] == "neutro"
