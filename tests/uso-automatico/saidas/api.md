# API fictícia de exportações do Atlas

Esta página descreve o contrato para integrações internas. Os exemplos servem
para leitura; os endereços usam o domínio reservado `example`.

Neste documento, request em prosa significa requisição HTTP; operation significa
operação. O termo job permanece job e não implica que exista agendamento.
Os nomes dos campos, estados, cabeçalhos e mensagens entre crases fazem parte do
contrato literal.

## Autenticação e acesso

Use `Authorization: Bearer $ATLAS_TOKEN`. O token identifica o cliente, mas não
comprova autorização sobre qualquer organização.

As permissões exigidas são:

- Para criar uma exportação: `exports:write` na organização informada por `X-Org-Id`.
- Para consultar uma exportação: `exports:read` nessa mesma organização.

Ter permissão de leitura não autoriza criar exportações. O contrato não descreve
como obter ou renovar credenciais.

## Criar uma operação

Envie `POST /v1/exports`. O corpo deve conter `range`. Os campos `from` e `to` de
`range` são datas ISO 8601 inclusivas. O campo `dry_run` é booleano e vale `false`
quando omitido.

O exemplo de requisição é literal:

```json
{"range":{"from":"2026-10-01","to":"2026-10-07"},"dry_run":false}
```

```sh
curl -X POST https://api.atlas.example/v1/exports -H 'Authorization: Bearer $ATLAS_TOKEN' -H 'X-Org-Id: org-demo' -H 'Idempotency-Key: exp-demo-17' -H 'Content-Type: application/json' --data '{"range":{"from":"2026-10-01","to":"2026-10-07"},"dry_run":false}'
```

O código `202` indica que a requisição foi aceita. Esse código não garante que o
job tenha começado, que tenha terminado ou que um arquivo esteja disponível.
A resposta inicial tem este formato:

```json
{"id":"exp-demo-17","state":"accepted","attempts":0,"file_url":null}
```

### Idempotência

O cabeçalho `Idempotency-Key` é obrigatório na criação e é reconhecido por 24 horas.
Durante esse período:

- A mesma chave com o mesmo corpo retorna a mesma operação.
- A mesma chave com outro corpo retorna `409`.

Depois desse período, a chave pode criar uma nova operação. O cliente não deve
presumir deduplicação permanente.

## Consultar e interpretar o estado

Use `GET /v1/exports/{id}`. Uma resposta `200` confirma a consulta ao registro,
mas não confirma o sucesso da exportação.

A visão consultada pode estar atrasada em até 30 segundos em relação ao
processamento. Essa tolerância não é um prazo de conclusão.

| Estado literal | Significado |
|---|---|
| `accepted` | Recebimento confirmado; início ainda não confirmado. |
| `running` | Processamento em andamento. |
| `completed` | Processamento concluído; conferir `file_url` para a disponibilidade do arquivo. |
| `failed` | Falha registrada; o contrato não informa recuperação automática. |

Mesmo em `completed`, `file_url` pode ser `null` até a publicação do arquivo.
A disponibilidade do arquivo e a confirmação de entrega ao destinatário são fatos
diferentes. Esta página não define uma confirmação de entrega.

## Paginação e valores

A listagem `GET /v1/exports` aceita `limit` inteiro de 1 a 100. O valor padrão é 50.

O valor de `next_cursor` é opaco e não deve ser reconstruído pelo cliente.
Um valor `null` encerra a enumeração do snapshot consultado, sem impedir que novos
registros surjam depois. Um cursor expirado retorna `410`. A API não promete
reinício transparente da listagem.

O campo `ratio` é uma string decimal entre `"0.00"` e `"1.00"`. Não é um percentual
nem um número JSON. Preserve esse tipo no exemplo:

```json
{"items":[],"next_cursor":null,"limit":50,"ratio":"0.05"}
```

## Falhas e novas tentativas

| Código literal | Tratamento previsto |
|---|---|
| `401` | Credencial ausente ou inválida; não repetir sem corrigir a autenticação. |
| `403` | Acesso negado; não repetir com o mesmo contexto esperando autorização. |
| `409` | Conflito de idempotência; não trocar a chave para contornar o conflito. |
| `429` | Aguardar pelo menos o intervalo de `Retry-After` antes de nova tentativa. |
| `503` | Indisponibilidade transitória; uma nova tentativa é permitida, sem garantia de êxito. |

O servidor inclui `Retry-After` em `429`, mas esta página não garante esse cabeçalho
em `503`.

A mensagem literal `Export accepted; delivery unconfirmed` não deve ser usada como
confirmação de entrega.

Este contrato não estabelece um orçamento máximo de tentativas nem autoriza
tentativas ilimitadas.
