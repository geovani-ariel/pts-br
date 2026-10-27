# Relato fictício: atraso nas exportações do Atlas

Este relato registra o que sabemos a partir dos logs e das mensagens fornecidas.
Ele não substitui uma análise de causa. Todos os horários abaixo são de 20 de
outubro de 2026, em UTC-3. A janela observada vai de 09:54 a 10:12; não sabemos
se houve impacto antes ou depois dela.

## Contexto e sinais observados

Na amostra disponível, 14 de 210 requisições de criação de exportação retornaram
`503`. São requisições, não 14 clientes distintos. Não temos a quantidade de
pessoas afetadas nem dados suficientes para estimar perda de arquivos. As demais
196 requisições receberam `202`, o que confirma aceitação, sem confirmar conclusão
ou entrega. Não foi observada exclusão de arquivos nos logs consultados; isso
não prova ausência de exclusão em todo o ambiente.

Às 09:50, uma nova versão havia sido publicada. Essa publicação antecede a janela
observada, mas a proximidade não comprova relação causal. Às 09:58, havia operações
com `state=accepted`; o material fornecido não mostra quando elas começaram.

## Linha do tempo

| Horário | Registro disponível |
|---|---|
| 09:54 | Primeira resposta `503` na amostra entregue à análise. |
| 09:58 | Operações ainda observadas em `state=accepted`. |
| 10:02 | O suporte relatou um timeout na operação `exp-77`. |
| 10:04 | Uma resposta da operação `exp-77` chegou ao cliente de teste. |
| 10:08 | A equipe desativou `exports_batch_v2` somente em homologação. |
| 10:12 | Última resposta `503` da amostra fornecida. |
| 11:20 | Os testes locais disponíveis passaram com a correção candidata. |

O relato do timeout ocorreu antes da chegada da resposta de `exp-77`. Os logs
fornecidos não fixam o instante em que o timeout ocorreu. A resposta das 10:04
foi recebida por um cliente de teste; não temos confirmação de entrega dos
arquivos aos demais destinatários.

## Hipótese e alcance das ações

A equipe suspeita de saturação do pool de conexões. A hipótese é compatível com
parte dos sintomas, mas não foi confirmada. Não houve medição do pool durante
a janela. Também foi levantada a possibilidade de um problema na fila; o material
não permite escolher entre as hipóteses nem afirmar que sejam excludentes.

A desativação de `exports_batch_v2` às 10:08 ocorreu somente em homologação.
Não foi uma alteração em produção e não comprova mitigação do impacto em produção.
As permissões dos tokens não foram alteradas. Não há autorização neste relato
para alterar credenciais, reprocessar requisições ou excluir arquivos.

## Situação da correção e próximos passos

Às 11:20, os testes locais disponíveis passaram com a correção candidata no
commit `a1b2c3d`. Não houve deploy dessa correção nos dados fornecidos. O resultado
local não demonstra que o problema tenha sido resolvido em produção. Uma falha
pode continuar ocorrendo mesmo após os testes locais passarem.

A equipe pretende comparar os logs da fila com os da API, se esses logs forem
fornecidos. O acesso a essa segunda fonte ainda não foi concedido. O suporte
já prestado aos integradores está registrado, mas a existência de um canal
disponível não comprova que cada pessoa tenha sido atendida.

Até obtermos esses dados, mantemos o incidente como investigação em andamento.
A falta de um novo alerta depois de 10:12 não basta para declarar recuperação.
Preservamos esta ressalva porque, hoje, nossa conclusão depende apenas da amostra
fornecida, e não de uma verificação de todo o ambiente.
