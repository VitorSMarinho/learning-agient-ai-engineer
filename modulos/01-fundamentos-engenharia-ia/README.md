# Módulo 01 — Fundamentos da Engenharia de IA

## Objetivo

Sair do "notebook que chama uma API de LLM" pra código de produção: configuração segura,
tratamento de erro, saída validada e testável. Engenharia de IA começa aqui, antes de RAG ou
agentes — se a fundação (config, retry, validação, teste) não é sólida, nada que vem depois
segura.

## Pré-requisitos

Python intermediário (funções, módulos, venv). Não precisa saber nada de IA ainda.

## Fundamentos

Antes de abrir o editor, entenda os cinco pilares deste módulo. Isso não substitui a
documentação oficial (linkada embaixo) — é o mapa mental pra você saber o que procurar nela.

**1. Gestão de configuração e segredo.** Uma API key de LLM é dinheiro e acesso — se ela vaza
num commit público, alguém gasta seu crédito ou pior. A regra não é "tomar cuidado", é
estrutural: o código nunca deveria conseguir rodar com um segredo hardcoded, porque o segredo
simplesmente não existe no código, só em variável de ambiente (lida em runtime, nunca
versionada). O padrão universal é um arquivo `.env` (git-ignorado) + um `.env.example`
(versionado, sem valor real) documentando quais variáveis existem.

**2. LLM como dependência externa não confiável.** Toda chamada de API de LLM pode falhar por
motivos que não têm nada a ver com seu código: rate limit, timeout de rede, instabilidade do
provedor. Tratar isso como "exceção rara" é o erro mais comum de quem começa — na prática, é
rotina. Engenharia de verdade assume que a chamada VAI falhar em algum momento e decide
antecipadamente: quantas vezes tentar de novo, quanto esperar entre tentativas (backoff
exponencial, não intervalo fixo), e o que fazer se todas as tentativas esgotarem.

**3. Saída estruturada e validada.** Um LLM devolve texto. Texto não é um contrato. Se seu
código faz `response.split(",")[1]` esperando um formato específico, ele quebra silenciosamente
no dia em que o modelo formatar diferente. A solução é pedir uma estrutura (JSON, por exemplo) e
validar essa estrutura com um schema antes de usar o valor — se não bater com o schema, isso é
um erro tratável, não uma exceção que derruba o programa.

**4. Testes que não dependem da API real.** Se seu teste chama a API de verdade, ele fica lento,
custa dinheiro, e falha quando a internet cai — nada disso tem a ver com "meu código tá
correto?". A resposta é isolar o ponto de chamada de rede numa função própria e substituí-la
(mock) nos testes por uma resposta fake e controlada. Isso testa a SUA lógica, não a
disponibilidade do provedor.

**5. Avaliação básica.** "Funciona" não é binário quando o output vem de um modelo. Você precisa
de um jeito de medir se as respostas estão boas o suficiente — o mínimo viável é um pequeno
conjunto de exemplos com resposta esperada conhecida (gabarito), rodar o modelo neles, e
comparar. Isso é uma avaliação, não um teste unitário — mede qualidade, não corretude binária.

## Documentação de referência

Leia a documentação oficial do provedor que você escolher — não precisa ler os três, mas vale
saber que eles existem e como se comparam:

- **Anthropic (Claude)** — [Guia de início](https://docs.claude.com/en/docs/get-started) e
  [Guia de engenharia de prompt](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview).
  Free tier de créditos pra testar.
- **OpenAI** — [Guia de início da API](https://platform.openai.com/docs/quickstart) e
  [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) (equivalente
  ao que você vai implementar manualmente com Pydantic no critério 3).
- **Google Gemini** — [Guia de início](https://ai.google.dev/gemini-api/docs) — tem free tier
  generoso, boa opção se quiser zero custo sem instalar nada local.
- **Ollama** — [Documentação](https://ollama.com) — roda modelo local de graça, sem API key,
  pra quem quer zero custo e zero dependência de rede externa (mas cuidado: modelo local ainda é
  uma dependência não confiável, os mesmos critérios de retry/validação se aplicam).

Ferramentas específicas usadas no projeto:

- [Pydantic — Validators](https://docs.pydantic.dev/latest/concepts/validators/) — como validar
  saída estruturada (fundamento 3).
- [tenacity](https://tenacity.readthedocs.io/) — biblioteca de retry com backoff usada no
  projeto (fundamento 2). Leia especialmente `wait_exponential` e `retry_if_exception_type`.
- [Real Python — Python Environment Variables](https://realpython.com/python-dotenv/) —
  `.env`/`python-dotenv` na prática (fundamento 1).
- [The Twelve-Factor App — Config](https://12factor.net/config) — o porquê por trás do
  fundamento 1, não só o como.
- [Prompt Engineering Guide](https://www.promptingguide.ai/) — referência livre e completa sobre
  como escrever prompt que produz saída estruturada de forma confiável.

## O que você vai construir

Um CLI em Python que classifica o sentimento de um lote de textos usando um LLM (Claude API,
OpenAI, ou Ollama local — sua escolha, desde que documentada), com engenharia de verdade por
trás: sem chave hardcoded, retry com backoff em falha de API, saída validada por Pydantic
(nunca texto solto), testes que rodam sem depender da API real, e um script de avaliação que
compara a saída do modelo contra um pequeno gabarito rotulado à mão.

Ver `projeto/ENUNCIADO.md` pro enunciado completo e `projeto/CRITERIOS_ACEITE.md` pra rubrica.

## Como é avaliado

Ao abrir o PR com a solução neste repo, rode a skill `revisar-modulo-agient`. Ela
aciona o subagente `python-reviewer` sobre o diff, usando `projeto/CRITERIOS_ACEITE.md` como
rubrica, posta o resultado como comentário no PR e grava `reviews/01-fundamentos-engenharia-ia.json`.
