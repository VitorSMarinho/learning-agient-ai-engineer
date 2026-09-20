# Módulo 10 — OCR Pipelines

## Objetivo

Extrair texto estruturado de documento real (nota fiscal, contrato, print de conversa) é um dos
casos de uso de IA mais pedidos por comércio local, e é onde "OCR tradicional" e "LLM
multimodal" se encontram. Este módulo compara as duas abordagens num pipeline de produção.

## Pré-requisitos

Módulo 02.

## Conceitos-chave

- OCR clássico (Tesseract) vs extração multimodal via LLM com visão
- Pré-processamento de imagem (rotação, contraste, recorte) e o quanto isso muda a acurácia
- Extração estruturada: ir de "texto solto" pra JSON validado (nome, valor, data)
- Avaliação de OCR: taxa de erro de caractere, campo por campo, não só "achei que ficou bom"

## Recursos gratuitos

- [Tesseract OCR — documentação oficial](https://tesseract-ocr.github.io/)
- [Anthropic — Vision documentação oficial](https://docs.claude.com/en/docs/build-with-claude/vision)
- [OpenCV — documentação oficial](https://docs.opencv.org/) (pré-processamento de imagem)
- [pytesseract — repositório oficial](https://github.com/madmaze/pytesseract)

## O que você vai construir

Pipeline que recebe imagem de um documento simples (ex.: nota fiscal ou recibo, pode ser
foto/scan seu mesmo), roda as duas abordagens (Tesseract + LLM com visão), extrai campos
estruturados validados por Pydantic dos dois, e compara acurácia campo a campo contra um
gabarito que você digita à mão.

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`python-reviewer`.
