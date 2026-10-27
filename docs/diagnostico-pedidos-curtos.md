# Diagnóstico da seleção em pedidos curtos

**Não foi encontrada uma correção comprovada apenas na skill.** Duas novas
descrições foram rejeitadas e a original foi restaurada byte a byte. A instalação
permanece na v0.1.4, sem alterar `AGENTS.md`, configuração pessoal ou corpo das
regras linguísticas. Este diagnóstico complementa a [primeira rodada](selecao-descricao.md).

## Onde ocorre a decisão

A [documentação oficial](https://learn.chatgpt.com/docs/build-skills) distingue
invocação explícita e seleção implícita. O catálogo fornece metadados para o
modelo decidir quando consultar a skill. A descrição não é um disparador
determinístico por palavra ou tamanho do pedido.

O código oficial do CLI instalado, **rust-v0.154.0**, permite delimitar o problema:

- Skills locais usam o `description` do frontmatter; o caminho host usa a política
  `CoreCompatible`. Alterar somente `interface.short_description` em
  `agents/openai.yaml` não muda essa descrição no CLI.
  [Fonte: render.rs](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/render.rs#L33).
- O orçamento compartilhado pode abreviar descrições preservando seus prefixos.
  O renderizador não recebe o tamanho do pedido como critério de seleção.
  [Fonte: alocação de descrições](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/render.rs#L323).
- Menções explícitas seguem outra rota: o runtime resolve a skill e carrega seu
  corpo antes da amostragem. Isso pode ocorrer sem comando de leitura visível.
  [Fonte: início do turno](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/session/turn.rs#L873)
  e [leitura interna](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/ext/skills/src/host_prompt.rs#L76).

Assim, a falha observada nos pedidos implícitos fica na decisão de consultar o
conteúdo, depois da descoberta da skill. A instalação não está simplesmente
invisível: houve leituras de I09 nas mesmas condições de execução.

## Captura local do catálogo

Foi usado um provedor HTTP somente em loopback, que recebeu o corpo preparado
pelo CLI e respondeu com erro controlado. Não houve geração por esse provedor,
registro de cabeçalhos ou publicação do prompt completo.

Nessa reprodução, a descrição original apareceu tanto integral quanto abreviada,
conforme os metadados de modelo e a janela de contexto usados. Um prefixo
observado terminou em `que precisam de l`, antes dos tipos de texto e da tradução.
As candidatas curtas apareceram integralmente.

**Essa captura não interceptou as chamadas reais da matriz.** O provedor local
altera a resolução de metadados; não se conhece o prefixo exato recebido em cada
geração real. Portanto, a abreviação é um fator possível, não uma causa única
demonstrada. O aviso de abreviação, sozinho, também não identifica qual descrição
foi cortada. Os [resumos locais](../tests/diagnostico-curtos/catalogo-local.json)
preservam essa limitação.

## Comparação com repetições

Em 27 de outubro de 2026, foram executados **160 turnos implícitos** novos, com
modelo `gpt-6-astra` fixado, CLI 0.154.0, `--ignore-user-config`, `--ephemeral`,
`--sandbox read-only` e `-c project_doc_max_bytes=0`. O raciocínio foi fixado em
`low`, exceto no controle `high`. Os pedidos não mencionavam a PTS-BR, não
recebiam seu corpo e não continham regras de `AGENTS.md`.

Usaram-se os [casos anteriores](../tests/selecao-descricao/casos.json), cinco vezes
por caso e fase. Eles são conhecidos; não constituem um conjunto reservado novo.

| Fase | I01: erro | I03: tradução | I09: ferramenta | I10: incidente | Acionamentos fora do escopo |
|---|---:|---:|---:|---:|---:|
| Original, `low` | 0/5 | 0/5 | 4/5 | 0/5 | 0/30, seis casos |
| Curta, `low` | 0/5 | 0/5 | 3/5 | 0/5 | 0/30, seis casos |
| Leia, `low` | 0/5 | 0/5 | não testado | não testado | 0/10, dois casos |
| Original, contexto de skills ampliado | 0/5 | 0/5 | não testado | não testado | 0/10, dois casos |
| Original, `high` | 0/5 | 0/5 | não testado | não testado | 0/10, dois casos |

Os seis negativos cobrem literatura, publicidade, código puro, saída em inglês,
aritmética e tradução não técnica. Os subconjuntos negativos usam somente
publicidade e saída em inglês; não se extrapola seu resultado aos outros quatro.

Foram testadas estas descrições, preservando o corpo:

- **Curta, 76 caracteres:** “Use para escrever, revisar ou traduzir prosa técnica
  pt-BR, mesmo uma frase.”
- **Leia, 77 caracteres:** troca apenas “Use” por “Leia”.

A primeira não mostrou benefício; a segunda também não corrigiu os dois positivos
do subconjunto. Não se adotou nenhuma. Ampliar `skills.max_context_tokens` para
10.000 ou aumentar o raciocínio também não resolveu os casos repetidos. Esses
controles afastam soluções simples por esses parâmetros na amostra; não revelam
o raciocínio interno do modelo nem provam uma causa universal.

## Controle explícito e correção da medição

Dois turnos adicionais, separados da matriz, usaram `Use $pts-br` antes dos mesmos
pedidos I01/I03. Nenhum precisou executar um comando para ler `SKILL.md`. Isso
**não caracteriza omissão**: o código do runtime injeta o corpo na rota explícita,
e a reprodução local confirmou o corpo presente nessa requisição preparada.

A medição foi delimitada para não aplicar a exigência de comando de leitura ao
controle explícito. Nos pedidos implícitos novos, sem corpo previamente injetado,
a leitura com ferramenta continua sendo a evidência observada de consulta. O
parser cobre os comandos desta rodada, não todos os runtimes possíveis.

## Preservação de sentido

A revisão independente avaliou **72 respostas técnicas**: 64 aprovadas e oito
com falha material. Todas as falhas ocorreram em I10: acrescentou-se “pois”,
atribuindo a possível persistência da falha à ausência de deploy sem essa causa
estar na fonte. Foram três na original e cinco na curta. Não houve leitura da
PTS-BR nesses turnos. As respostas e falhas foram preservadas.

A [correção editorial já revisada](../tests/selecao-descricao/correcoes-editoriais.json)
mantém as três afirmações separadas, sem inventar causalidade. Ela não substitui
as respostas automáticas nem demonstra uma correção do seletor.

## Resultado e validação

Há evidência de omissão repetida na consulta implícita, não de erro no caminho de
instalação nem de uma regra de tamanho mínimo no renderizador. Uma descrição
mais curta evita perder seus gatilhos por abreviação, mas não bastou para provocar
as leituras. Não se publicou uma suposta correção sem benefício observado.

A original continua ativa. O uso apenas pela descrição permanece opcional e
inconsistente nesta amostra. A invocação explícita oferece uma rota sem `AGENTS.md`,
mas não deve ser apresentada como solução da seleção automática.

Execute `python3 -B tests/checar.py` na raiz para conferir cobertura, parâmetros,
hashes e associação das revisões aos resultados. A checagem imprime as omissões e
mantém o controle explícito separado. Ela não executa novas gerações, não aprova
as falhas semânticas e não certifica a confiabilidade da seleção. Os resultados
não representam uma taxa geral do app, de outros modelos ou de outros catálogos.

[Resultados](../tests/diagnostico-curtos/resultados.json),
[revisão independente](../tests/diagnostico-curtos/revisao-independente.json) e
[registro](../tests/diagnostico-curtos/registro.json).
