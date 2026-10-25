# PTS-BR — Português Técnico Simplificado Brasileiro

Skill para escrever, revisar e traduzir textos técnicos em português brasileiro.
O objetivo é reduzir ambiguidades sem perder fatos, condições, exceções ou grau
de certeza. Inclui um glossário que distingue traduções preferidas, termos
mantidos no original e decisões que dependem do contexto.

## Instalação pelo Skills CLI

Requer Node.js e npm para executar o instalador. A versão do CLI validada foi
`skills@1.7.4`, com Node.js `>=22.20.0`. A skill em si é Markdown e não exige
dependências, chave de API ou acesso à rede durante a revisão de um texto.

### Codex — disponível em todos os projetos

```sh
npx skills@latest add geovani-ariel/pts-br --skill pts-br --agent codex --global --copy
```

`--global` instala para o usuário. `--copy` cria uma cópia, sem depender de um
link simbólico para a pasta de origem. Abra uma nova conversa após instalar.

### Somente no projeto atual

Na pasta do projeto que vai usar a skill, execute:

```sh
npx skills@latest add geovani-ariel/pts-br --skill pts-br --agent codex --copy
```

### A partir de uma pasta local

Depois de extrair o ZIP, execute na pasta que contém `pts-br`:

```sh
npx skills@latest add ./pts-br --skill pts-br --agent codex --copy
```

Para descobrir a skill sem instalar:

```sh
npx skills@latest add geovani-ariel/pts-br --list
```

Para consultar e atualizar uma instalação global feita pelo CLI:

```sh
npx skills@latest list --global --agent codex
npx skills@latest update pts-br --global
```

Outros agentes podem ser selecionados por `--agent`, conforme a
[documentação oficial do Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).
A validação deste projeto cobre o Codex. Para desativar a telemetria do CLI,
defina `DISABLE_TELEMETRY=1`, conforme a [documentação de telemetria](https://skills.sh/docs/cli).

## Uso

### Migração do nome anterior

O identificador anterior era `portugues-claro`. Se você o instalou pelo Skills
CLI, remova essa instalação e instale `pts-br`, evitando duas cópias da mesma skill:

```sh
npx skills@latest remove portugues-claro --global --agent codex
npx skills@latest add geovani-ariel/pts-br --skill pts-br --agent codex --global --copy
```

### Pedidos no chat

No chat do agente:

```text
Use $pts-br para revisar este procedimento sem alterar as condições:
[texto]
```

Outros pedidos possíveis:

```text
Use $pts-br para traduzir esta descrição de ferramenta para pt-BR.
Use $pts-br no modo natural e preserve o tom deste comunicado.
Use $pts-br e mostre antes/depois com os motivos das mudanças.
```

A saída padrão contém somente o texto revisado. Quando faltar informação para
eliminar uma ambiguidade, a skill registra uma pendência. Formatos explícitos,
como JSON, continuam tendo de respeitar o contrato do pedido.

## Exemplo

**Antes**

> Somente em homologação e após aprovação, exporte os registros e exclua a cópia temporária apenas se a exportação terminar sem erros.

**Depois**

> Execute estes passos somente em homologação e após aprovação:
>
> 1. Exporte os registros.
> 2. Exclua a cópia temporária apenas se a exportação terminar sem erros.

O cabeçalho preserva as condições das duas ações. Há outros casos comentados em
[exemplos](examples/antes-depois.md).

## Como as decisões são tomadas

- **Rigoroso:** instruções, mensagens de erro, prompts e descrições de ferramentas.
- **Natural:** explicações, documentação e comunicados, preservando o tom.
- **Tradução:** o glossário do pedido prevalece sobre o do projeto, e ambos sobre
  a base da skill. Código, identificadores, mensagens literais e rótulos reais
  de interface permanecem protegidos no escopo da revisão.

Veja [como funciona](docs/como-funciona.md), o [glossário](references/glossario.md)
e as [regras com exemplos](references/regras.md).

## Fontes

| Referência | Contribuição |
|---|---|
| ABNT NBR ISO 24495-1:2024 — Linguagem simples | Leitor, finalidade, organização, compreensão e uso. Veja o [escopo da ISO](https://www.iso.org/standard/78907.html). |
| [Microsoft — guia de localização pt-BR](https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides) | Tradução por contexto, terminologia, siglas e nomes de produto. |
| [Português Técnico Controlado](https://github.com/kayquer/portugues-tecnico-controlado) | Ambiguidades próprias do português e organização do glossário. |
| [ASD-STE100 Skill](https://github.com/danyuchn/asd-ste100-skill) | Estrutura de instruções, condições, avisos e textos consumidos por agentes. |

As seções e versões consultadas, as adaptações e os conflitos entre fontes estão
documentados em [referências](references/referencias.md) e
[proveniência](references/proveniencia.md). As traduções do glossário são
convenções editáveis, sem alegação de conformidade integral ou certificação.

## Testes

A rodada documentada gerou 100 respostas ao comparar versões. A versão final
daquela rodada passou nos 28 casos da amostra, com checagens mecânicas e revisão
semântica manual. Os casos cobrem condições, modalidade, traduções, datas,
elementos literais e formatos de saída.

```sh
python3 tests/verificar.py --selftest
python3 tests/verificar.py tests/resultados.json
python3 tests/verificar.py --casos tests/casos-asd.json tests/resultados-asd.json
python3 tests/verificar.py --casos tests/casos-dificeis.json tests/resultados-dificeis.json
python3 -B tests/test_verificar.py
```

O verificador usa apenas a biblioteca padrão do Python. Ele confere respostas
salvas; não chama modelos nem prova equivalência semântica. Veja
[método e limitações](docs/testes.md).

A bateria complementar acrescenta 24 casos baseados em ASD-STE100 e PTC,
totalizando 52 casos distintos nas duas baterias. Inclui procedimentos fictícios,
avisos, mensagens isoladas para agentes, linguagem estatística, glossários de
outros domínios, CSV, YAML, XML e ambiguidades próprias do português. Veja
[adaptações e resultados da rodada](docs/base-asd-ptc.md).

Uma terceira bateria acrescenta 24 casos difíceis de tradução e ambiguidade,
totalizando 76 casos distintos. Ela cobre escopo de negações e qualificadores
temporais, confirmação versus conclusão, cardinalidade, marcadores repetidos,
ICU e tradução bilíngue. Veja [problemas encontrados e correções](docs/rodada-dificil.md).

## Licença

[MIT](LICENSE). Copyright da adaptação: Geovani Paschoini, 2026.
O aviso de Dustin Yuchen Teng permanece no arquivo principal, e o aviso de
Kayque Rotondo está preservado em [LICENSE-PTC](LICENSE-PTC).

A licença deste projeto não altera os direitos sobre normas e guias externos.
O pacote não redistribui a norma ABNT, o guia integral da Microsoft ou o
dicionário oficial ASD-STE100.
