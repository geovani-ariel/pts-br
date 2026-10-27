# PTS-BR

Português Técnico Simplificado Brasileiro. Skill para escrever, revisar e
traduzir procedimentos, documentação, prompts e mensagens para agentes em pt-BR.
O foco é preservar fatos, condições, exceções, grau de certeza e terminologia.

[Instalação](#instalação) · [Atualização](#atualização) · [Como usar](#como-usar) · [Glossário](references/glossario.md) · [Exemplos](examples/antes-depois.md) · [Testes](#testes) · [Versões](CHANGELOG.md)

## Antes e depois

**Antes**

> Somente em homologação e após aprovação, exporte os registros e exclua a cópia temporária apenas se a exportação terminar sem erros.

**Depois**

> Execute estes passos somente em homologação e após aprovação:
>
> 1. Exporte os registros.
> 2. Exclua a cópia temporária apenas se a exportação terminar sem erros.

A condição de homologação e a aprovação continuam valendo para os dois passos.
A exclusão ainda depende do sucesso da exportação.

## Instalação

Para instalar no Codex e usar em todos os projetos:

```sh
npx skills@latest add geovani-ariel/pts-br --skill pts-br --agent codex --global --copy
```

Abra uma nova conversa após instalar. `--global` instala para o usuário;
`--copy` mantém uma cópia independente da pasta de origem.

O instalador usa Node.js e npm. Os comandos foram validados com `skills@1.7.4`,
que requer Node.js `>=22.20.0`. A skill é composta por arquivos Markdown e não
exige dependências, chave de API ou rede para revisar o texto fornecido.

<details>
<summary>Instalação por projeto, pasta local, atualização e migração</summary>

### Somente no projeto atual

Execute na pasta do projeto:

```sh
npx skills@latest add geovani-ariel/pts-br --skill pts-br --agent codex --copy
```

### A partir de uma pasta local

Depois de extrair o ZIP, execute na pasta que contém `pts-br`:

```sh
npx skills@latest add ./pts-br --skill pts-br --agent codex --copy
```

### Descobrir e consultar

Liste a skill no repositório sem instalar:

```sh
npx skills@latest add geovani-ariel/pts-br --list
```

Liste as skills instaladas globalmente:

```sh
npx skills@latest list --global --agent codex
```

### Migrar de `portugues-claro`

Se você instalou a versão com o nome anterior pelo Skills CLI, remova-a e
instale `pts-br` para evitar cópias duplicadas:

```sh
npx skills@latest remove portugues-claro --global --agent codex
npx skills@latest add geovani-ariel/pts-br --skill pts-br --agent codex --global --copy
```

### Outros agentes e telemetria

Outros agentes podem ser selecionados por `--agent`, conforme a
[documentação oficial do Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).
A instalação deste projeto foi validada no Codex. Para desativar a telemetria
do CLI, defina `DISABLE_TELEMETRY=1`, conforme a
[documentação de telemetria](https://skills.sh/docs/cli).

</details>

## Atualização

A PTS-BR não consulta atualizações nem altera a própria instalação durante uma
revisão de texto. Consulte os [releases](https://github.com/geovani-ariel/pts-br/releases)
e compare com o arquivo `VERSION` da pasta instalada indicada pelo CLI.

Para atualizar uma instalação global que acompanha a branch padrão do repositório:

```sh
npx skills@1.7.4 update pts-br --global
```

Antes de atualizar, guarde suas alterações locais e registre a versão instalada.
O comando pode substituir os arquivos. Em uma instalação por projeto, execute
na pasta do projeto e troque `--global` por `--project`.

**No `skills@1.7.4`, `check` pode atualizar arquivos:** ele usa a mesma rotina
que `update`. Não use esse comando como consulta sem alterações. `@latest`
seleciona a versão do CLI, não a versão da PTS-BR.

Para instalar uma versão específica, use a URL da tag. Exemplo de versão publicada:

```sh
npx skills@1.7.4 add https://github.com/geovani-ariel/pts-br/tree/v0.1.0 --skill pts-br --agent codex --global --copy
```

Reexecutar esse comando também permite retornar à v0.1.0. Uma instalação feita
por tag continua nessa referência ao usar `update`; para mudar de versão, use
`add` com a URL da tag desejada. Para voltar a acompanhar a branch padrão,
reexecute o comando de instalação sem `/tree/v0.1.0`.

Veja o [guia de atualização e recuperação](docs/atualizacao.md) para confirmar
versão, tratar cópias manuais e consultar o ciclo de instalação testado.

## Como usar

O Codex pode selecionar a skill pela descrição, mas isso não garante leitura em
todo pedido compatível. A [rodada sem AGENTS](docs/selecao-descricao.md) registrou
omissões em trechos curtos e traduções; as duas descrições candidatas não
resolveram o problema e foram rejeitadas. Para aplicá-la como padrão em
textos técnicos, registre essa preferência no `AGENTS.md` do seu ambiente.
A [rodada de uso automático](docs/uso-automatico.md) verificou essa política em
três documentos completos, sem mencionar a skill nos pedidos de revisão.

O [diagnóstico dos pedidos curtos](docs/diagnostico-pedidos-curtos.md) repetiu os
casos com duas descrições menores e controles de contexto e raciocínio, sem
encontrar uma correção comprovada. A descrição original permanece ativa.

A invocação explícita é opcional. No chat do agente:

```text
Use $pts-br para revisar este procedimento sem alterar as condições:
[texto]
```

Você também pode pedir tradução, escolher o modo ou comparar as alterações:

```text
Use $pts-br para traduzir esta descrição de ferramenta para pt-BR.
Use $pts-br no modo natural e preserve o tom deste comunicado.
Use $pts-br e mostre antes/depois com os motivos das mudanças.
```

Por padrão, a resposta contém somente o texto revisado. Quando a fonte for
ambígua, a skill conserva as leituras abertas ou indica o que falta esclarecer.
Notas e alternativas usam canais autorizados. Se não houver uma tradução fiel
no contrato nem um sinal de falha previsto, a skill suspende o artefato e pede
apenas o contexto ou ajuste necessário. Veja os [casos de contrato incompatível](docs/contratos-ambiguos.md).

## Regras de revisão e tradução

| Modo | Quando usar |
|---|---|
| Rigoroso | Procedimentos, avisos, erros, prompts, ferramentas e mensagens entregues isoladamente a agentes. |
| Natural | Explicações, documentação e comunicados, preservando tom e autoria. |

O glossário distingue termos que devem ser traduzidos, mantidos no original ou
resolvidos pelo contexto. O glossário do pedido prevalece sobre o do projeto;
ambos prevalecem sobre a base da skill. Para adotar decisões da equipe, copie o
[modelo de glossário do projeto](templates/glossario-projeto.md) e informe seu
caminho ao agente.

Código, comandos, identificadores, URLs, mensagens literais e rótulos reais de
interface permanecem protegidos no escopo da revisão. Marcadores temporais e
negações precisam continuar ligados à mesma ação ou afirmação do original.

Veja [como funciona](docs/como-funciona.md), o [glossário](references/glossario.md)
e as [regras detalhadas](references/regras.md). Os
[exemplos comentados](examples/antes-depois.md) cobrem condições compartilhadas,
hipóteses, código, JSON, CSV e traduções ambíguas.

## Testes

O repositório contém 108 casos focais em cinco baterias e três documentos
completos na [rodada de uso automático](docs/uso-automatico.md). A
[avaliação v0.1.2](docs/contratos-ambiguos.md) registra a execução dos 108 casos
focais contra a mesma cópia das instruções, com hashes dos arquivos avaliados:

| Bateria | Casos | Cobertura |
|---|---:|---|
| [Original](docs/testes.md) | 28 | Fidelidade, condições, terminologia, elementos literais e formatos de saída. |
| [ASD-STE100 e PTC](docs/base-asd-ptc.md) | 24 | Avisos, procedimentos, outros domínios técnicos, conectores e integração com agentes. |
| [Tradução e ambiguidade](docs/rodada-dificil.md) | 24 | Negação modal, escopo temporal, cardinalidade, marcadores, ICU e pares bilíngues. |
| [Estabilidade](docs/avaliacao-v0.1.0.md) | 12 | Reaplicação, substituição de nomes e valores, formatos equivalentes e ambiguidade em campos fechados. |
| [Ambiguidade e contratos incompatíveis](docs/contratos-ambiguos.md) | 20 | Tradução sem notas, limites rígidos e flexíveis, falha autorizada e suspensão antes de um artefato impossível. |

Para conferir as respostas salvas e executar os testes do verificador:

```sh
python3 -B tests/checar.py
```

O verificador usa apenas a biblioteca padrão do Python e confere contratos e
literais nas respostas salvas. Não chama modelos nem prova equivalência semântica.
Os 20 casos novos distinguem traduções entregues, impedimentos previstos no
contrato e comunicações de suspensão; essas últimas não contam como traduções
concluídas nem como cumprimento do formato impossível.
Os relatórios detalham as revisões manuais, correções e limites das amostras,
incluindo a comparação inicial de 100 respostas entre versões. A
[ficha de avaliação semântica](docs/avaliacao-semantica.md) padroniza os critérios
e a gravidade das falhas. O mesmo comando roda no GitHub Actions; ele não gera
novas respostas nem executa uma nova revisão semântica.

A versão do pacote está em [VERSION](VERSION), com mudanças documentadas no
[changelog](CHANGELOG.md). Os [releases](https://github.com/geovani-ariel/pts-br/releases)
identificam o commit publicado.

As instruções linguísticas da v0.1.2 permaneceram iguais na v0.1.3; os três
documentos acrescentam cobertura de condições entre seções e evidência de leitura
da skill sob a política de `AGENTS.md`.

A [seleção apenas pela descrição](docs/selecao-descricao.md) foi avaliada em
12 pedidos, com controles negativos e duas candidatas rejeitadas. As omissões
permanecem visíveis no relatório e no comando de checagem. A aprovação da
integridade no CI não significa aprovação de todos os acionamentos implícitos.

## Fontes

| Referência | Contribuição |
|---|---|
| ABNT NBR ISO 24495-1:2024 — Linguagem simples | Leitor, finalidade, organização, compreensão e uso. Veja o [escopo da ISO](https://www.iso.org/standard/78907.html). |
| [Microsoft — guia de localização pt-BR](https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides) | Tradução por contexto, terminologia, siglas e nomes de produto. |
| [Português Técnico Controlado](https://github.com/kayquer/portugues-tecnico-controlado) | Ambiguidades próprias do português e organização do glossário. |
| [ASD-STE100 Skill](https://github.com/danyuchn/asd-ste100-skill) | Estrutura de instruções, condições, avisos e textos consumidos por agentes. |

Consulte as [seções e versões utilizadas](references/referencias.md) e a
[proveniência da adaptação](references/proveniencia.md). As escolhas do glossário
são convenções editáveis. A PTS-BR não oferece certificação ou conformidade
integral com essas referências.

## Licença

[MIT](LICENSE). Copyright da adaptação: Geovani Paschoini, 2026.
O aviso de Dustin Yuchen Teng permanece no arquivo principal; o de Kayque
Rotondo está preservado em [LICENSE-PTC](LICENSE-PTC).

A licença do projeto não altera os direitos sobre normas e guias externos.
O pacote não redistribui a norma ABNT, o guia integral da Microsoft ou o
dicionário oficial ASD-STE100.
