# Exportação controlada de registros do Atlas

Este procedimento é fictício e descreve uma exportação assistida para a equipe de operações.
O operador responsável pela janela deve ler o documento completo antes de iniciar.
As condições da janela também se aplicam à conferência e à retomada.

## Escopo da janela

Todas as ações das seções Preparação, Exportação, Conferência e Retomada só são permitidas quando estas condições forem atendidas:

- O ambiente é `hml-a`.
- A execução ocorre dentro da janela aprovada.
- Paula aprovou a execução no ticket `CHG-241`.

A aprovação de Paula não dispensa a confirmação do operador de que o destino é `hml-a`.
Nenhuma aprovação deste procedimento autoriza executar esses passos em produção.

Se faltar uma dessas condições, não inicie a sequência.
A única exceção é a leitura dos logs existentes para diagnóstico.
Essa leitura pode ocorrer fora da janela, sem criar uma exportação nem alterar registros.

## Preparação

AVISO [W-17]: A exportação pode conter registros duplicados se for retomada com outro identificador.
Antes de qualquer nova tentativa, confira o identificador da operação anterior.
Uma operação aceita ainda pode não ter começado.

O operador deve registrar no ticket o ambiente e o identificador `exp-241`.
Antes da exportação, execute a conferência somente de leitura abaixo.
Esse comando não aprova a janela e não altera o estado da origem.

```sh
atlasctl inspect --env hml-a --operation exp-241 --read-only
```

Se a conferência indicar uma exportação ainda em andamento com esse identificador, aguarde a conclusão dela.
Não crie uma segunda exportação.

Se não houver operação em andamento e todas as condições da janela continuarem atendidas, prossiga.

## Exportação

Somente depois de concluir a preparação, execute o comando abaixo:

```sh
atlasctl export --env hml-a --operation exp-241 --output /tmp/atlas-exp-241.json
```

A resposta `accepted` confirma apenas o recebimento da solicitação.
Não confirma que o arquivo foi criado, que a operação terminou ou que os registros foram conferidos.

Para consultar o estado da operação:

1. Aguarde pelo menos 90 segundos antes da primeira consulta de estado.
2. Faça no máximo seis consultas, com intervalo mínimo de 30 segundos entre elas.
3. Se a sexta consulta ainda não confirmar a conclusão, interrompa as consultas e registre o estado observado.

Não declare falha da exportação apenas porque esse limite de consultas foi atingido.

## Conferência

Após a confirmação de conclusão, o operador deve:

- Verificar a existência do arquivo.
- Comparar a contagem do arquivo com a contagem registrada no início da operação.

O arquivo só pode ser considerado conferido se as duas verificações passarem.

Se o arquivo não existir ou se as contagens divergirem:

- Preserve os arquivos e os logs.
- Registre a divergência.
- Não inicie a limpeza.

Não há autorização para corrigir a contagem alterando os dados exportados.

Somente após a conferência e a confirmação de recebimento por Paula, o operador pode excluir a cópia temporária.
Essa exclusão é permitida, não obrigatória.
O original da origem não deve ser excluído em nenhuma etapa deste procedimento.

## Retomada

Se a operação anterior falhar antes de produzir um arquivo, o operador pode usar `--resume-from exp-241` na mesma janela.
Essa permissão depende de a aprovação continuar válida e de não existir outra execução em andamento.

Se a janela tiver encerrado, obtenha nova aprovação antes de retomar.
As condições da seção Escopo da janela também se aplicam à retomada.

Este texto não define como resolver uma divergência nas contagens.
Encaminhe o caso para Paula sem descartar a evidência.
