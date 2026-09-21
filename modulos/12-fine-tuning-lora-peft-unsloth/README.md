# Módulo 12 — Fine-Tuning: LoRA, PEFT, Unsloth

## Objetivo

Módulo de fechamento da trilha: quando prompt engineering e RAG não bastam (formato muito
específico, domínio muito nichado, custo de contexto longo repetido), fine-tuning eficiente é
a próxima ferramenta. Aqui você faz de verdade, não só lê sobre.

## Pré-requisitos

Módulos 01, 02, 11 (já sabe servir modelo local).

## Fundamentos

**Por que fine-tuning completo é raro.** Fine-tuning completo re-treina TODOS os parâmetros do
modelo — pra um modelo de bilhões de parâmetros, isso exige memória de GPU proporcional ao
tamanho do modelo inteiro, várias vezes (pesos, gradientes, estados do otimizador). É caro,
lento, e arriscado (pode degradar capacidades gerais do modelo — "esquecimento catastrófico").
LoRA (Low-Rank Adaptation) resolve isso treinando só um número pequeno de parâmetros extras
(matrizes de baixo rank injetadas em camadas específicas) e mantendo o modelo original congelado
— resultado próximo do fine-tuning completo, com uma fração do custo computacional e memória.

**PEFT: o que é treinado vs congelado.** PEFT é a categoria geral de técnicas que treinam só uma
fatia pequena dos parâmetros (LoRA é a mais comum, mas não a única). O modelo base fica
congelado — nenhum peso dele muda. O que é treinado são as camadas extras adicionadas. Isso tem
uma consequência prática boa: você pode ter vários "adapters" LoRA diferentes (um por tarefa)
compartilhando o mesmo modelo base congelado, e trocar entre eles sem recarregar o modelo
inteiro.

**Preparação de dataset.** Fine-tuning não corrige um modelo ruim com dado ruim — o princípio é
"qualidade > quantidade" de forma bem mais extrema aqui do que em treino do zero. Um dataset
pequeno (dezenas a poucas centenas de exemplos) mas consistente, bem formatado, e representativo
do padrão exato que você quer ensinar geralmente supera um dataset grande e ruidoso. Formato
importa: os exemplos precisam seguir exatamente a estrutura de prompt/resposta que o modelo vai
usar em produção.

**Avaliação pré/pós.** Sem medir o modelo ANTES do fine-tuning no mesmo conjunto de teste que
você vai usar DEPOIS, você não tem prova de que o treino ajudou — só a impressão de que ajudou.
Essa avaliação também precisa ser honesta o suficiente pra revelar quando o fine-tuning NÃO
melhorou (dataset pequeno demais, tarefa mal definida, overfitting nos exemplos de treino) — que
é um resultado tão válido de documentar quanto "melhorou".

## Documentação de referência

- [Unsloth — documentação e notebooks oficiais](https://docs.unsloth.ai/) — o caminho mais
  direto pra rodar fine-tuning LoRA de verdade na GPU gratuita do Colab; comece pelos notebooks
  prontos antes de customizar.
- [Hugging Face — PEFT (documentação oficial)](https://huggingface.co/docs/peft/index) — a
  biblioteca por trás da maioria das implementações de LoRA em Python.
- [Hugging Face — LoRA (guia conceitual oficial)](https://huggingface.co/docs/peft/conceptual_guides/lora) —
  explica a matemática de baixo rank de forma acessível, sem precisar do paper original.
- [Google Colab](https://colab.research.google.com/) — onde você roda o treino, GPU gratuita
  (com limite de tempo/cota, mas suficiente pro escopo deste projeto).

## O que você vai construir

Fine-tuning LoRA de um modelo pequeno open-weight (via Unsloth, no Colab gratuito) num dataset
pequeno e específico que você mesmo monta (ex.: 50-100 exemplos de um formato de resposta bem
definido), com avaliação antes/depois no mesmo conjunto de teste documentando a melhora (ou
honestamente documentando que não melhorou, e por quê).

## Como é avaliado

Este módulo ainda não tem projeto prático detalhado. Quando tiver, será resolvido e submetido
via PR neste repo, revisado pela skill `revisar-modulo-agient` usando o subagente
`engineering-ai-engineer`.
