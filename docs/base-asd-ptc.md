# Adaptação conjunta de ASD-STE100 e PTC

Esta rodada acrescenta 24 casos à bateria original de 28. Os casos foram
executados antes dos ajustes de comportamento e depois deles. Foram geradas 56
respostas: 24 no controle, 24 na comparação, quatro de regressão e quatro após
um ajuste localizado nos campos textuais.

## Contribuição de cada base

| Princípio | Base | Aplicação em português | Casos |
|---|---|---|---|
| Condição antes da ação e preservação de avisos | ASD-STE100 Skill | Preservar nível, código, condições e proibições; não inventar medidas de segurança. | P01–P04, P06 |
| Uma ação principal por frase | ASD-STE100 Skill | Aplicar também em valores textuais editáveis, sem criar linhas ou chaves no formato. | C01, C02, L04 |
| Leitura sem contexto de outro agente | ASD-STE100 Skill | Explicitar referentes conhecidos quando cada trecho for entregue isoladamente. | P05, C03 |
| Limites de vocabulário e conformidade | ASD-STE100 Skill | Distinguir revisão editorial, conferência de glossário e certificação normativa. | C06 |
| Conectores e escopo de adjetivos | PTC | Não escolher causalidade, temporalidade ou alcance do modificador sem contexto. | R01–R03 |
| Léxico dependente do sentido | PTC, adaptado | Preservar ressalvas factuais e usos legítimos de palavras, sem aplicar proibições gerais. | R04–R06 |
| Termos técnicos com vários sentidos | Ambas | Usar glossário de domínio e distinguir conceitos em estatística, manutenção, transporte e software. | L01–L06 |

As seções consultadas e versões estão na [base documental](../references/referencias.md).
Os princípios são adaptados; a skill não distribui o dicionário oficial ASD nem
reproduz todas as prescrições da PTC.

## Resultado observado

Os 24 casos do controle preservaram o sentido na revisão manual. As orientações
acrescentadas tornam explícitos critérios que já funcionavam em muitos exemplos;
não são apresentadas como correções de 24 defeitos.

Na comparação, um valor de CSV manteve duas ações na mesma frase: “Abra o arquivo
e, em seguida, aguarde”. O sentido estava preservado, mas a estrutura contrariava
a preferência rigorosa por uma ação por frase. Foi acrescentada uma orientação
específica para campos textuais editáveis, e C01 foi repetido com C02, L04 e a
regressão F03. O resultado de C01 passou a “Abra o arquivo. Em seguida, aguarde”,
com a mesma linha e coluna de CSV.

A revisão manual dos 24 resultados finais aprovou sentido e requisitos dos casos.
Quatro regressões da bateria anterior verificaram condições compartilhadas,
glossário do usuário, texto já claro e JSON com pendência. As checagens mecânicas
das duas baterias também passaram.

## O que foi implementado

- Maior rigor para avisos operacionais e mensagens consumidas isoladamente.
- Preservação explícita de nível, código e alcance dos avisos.
- Disciplina de frase dentro de valores textuais, respeitando o formato.
- Distinção entre conferir uma lista fornecida e certificar uma norma.
- Exemplos de conectores, adjetivos coordenados e ressalvas que limitam evidência.
- Opção `--casos` no verificador, para acrescentar baterias sem substituir a original.

Os testes da nova opção foram escritos antes da implementação: o CLI rejeitava
`--casos`. Depois do ajuste, um resultado válido da bateria externa foi aceito e
um literal alterado continuou sendo rejeitado.

## Repetir e auditar

```sh
python3 tests/verificar.py tests/resultados.json
python3 tests/verificar.py --casos tests/casos-asd.json tests/resultados-asd.json
python3 -B tests/test_verificar.py
```

Os [casos](../tests/casos-asd.json), [resultados anteriores](../tests/resultados-asd-anterior.json),
[intermediários](../tests/resultados-asd-intermediarios.json) e
[finais](../tests/resultados-asd.json) ficam disponíveis para comparação. Os
resultados finais de C01, C02 e L04 foram atualizados pela repetição localizada;
os demais foram mantidos da comparação, pois essa alteração se restringiu a
campos textuais estruturados. F03 foi conferido na repetição de regressão.

CSV, XML e YAML também receberam conferência sintática separada na rodada.
O verificador distribuído não é um validador universal desses formatos: seus
limites continuam sendo elementos literais e os contratos declarados nos casos,
com análise específica de JSON. A revisão semântica exige julgamento.

## Limites

Os exemplos de equipamentos são fictícios e servem à avaliação da linguagem;
não estabelecem valores seguros ou procedimentos técnicos certificados.
Os avaliadores geraram respostas em grupos independentes de seis casos sem
receber os critérios semânticos; o coordenador fez a revisão manual. Isso não
é uma taxa estatística de acerto nem substitui teste com os leitores reais.

As 28 respostas antigas não foram todas regeneradas nesta rodada. Foram
reexecutadas as checagens mecânicas e quatro casos semânticos relevantes.
