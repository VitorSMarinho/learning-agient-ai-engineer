"""Cliente de LLM isolado do resto do CLI, pra ser facil de mockar em teste."""
from __future__ import annotations

import os
from typing import Literal

import anthropic
from pydantic import BaseModel, ValidationError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

FALHAS_RECUPERAVEIS_API = (
    anthropic.APITimeoutError,
    anthropic.APIConnectionError,
    anthropic.RateLimitError,
)


class RespostaLLMInvalida(Exception):
    """A resposta do modelo nao bateu com o schema esperado."""


class Sentimento(BaseModel):
    classificacao: Literal["positivo", "negativo", "neutro"]
    justificativa: str = ""


def _modelo_configurado() -> str:
    return os.environ.get("ANTHROPIC_MODEL", "claude-3-5-haiku-latest")


def _chamar_api_anthropic(texto: str) -> str:
    """Faz a chamada de rede de verdade. Isolada pra poder ser mockada nos testes."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY nao configurada (veja .env.example)")

    client = anthropic.Anthropic(api_key=api_key)
    prompt = (
        "Classifique o sentimento do texto a seguir como positivo, negativo ou neutro. "
        "Responda em JSON no formato {\"classificacao\": \"...\", \"justificativa\": \"...\"}.\n\n"
        f"Texto: {texto}"
    )
    resposta = client.messages.create(
        model=_modelo_configurado(),
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    return resposta.content[0].text


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(FALHAS_RECUPERAVEIS_API),
    reraise=True,
)
def classificar_sentimento(texto: str) -> Sentimento:
    """Classifica o sentimento de um texto usando o LLM configurado.

    Levanta RespostaLLMInvalida se o modelo devolver algo fora do schema esperado
    (tratado como erro recuperavel pelo chamador, nao derruba o processo).
    """
    import json

    bruto = _chamar_api_anthropic(texto)
    try:
        dados = json.loads(bruto)
        return Sentimento(**dados)
    except (json.JSONDecodeError, ValidationError) as exc:
        raise RespostaLLMInvalida(f"Resposta fora do schema: {bruto!r}") from exc
