# Tradução ambígua e contratos incompatíveis — v0.1.2

Rodada de 26 de outubro de 2026, partindo da v0.1.1, commit
[4b5e9bc](https://github.com/geovani-ariel/pts-br/commit/4b5e9bcf2ff9e9a63b785000666ea4db6e92c0fb).
Foram preparados 16 casos iniciais e quatro reservados para verificar a
transferência da primeira correção. A bateria tem 20 casos; o projeto soma
108 casos nas cinco baterias.

## O que foi encontrado

**X05 — pergunta entregue como tradução.** O pedido exigia um único campo JSON
reservado à tradução, sem notas. Na execução anterior, a resposta foi:

```json
{"texto":"Qual a modalidade?"}
```

O parser aceita esse objeto, mas um consumidor pode exibir a pergunta como se
fosse a tradução. O controle sem a skill apresentou outro texto de impedimento
no mesmo campo. A revisão classificou ambas as respostas como falha material.

A instrução agora distingue um equivalente que mantém a ambiguidade, um sinal
de impedimento autorizado e uma comunicação anterior ao artefato. Sem canal de
falha, a skill suspende a entrega em vez de inventar campos ou colocar uma
pergunta no local reservado à tradução.

**X05 — aumento de limite sem necessidade demonstrada.** A primeira correção
solicitou a modalidade corretamente, mas afirmou que o limite de 20 caracteres
precisava aumentar. Essa afirmação não estava demonstrada: se o sentido fosse
proibitivo, “Não repetir pedidos.” caberia em 20 caracteres. A regra passou a
pedir apenas o contexto ou ajuste necessário. Na execução final, a resposta foi:

> A frase proíbe repetir as solicitações ou indica que elas podem não ser repetidas?

Essa pergunta suspende a tradução; não é uma saída no contrato JSON original.
Depois da resposta do usuário, o tamanho da tradução pode ser conferido.

**Verificador — limite dentro de JSON.** A checagem anterior só tinha limite da
resposta inteira. Foi acrescentado `max_caracteres_campos`, aplicado aos valores
textuais depois de decodificar o JSON. Dois controles negativos falharam antes
do ajuste: um valor acima do limite e um valor nulo no lugar de texto limitado.
Agora são rejeitados. Um controle com escapes Unicode confirma que a sintaxe
JSON não entra na contagem do valor.

## Desfechos dos 20 casos novos

A aprovação avalia a fidelidade da conduta, sem contar todo resultado como uma
tradução concluída:

| Desfecho observado | Casos | Interpretação |
|---|---:|---|
| Tradução | 8 | Equivalente fiel, dentro do contrato, sem notas desnecessárias. |
| Bloqueio autorizado | 4 | Impedimento comunicado pelo marcador ou esquema previsto no pedido. |
| Esclarecimento | 7 | Comunicação anterior ao artefato para resolver contexto ou limite. |
| Bloqueio sem canal | 1 | Impedimento mínimo, sem perguntas, conforme a restrição do caso. |

As oito suspensões das duas últimas linhas não satisfazem o formato ou limite
do artefato impossível. Elas interrompem a produção para não escolher um sentido,
omitir fatos ou simular uma tradução concluída. Quando existe um canal de falha
autorizado, ele prevalece sobre texto externo.

Há também controles que impedem bloquear traduções possíveis. “The key is valid”
pode virar “A chave é válida” sem decidir o tipo de chave. “Deve” pode conservar
leituras de expectativa e obrigação quando ambas permanecerem abertas na fonte.
Um limite preferencial cede à precisão; um limite rígido não autoriza truncar
condições ou negações.

## Execução e revisão

- Base v0.1.1: 16 casos com a skill e oito controles sem a skill; X05 reprovado
  nas duas condições, conforme a revisão independente.
- Primeira correção: 20 casos, incluindo os quatro reservados; 19 aprovados e
  X05 reprovado pela exigência de aumento de limite sem fundamento.
- A primeira correção também passou em uma execução e revisão das 88 regressões.
- Correção final: os 20 casos foram executados novamente, junto das 88 regressões.
  Os três revisores não identificaram falhas materiais ou críticas nos 108 registros.

Os geradores receberam somente IDs e pedidos, sem critérios ou respostas
anteriores. Na rodada final, houve quatro contextos novos: contratos (20),
original (28), ASD/PTC (24) e difíceis/estabilidade (36). Os revisores usaram
outros três contextos, cobrindo 20, 52 e 36 casos. Os pedidos da bateria de
estabilidade foram mantidos; não foram derivados novamente das respostas desta
rodada. A reexecução verifica regressão nesses pedidos estáticos.

A identificação exata do modelo, sua revisão e os parâmetros não são expostos
pela ferramenta de subagentes e ficam nulos no manifesto. Não foram medidos
custo, tokens faturados ou latência. Esta avaliação não equivale a validação
com leitores humanos, taxa estatística de acerto ou certificação normativa.

## Artefatos e repetição

- [Casos e critérios](../tests/casos-contratos.json).
- [Respostas anteriores](../tests/avaliacoes/v0.1.2/respostas-contratos-antes.json),
  [controle sem skill](../tests/avaliacoes/v0.1.2/controle-sem-skill.json) e
  [revisão anterior](../tests/avaliacoes/v0.1.2/revisao-contratos-antes.json).
- [Respostas intermediárias](../tests/avaliacoes/v0.1.2/respostas-contratos-intermediarias.json)
  e [revisão intermediária](../tests/avaliacoes/v0.1.2/revisao-contratos-intermediaria.json).
- [Respostas finais](../tests/avaliacoes/v0.1.2/respostas-contratos.json) e
  [revisão final](../tests/avaliacoes/v0.1.2/revisao-contratos.json).
- [Manifesto com hashes](../tests/avaliacoes/v0.1.2/manifesto.json) e
  [ficha semântica](avaliacao-semantica.md).

Os hashes identificam as instruções finais efetivamente fornecidas aos geradores,
as referências e os artefatos da rodada. A base anterior é a tag v0.1.1. As cópias
textuais das duas instruções alteradas na candidata intermediária também estão
no manifesto; as demais referências vieram da mesma base. Resultados históricos
não foram sobrescritos.

```sh
python3 -B tests/checar.py
python3 -B tests/verificar.py --casos tests/casos-contratos.json tests/avaliacoes/v0.1.2/respostas-contratos.json
```

O verificador confere os contratos possíveis e os sinais de falha autorizados.
Nos casos de suspensão, `contrato_solicitado` preserva a exigência incompatível
para auditoria, sem aplicar seu limite à comunicação de impedimento. O script
não decide se essa suspensão era necessária: isso depende da revisão semântica.
Não interprete a passagem mecânica desses registros como cumprimento do formato
original. A contagem de caracteres usa pontos de código Unicode de strings
Python, não bytes ou largura visual.
