# Testes e limites da avaliação

## Rodada documentada

Na rodada de 25 de outubro de 2026, foram geradas e revisadas 100 respostas:

| Versão | Casos | Resultado semântico observado |
|---|---:|---|
| Anterior | 24 | 24 aprovados |
| Compacta inicial | 24 | 22 aprovados |
| Compacta revisada | 24 | 23 aprovados |
| Final conservadora | 28 | 28 aprovados |

As candidatas compactas foram descartadas porque perderam uma limitação da
fonte e trocaram suporte fornecido por suporte disponível. A versão conservadora
preservou a estrutura das instruções e acrescentou verificações focadas.

Quatro casos foram reservados à rodada final, sem orientar os ajustes das
candidatas. Depois dessa rodada, foram acrescentados os materiais de publicação
e o campo de licença; esses acréscimos não mudaram as regras de reescrita.

## Executar as checagens

Requer apenas Python 3, sem pacotes externos. Na raiz do repositório:

```sh
python3 tests/verificar.py --selftest
python3 tests/verificar.py tests/resultados.json
```

[casos.json](../tests/casos.json) contém os pedidos e critérios semânticos.
[resultados.json](../tests/resultados.json) contém as respostas da rodada final.
O [verificador](../tests/verificar.py) confere elementos literais, chaves, tipos,
valores fixos e contratos de saída. O autoteste aceita um controle válido e
rejeita seis controles inválidos.

## Gerar uma nova amostra

Disponibilize [SKILL.md](../SKILL.md) e suas referências a um agente. Forneça
somente os campos `id` e `prompt` dos casos, sem os critérios esperados. Peça
que cada pedido seja tratado independentemente e que o resultado seja uma lista:

```json
[{"id":"S01","resposta":"Texto integral entregue pelo agente."}]
```

`resposta` deve ser sempre string, inclusive quando seu conteúdo for um objeto
JSON. Salve as respostas em outro arquivo e execute:

```sh
python3 tests/verificar.py /caminho/para/novas-respostas.json
```

Depois, confira os critérios semânticos manualmente. `--parcial` pode ser usado
quando alguns casos não foram executados, mas essa opção não permite relatar
cobertura da bateria completa.

## O que o resultado não demonstra

O verificador não chama modelos nem decide equivalência de sentido. Uma resposta
pode respeitar o JSON e ainda perder um fato, como ocorreu nas candidatas.

Os casos foram executados em grupos com contextos novos. O agente coordenador
fez a revisão manual, sem uma segunda banca independente. São amostras
sintéticas, sem taxa estatística de acerto, teste com leitores reais ou prova de
conformidade normativa.

O caso com instrução embutida também foi executado sob uma proibição explícita
do avaliador de executar comandos citados. Portanto, não é um teste isolado de
resistência a instruções maliciosas. Latência, custo e tokens faturados não foram
medidos.
