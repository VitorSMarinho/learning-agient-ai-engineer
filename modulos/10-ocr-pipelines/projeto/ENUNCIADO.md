# Projeto — Extração Estruturada de Recibo: Tesseract vs LLM com Visão

## Contexto

"Digitalizar recibo/nota fiscal" é um dos pedidos mais comuns de automação pra comércio local.
Tesseract (OCR clássico, gratuito, roda local) e um LLM multimodal (mais caro, mais robusto a
foto torta/mal iluminada) resolvem o mesmo problema de formas bem diferentes — este projeto faz
você comparar os dois com dado real, não só ler sobre a diferença.

## Tarefa

1. Consiga (ou crie) pelo menos **5 imagens** de documentos simples com campos estruturados
   (recibo, nota fiscal, cupom — pode ser foto/scan seu mesmo, ou uma base pública gratuita de
   recibos). Cada documento precisa ter pelo menos: um valor monetário, uma data, um
   nome/descrição.
2. Construa um pipeline que roda os documentos por **duas rotas**:
   - **Rota Tesseract**: pré-processamento básico de imagem (conversão pra escala de cinza,
     talvez binarização/contraste — use OpenCV ou Pillow) → OCR via `pytesseract` → texto bruto.
   - **Rota LLM com visão**: envia a imagem direto pra um modelo com visão (Claude, GPT-4V, ou
     equivalente) pedindo os campos estruturados.
3. Das DUAS rotas, extraia os campos estruturados (valor, data, nome/descrição) validados por
   Pydantic. Pra rota Tesseract, isso significa parsear o texto bruto (regex/heurística) pros
   mesmos campos.
4. Digite à mão um **gabarito** com o valor correto de cada campo pra cada um dos 5+ documentos.
5. Compare as duas rotas contra o gabarito: acurácia campo a campo (não "achei que ficou bom") —
   quantos valores, datas e nomes cada rota acertou exatamente.
6. Documente no README da entrega: em qual tipo de documento cada rota foi melhor, e o
   trade-off custo/velocidade/robustez entre elas.

## Restrições técnicas

- Python 3.11+. `pytesseract` + Tesseract instalado (documente a instalação no README — é
  gratuito). Pra rota LLM, pode usar Claude API ou Ollama com um modelo multimodal local se
  tiver hardware — documente qual usou.
- Testes (`pytest`) não precisam rodar OCR/LLM de verdade (isso é custoso/lento) — mockar as
  chamadas de extração e testar a lógica de parsing/validação/comparação de acurácia é
  suficiente.
- Dependências em `requirements.txt`.

## Entrega

PR neste repo com código em `modulos/10-ocr-pipelines/projeto/entrega/`, as imagens de exemplo
(ou instruções de onde conseguir), `gabarito.csv`, os resultados das duas rotas, e o relatório
de acurácia comparando as duas. Depois rode a skill `revisar-modulo-agient`.
