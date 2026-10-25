# Rodada de tradução e ambiguidade

Avaliação de 25 de outubro de 2026, partindo da versão
[3c9c2d4](https://github.com/geovani-ariel/pts-br/commit/3c9c2d47139bf0ce36202b9da55de3a71e225476).
Foram preparados 20 casos iniciais e quatro casos de transferência reservados
à validação da correção. A nova bateria soma 24 casos; as três baterias do
projeto contêm 76 casos distintos.

## Cobertura

Os casos cobrem ausência de obrigação versus proibição, negação modal ambígua,
condições necessárias que não são suficientes, quantificadores, cardinalidade,
ausência de confirmação, prazos mínimos e referentes ambíguos. Também verificam
porcentagens versus pontos percentuais, consistência eventual, glossários,
versões, identificadores, comentários de código, ICU, JSON e pares bilíngues.

Os casos reservados distinguem o momento de um evento, de um relato e de uma
confirmação. Não foram usados para redigir o exemplo da correção.

## Problemas encontrados

### D09 — deslocamento do qualificador temporal

A fonte dizia que o timeout foi **relatado antes** de a resposta chegar. A primeira
tradução permitia entender somente que o timeout havia **ocorrido antes**, sem
fixar o momento do relato. Uma revisão independente confirmou a ambiguidade
introduzida.

A correção exige preservar o verbo ou a afirmação a que o marcador temporal se
liga. Relato, evento e confirmação são tratados separadamente. Na nova execução:

> O relato de que o tempo limite foi excedido ocorreu antes de a resposta chegar.

D21–D24 verificaram a transferência dessa orientação a outros relatos, datas e
informações não verificadas.

### D02 — preservação sem entrega da tradução

Em “Requests may not be retried”, a primeira resposta preservou o inglês e
registrou a ambiguidade entre proibição e possibilidade. Isso evitava escolher
uma leitura, mas não entregava a tradução pedida. A primeira revisão aceitou o
fallback; outra revisão independente identificou a limitação de entrega.

A regra passou a exigir um equivalente que conserve a ambiguidade ou traduções
condicionais no idioma pedido. A nova execução apresentou as duas leituras em
português, identificadas como hipóteses, com a pendência. Não impôs proibição nem
possibilidade como intenção confirmada da fonte.

### Verificador — repetição de marcadores

A presença de um marcador não comprova que suas ocorrências foram preservadas.
O verificador ganhou `ocorrencias_literais`, usado em D15 para exigir duas
ocorrências de `{name}`. A tradução gerada já conservava ambas, mas os testes
do verificador mostraram que uma resposta com apenas uma ocorrência, ou com
três, não era rejeitada.

Os testes negativos falharam antes do ajuste e passaram depois dele. Agora são
cinco testes unitários: dois da seleção de baterias e três da contagem literal.

## Validação

- 24 resultados finais passaram nas checagens mecânicas da nova bateria.
- A revisão semântica independente dos resultados encontrou D02 após a correção
  temporal. D01, D02, D17 e D19 foram repetidos após o ajuste de entrega; o mesmo
  revisor não encontrou falha material nesses quatro resultados atualizados.
- Os demais resultados foram preservados da execução já revisada. Eles não
  foram todos regenerados depois do ajuste localizado da tradução ambígua.
- Quatro regressões semânticas da bateria original verificaram condições,
  continuidade temporal, estados de publicação e JSON com pendência.
- As checagens mecânicas das duas baterias anteriores continuaram passando.
- O autoteste existente e os cinco testes unitários do verificador passaram.

Os geradores receberam apenas os pedidos, sem os critérios esperados. Os casos
iniciais foram executados em grupos de dez, em contextos novos; os quatro casos
reservados usaram outro contexto. A revisão foi feita pelo coordenador e por
agentes revisores independentes, sem validação com leitores humanos.

## Repetir e auditar

```sh
python3 tests/verificar.py --casos tests/casos-dificeis.json tests/resultados-dificeis.json
python3 tests/verificar.py --parcial --casos tests/casos-dificeis.json tests/resultados-dificeis-antes.json
python3 -B tests/test_verificar.py
```

Compare os [casos e critérios](../tests/casos-dificeis.json), os
[resultados anteriores](../tests/resultados-dificeis-antes.json), os
[intermediários](../tests/resultados-dificeis-intermediarios.json) e os
[finais](../tests/resultados-dificeis.json). As quatro
[regressões semânticas](../tests/resultados-regressao-dificeis.json) usam os casos
S02, S06, S08 e F03 de `tests/casos.json`.

Exemplo de contrato de repetição, sem exigir uma redação específica:

```json
{"id":"D15","ocorrencias_literais":{"{name}":2}}
```

A contagem é feita sobre o texto da resposta serializada. Não é uma análise
geral de sintaxe de templates ou de codificações equivalentes. A mensagem ICU
foi conferida por inspeção e pelo contrato JSON, sem parser ICU dedicado.

## Limites

Os resultados descrevem amostras, não uma taxa estatística de acerto. Conferir
literais e contratos não prova equivalência semântica. As ambiguidades que a
fonte não resolve continuam explícitas; a skill não escolhe atores, intenção
modal ou fatos para deixar o texto mais fluente.
