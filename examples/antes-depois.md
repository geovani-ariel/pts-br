# Exemplos comentados

Os exemplos ilustram decisões da skill. São textos sintéticos, sem certificação
normativa. As equivalências técnicas podem ser alteradas pelo glossário do pedido.

## 1. Instrução com condições compartilhadas

**Antes**

> Somente em homologação e após aprovação, exporte os registros e exclua a cópia temporária apenas se a exportação terminar sem erros.

**Depois**

> Execute estes passos somente em homologação e após aprovação:
>
> 1. Exporte os registros.
> 2. Exclua a cópia temporária apenas se a exportação terminar sem erros.

**Motivo:** o cabeçalho restringe os dois passos. O sucesso da exportação
continua sendo uma condição adicional para a exclusão.

## 2. Hipótese que deve continuar sendo hipótese

**Antes e depois**

> A falha pode ter sido causada por falta de permissão.

**Motivo:** o texto já está claro. Remover “pode ter sido” transformaria uma
causa possível em diagnóstico confirmado. A skill não força uma alteração.

## 3. Tradução de prosa com termos preservados

**Pedido:** traduzir para pt-BR usando o glossário da skill.

**Antes**

> Check the settings before the deploy. Review the branch before the merge.

**Depois**

> Verifique as configurações antes do deploy. Revise a branch antes do merge.

**Motivo:** “settings” recebe a tradução preferida. Os termos Git e de operação
seguem as convenções da base. Se o pedido fixar “implantação” para “deploy”,
essa preferência prevalece na prosa.

## 4. Código e rótulos reais

**Antes**

> Deverá ser realizada a execução de `npm run build`. Depois, clique no botão real “Create deployment”.

**Depois**

> Execute `npm run build`. Depois, clique no botão “Create deployment”.

**Motivo:** a prosa fica direta. O comando e o rótulo que o leitor precisa
reconhecer permanecem literais.

## 5. Referente ausente

**Antes**

> Marina avisou Carla que seu acesso seria removido amanhã.

**Depois**

> Marina avisou Carla que seu acesso seria removido amanhã.
>
> Pendente: informar se o acesso é de Marina ou de Carla.

**Motivo:** a fonte não identifica o titular. Escolher uma pessoa criaria uma
informação. Converter “amanhã” em uma data também exige conhecer a referência.

## 6. JSON com contrato preservado

**Pedido:** traduzir somente `message`, sem alterar os demais valores e sem
escrever nada fora do JSON.

**Antes**

```json
{"message":"The request may have failed.","code":"TIMEOUT","retry":false}
```

**Depois**

```json
{"message":"A solicitação pode ter falhado.","code":"TIMEOUT","retry":false}
```

**Motivo:** a mensagem continua incerta. As chaves, o código e o booleano
mantêm o contrato. As cercas Markdown aqui apresentam o exemplo; na tarefa
descrita, a resposta conteria somente o objeto JSON.

## 7. Estados que não são sinônimos

**Antes**

> The patch is available for download, but it has not been delivered to customer devices. Delivery does not imply installation.

**Depois**

> A correção está disponível para download, mas ainda não foi entregue aos dispositivos dos clientes. A entrega não implica instalação.

**Motivo:** disponibilidade, entrega e instalação continuam sendo estados
distintos. Uma revisão não deve transformar disponibilidade em entrega.

## 8. Localização com identificadores protegidos

**Origem:** inglês, com convenção numérica en-US.

**Antes**

> The coefficient is 0.05. The version is v1.5.0. The record ID is 00123.

**Depois**

> O coeficiente é 0,05. A versão é v1.5.0. O ID do registro é 00123.

**Motivo:** o coeficiente é localizado sem mudar seu valor. Versão e
identificador não são números comuns; seus pontos e zeros permanecem.
