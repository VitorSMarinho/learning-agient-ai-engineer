# Projeto — Servindo e Medindo um Modelo Local via Ollama

## Contexto

"Rodei um chat no terminal com Ollama" não é a mesma coisa que "sei servir um modelo local com
throughput mensurável". Este projeto força você a expor o modelo como serviço de verdade
(reaproveitando o FastAPI do Módulo 02) e medir número real, não impressão.

## Tarefa

1. Instale Ollama e baixe um modelo open-weight pequeno o suficiente pro seu hardware (ex.:
   `llama3.2:1b`, `qwen2.5:1.5b`, ou equivalente — documente qual escolheu e por quê).
2. Exponha o modelo atrás de uma rota FastAPI (`POST /gerar`, reaproveitando o padrão do Módulo
   02: request/response tipados por Pydantic) que recebe um prompt e retorna a geração do Ollama
   local.
3. Construa um script de **benchmark** que dispara requisições pra essa rota em **3 níveis de
   concorrência** (ex.: 1, 5, 10 requisições simultâneas) usando o mesmo prompt de teste, e mede:
   - tokens/segundo (throughput)
   - latência até o primeiro token (ou até a resposta completa, se sua config não suportar
     streaming — documente qual mediu)
4. Documente no README da entrega: hardware usado (CPU/GPU, RAM), modelo escolhido e tamanho,
   e uma tabela com os resultados dos 3 níveis de concorrência.
5. (Opcional, não obrigatório) Se tiver acesso a uma API paga de LLM, rode o mesmo prompt nela e
   compare latência/qualidade — mas isso é extra, não bloqueia aprovação.

## Restrições técnicas

- Python 3.11+, FastAPI (Módulo 02), Ollama rodando local (gratuito, só precisa de RAM/CPU
  suficiente pro modelo escolhido — modelos de 1-3B rodam em hardware modesto).
- Testes (`pytest`) da rota FastAPI usam `TestClient` com o cliente Ollama mockado (não é
  obrigatório rodar Ollama de verdade pros testes passarem, só pro benchmark).
- Dependências em `requirements.txt`.

## Entrega

PR neste repo com código em `modulos/11-modelos-locais-ollama-vllm/projeto/entrega/`, o script
de benchmark, os resultados reais obtidos (tabela no README), e testes da rota FastAPI mockados.
Depois rode a skill `revisar-modulo-agient`.
