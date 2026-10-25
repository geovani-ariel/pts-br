# Português claro

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
npx skills@latest add geovani-ariel/portugues-claro --skill portugues-claro --agent codex --global --copy
```

`--global` instala para o usuário. `--copy` cria uma cópia, sem depender de um
link simbólico para a pasta de origem. Abra uma nova conversa após instalar.

### Somente no projeto atual

Na pasta do projeto que vai usar a skill, execute:

```sh
npx skills@latest add geovani-ariel/portugues-claro --skill portugues-claro --agent codex --copy
```

### A partir de uma pasta local

Depois de extrair o ZIP, execute na pasta que contém `portugues-claro`:

```sh
npx skills@latest add ./portugues-claro --skill portugues-claro --agent codex --copy
```

Para descobrir a skill sem instalar:

```sh
npx skills@latest add geovani-ariel/portugues-claro --list
```

Para consultar e atualizar uma instalação global feita pelo CLI:

```sh
npx skills@latest list --global --agent codex
npx skills@latest update portugues-claro --global
```

Outros agentes podem ser selecionados por `--agent`, conforme a
[documentação oficial do Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).
A validação deste projeto cobre o Codex. Para desativar a telemetria do CLI,
defina `DISABLE_TELEMETRY=1`, conforme a [documentação de telemetria](https://skills.sh/docs/cli).

## Uso

No chat do agente:

```text
Use $portugues-claro para revisar este procedimento sem alterar as condições:
[texto]
```

Outros pedidos possíveis:

```text
Use $portugues-claro para traduzir esta descrição de ferramenta para pt-BR.
Use $portugues-claro no modo natural e preserve o tom deste comunicado.
Use $portugues-claro e mostre antes/depois com os motivos das mudanças.
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
| [ASD-STE100 Skill](https://github.com/danyuchn/asd-ste100-skill) | Inspiração inicial para aplicar linguagem controlada a textos consumidos por agentes. |

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
```

O verificador usa apenas a biblioteca padrão do Python. Ele confere respostas
salvas; não chama modelos nem prova equivalência semântica. Veja
[método e limitações](docs/testes.md).

## Licença

[MIT](LICENSE). Copyright da adaptação: Geovani Paschoini, 2026.
O aviso de Dustin Yuchen Teng permanece no arquivo principal, e o aviso de
Kayque Rotondo está preservado em [LICENSE-PTC](LICENSE-PTC).

A licença deste projeto não altera os direitos sobre normas e guias externos.
O pacote não redistribui a norma ABNT, o guia integral da Microsoft ou o
dicionário oficial ASD-STE100.
