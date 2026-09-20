# Critérios de Aceite — Módulo 10

Itens **1-6 são obrigatórios**. Item 7 é qualidade.

- [ ] **(obrigatório) Duas rotas implementadas**: existe código real pra rota Tesseract
  (pré-processamento + OCR + parsing) e pra rota LLM com visão, não só uma das duas.
- [ ] **(obrigatório) Saída validada por schema**: os campos extraídos (valor, data,
  nome/descrição) das duas rotas passam por um modelo Pydantic antes de virar resultado final.
- [ ] **(obrigatório) Gabarito rotulado à mão**: existe `gabarito.csv` (ou equivalente) com
  valor correto de cada campo pra pelo menos 5 documentos.
- [ ] **(obrigatório) Comparação de acurácia real**: existe um script/função que compara as
  duas rotas contra o gabarito campo a campo e produz um número (% de acerto), não uma
  impressão subjetiva.
- [ ] **(obrigatório) Testes sem custo obrigatório**: `pytest` roda sem exigir Tesseract
  instalado nem chamada de API paga real — lógica de parsing/validação/comparação testada com
  mocks/fixtures.
- [ ] **(obrigatório) Documentação de instalação**: README da entrega explica como instalar
  Tesseract (gratuito) e como configurar a chave/modelo da rota LLM.
- [ ] Discussão no README de quando cada rota foi melhor, com base nos números reais obtidos.

**Veredito**: `aprovado` se os 6 itens obrigatórios atendem; `precisa_ajuste` caso contrário.
