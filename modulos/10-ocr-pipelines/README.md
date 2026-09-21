# Módulo 10 — OCR Pipelines

## Objetivo

Extrair texto estruturado de documento real (nota fiscal, contrato, print de conversa) é um dos
casos de uso de IA mais pedidos por comércio local, e é onde "OCR tradicional" e "LLM
multimodal" se encontram. Este módulo compara as duas abordagens num pipeline de produção.

## Pré-requisitos

Módulo 02.

## Fundamentos

**OCR clássico vs extração multimodal.** Tesseract lê pixel e devolve texto — rápido, roda
local, de graça, mas não entende layout: não sabe que "R$ 45,90" na terceira linha é o campo
"valor total". Um LLM com visão recebe a imagem inteira e pode devolver direto a estrutura que
você pediu ("me dá o valor total em JSON"), porque ele entende contexto visual, não só caractere
— mas custa por chamada e é mais lento. Na prática, a escolha certa depende do volume (Tesseract
escala de graça, LLM não) e da complexidade do layout (documento simples e padronizado favorece
Tesseract; documento variado favorece LLM).

**Pré-processamento de imagem.** OCR clássico é extremamente sensível à qualidade da imagem de
entrada: foto torta, contraste ruim, ou fundo com ruído derruba a acurácia de forma dramática
— não gradual. Rotação, ajuste de contraste e recorte da área relevante antes de passar pro
Tesseract frequentemente importam mais pra acurácia final do que qualquer parâmetro de
configuração do próprio OCR. LLM com visão é bem mais tolerante a isso, mas não infinitamente.

**Extração estruturada.** Ter o texto não resolve o problema — "Total: R$45,90\nData:
12/03/2026" ainda é string solta. Extração estruturada é o passo de ir desse texto (ou da
imagem direto, no caso do LLM) pra um objeto validado com campos tipados (`valor: Decimal`,
`data: date`). Isso conecta direto com o Módulo 01: a mesma disciplina de "nunca confiar em
string solta, sempre validar contra schema" se aplica aqui.

**Avaliação de OCR.** "Ficou bom" não é métrica. Avaliação de OCR de verdade mede campo por
campo contra um gabarito: esse campo específico foi extraído corretamente, sim ou não? Taxa de
erro de caractere (quantos caracteres errados por caractere total) é a métrica clássica pro
texto bruto; para extração estruturada, a métrica que importa mais é "esse campo bateu com o
gabarito", porque um erro de 1 caractere no CPF é tão grave quanto errar o campo inteiro.

## Documentação de referência

- [Tesseract OCR — documentação oficial](https://tesseract-ocr.github.io/) — comece pelo guia de
  uso via linha de comando antes de ir pro `pytesseract`, ajuda a entender os parâmetros reais.
- [pytesseract — repositório oficial](https://github.com/madmaze/pytesseract) — wrapper Python
  que você vai usar no projeto.
- [OpenCV — documentação oficial](https://docs.opencv.org/) — funções de pré-processamento
  (rotação, threshold, denoise) que mudam a acurácia do Tesseract.
- [Anthropic — Vision (documentação oficial)](https://docs.claude.com/en/docs/build-with-claude/vision) —
  como enviar imagem pra Claude e pedir extração estruturada direto, pra comparar com o Tesseract.

## O que você vai construir

Pipeline que recebe imagem de um documento simples (ex.: nota fiscal ou recibo, pode ser
foto/scan seu mesmo), roda as duas abordagens (Tesseract + LLM com visão), extrai campos
estruturados validados por Pydantic dos dois, e compara acurácia campo a campo contra um
gabarito que você digita à mão.

## Como é avaliado

Ao abrir o PR com a solução neste repo, rode a skill `revisar-modulo-agient`. Ela
aciona o subagente `python-reviewer` sobre o diff, usando `projeto/CRITERIOS_ACEITE.md`
como rubrica, posta o resultado como comentário no PR e grava
`reviews/10-ocr-pipelines.json`.
