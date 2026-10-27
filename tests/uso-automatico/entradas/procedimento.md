# Exportação controlada de registros do Atlas

Este procedimento é fictício. Ele descreve uma exportação assistida para a equipe
de operações. O operador responsável pela janela deve ler o documento completo
antes de iniciar, pois as condições da janela também valem para os passos de
conferência e de retomada, e não somente para a exportação.

## Escopo da janela

Todas as ações das seções Preparação, Exportação, Conferência e Retomada só são
permitidas no ambiente `hml-a`, dentro da janela aprovada e após a aprovação de
Paula no ticket `CHG-241`. A aprovação de Paula não dispensa a confirmação do
operador de que o destino é `hml-a`. Nenhuma aprovação deste procedimento autoriza
executar esses passos em produção. Se faltar uma dessas condições, não inicie a
sequência; a única exceção é a leitura dos logs existentes para diagnóstico, que
pode ocorrer fora da janela, sem criar uma exportação nem alterar registros.

## Preparação

AVISO [W-17]: A exportação pode conter registros duplicados se for retomada com
outro identificador. Antes de qualquer nova tentativa, confira o identificador
da operação anterior. Uma operação aceita ainda pode não ter começado.

O operador deve registrar no ticket o ambiente e o identificador `exp-241`.
Antes da exportação, execute a conferência somente de leitura abaixo. Esse
comando não aprova a janela e não altera o estado da origem.

```sh
atlasctl inspect --env hml-a --operation exp-241 --read-only
```

Se a conferência indicar uma exportação ainda em andamento com esse identificador,
aguarde a conclusão dela; não crie uma segunda exportação. Se não houver operação
em andamento e todas as condições da janela continuarem atendidas, prossiga.

## Exportação

Execute o comando abaixo somente depois de concluir a preparação:

```sh
atlasctl export --env hml-a --operation exp-241 --output /tmp/atlas-exp-241.json
```

A resposta `accepted` confirma apenas o recebimento da solicitação. Não confirma
que o arquivo foi criado, que a operação terminou ou que os registros foram
conferidos. Aguarde pelo menos 90 segundos antes da primeira consulta de estado.
Depois, faça no máximo seis consultas, com intervalo mínimo de 30 segundos entre
elas. Se a sexta consulta ainda não confirmar a conclusão, interrompa as consultas
e registre o estado observado; não declare falha da exportação só por esse limite.

## Conferência

Após a confirmação de conclusão, o operador deve verificar a existência do arquivo
e comparar sua contagem com a contagem registrada no início da operação. O arquivo
só pode ser considerado conferido se as duas verificações passarem. Se o arquivo
não existir ou se as contagens divergirem, preserve os arquivos e os logs, registre
a divergência e não inicie a limpeza. Não há autorização para corrigir a contagem
alterando os dados exportados.

Somente após a conferência e a confirmação de recebimento por Paula, o operador
pode excluir a cópia temporária. Essa exclusão é permitida, não obrigatória.
O original da origem não deve ser excluído em nenhuma etapa deste procedimento.

## Retomada

Se a operação anterior falhar antes de produzir um arquivo, o operador pode usar
`--resume-from exp-241` na mesma janela, desde que a aprovação continue válida e
não exista outra execução em andamento. Se a janela tiver encerrado, obtenha nova
aprovação antes de retomar. Este texto não define como resolver uma divergência
nas contagens; encaminhe o caso para Paula sem descartar a evidência.
