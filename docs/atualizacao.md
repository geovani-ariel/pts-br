# Atualização, versão específica e recuperação

A manutenção é uma ação explícita do usuário. A PTS-BR não acessa a rede para
consultar versões durante a revisão nem instala atualizações por conta própria.
Os comandos abaixo usam `skills@1.7.4`, a versão do instalador efetivamente
testada. `@latest` é a versão do CLI; não é uma seleção da versão da skill.

## Antes de alterar a instalação

1. Abra o arquivo `VERSION` na pasta `pts-br` indicada pelo instalador e registre
   seu conteúdo. Consulte também o [changelog](../CHANGELOG.md).
2. Guarde suas alterações locais fora da pasta da skill. A reinstalação pode
   substituir arquivos e remover arquivos adicionados nessa pasta.
3. Escolha o escopo. Os exemplos usam `--global`; para instalação por projeto,
   execute na pasta do projeto e substitua por `--project` em `update` ou remova
   `--global` em `add`. Não instale uma segunda cópia em outro escopo para tentar
   atualizar a primeira.

Consulte novas versões nos [releases do GitHub](https://github.com/geovani-ariel/pts-br/releases).
Essa consulta não altera a instalação. A PTS-BR não possui notificação automática.

## Acompanhar a branch padrão

Se a origem registrada for o repositório sem uma tag fixada:

```sh
npx skills@1.7.4 update pts-br --global
```

Isso acompanha a origem registrada, que pode incluir mudanças posteriores ao
último release. Para escolher um pacote publicado, prefira uma tag explícita.

**Não trate `check` como consulta sem alterações no CLI 1.7.4.** Nessa versão,
`check` e `update` chamam a mesma rotina. Um controle isolado com hash registrado
desatualizado confirmou a reinstalação e a substituição de `VERSION` ao executar
`check pts-br --project --yes`. A
[referência online do CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
descreve uma consulta sem reinstalação; o teste observou comportamento diferente.
Essa observação é específica da versão testada, não uma garantia para versões futuras.

## Instalar uma versão publicada

Use o endereço da tag, preservando o nome da skill e o agente:

```sh
npx skills@1.7.4 add https://github.com/geovani-ariel/pts-br/tree/v0.1.1 --skill pts-br --agent codex --global --copy
```

O instalador identifica a origem como `pts-br.git @ v0.1.1`. Uma tag é uma
referência de publicação; o commit e o checksum dos artefatos permitem conferir
seu conteúdo. No projeto, `skills-lock.json` registra a origem e a referência.
Preserve esse arquivo se quiser manter esse registro.

Não use `geovani-ariel/pts-br@v0.1.1` para selecionar a versão: a sintaxe com `@`
no nome da origem pode selecionar o nome de uma skill. A URL `/tree/v0.1.1`
foi a forma escolhida para este procedimento.

Uma instalação por tag permanece nessa referência ao executar `update`.
O comando não escolhe automaticamente a próxima tag. Para mudar de versão,
reexecute `add` com a URL desejada.

## Retornar à versão anterior

Para retornar da v0.1.1 à v0.1.0 no mesmo escopo:

```sh
npx skills@1.7.4 add https://github.com/geovani-ariel/pts-br/tree/v0.1.0 --skill pts-br --agent codex --global --copy
```

Confira `VERSION` e abra uma nova conversa para usar a cópia reinstalada. Se sua
instalação estiver em outro escopo, ajuste o comando conforme a seção inicial.
Para retornar a outra versão, use a tag que você registrou antes da alteração;
não suponha que v0.1.0 será sempre a versão anterior.

Para deixar de fixar uma tag e acompanhar novamente a branch padrão:

```sh
npx skills@1.7.4 add geovani-ariel/pts-br --skill pts-br --agent codex --global --copy
```

## Instalação a partir de ZIP ou pasta local

Uma cópia manual não registra automaticamente a origem remota no Skills CLI.
Uma instalação com `add ./pts-br` registra uma origem local; isso também não
estabelece acompanhamento do GitHub. No teste por projeto, `update` não encontrou
uma origem atualizável e terminou com código zero. Portanto, esse código sozinho
não confirma uma atualização.

Para migrar uma instalação local para uma versão remota gerenciada pelo CLI,
faça backup, use `add` com a URL da tag no mesmo escopo e confirme `VERSION`.
Não é necessário remover primeiro a skill para usar o procedimento testado.
Se preferir manter a cópia manual, baixe o ZIP do release desejado, confira o
checksum publicado e substitua a pasta após preservar suas alterações.

## Validação do procedimento

Os testes usam pastas de projeto isoladas, com `--copy --yes`, no Codex, em macOS,
Node.js 24.15.0 e Skills CLI 1.7.4. O escopo global não foi sobrescrito pelo CLI.
Os exemplos globais usam a opção de escopo documentada; a execução real foi por
projeto, sem redefinir `HOME` ou `CODEX_HOME`.

O ciclo prepara a candidata 0.1.1 em pasta local e usa a tag remota v0.1.0 para
validar a instalação por referência e a recuperação. O registro completo dos
resultados fica abaixo; não é um teste de comportamento linguístico da skill.

| Verificação | Resultado observado |
|---|---|
| Instalar a tag remota v0.1.0 | 45 arquivos idênticos à tag e `ref: v0.1.0` no lock do projeto. |
| Reinstalar no mesmo local a candidata 0.1.1 | 46 arquivos idênticos à candidata e `VERSION` igual a 0.1.1. |
| Retornar à tag remota v0.1.0 | Os 45 arquivos originais foram restaurados; o arquivo exclusivo da candidata foi removido; a origem voltou a ser GitHub com a tag registrada. |
| Executar `check` no controle isolado | Houve reinstalação; não foi uma consulta sem alterações. |
| Executar `update` com origem local | Nenhuma origem atualizável encontrada; saída zero não comprovou atualização. |

A comparação conferiu o conjunto de arquivos e os bytes, não apenas a mensagem
de sucesso do instalador. A candidata foi identificada por `VERSION`; ainda não
era uma tag remota nessa etapa. Os testes não demonstram comportamento idêntico
em outros agentes, sistemas operacionais ou versões futuras do instalador.
