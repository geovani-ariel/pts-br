# Avaliação semântica

Avalie a resposta contra a fonte e o pedido, sem exigir uma redação única.
As checagens mecânicas são uma etapa separada.

| Dimensão | O que conferir |
|---|---|
| Fatos e evidência | Preservar fatos, hipóteses, limitações da fonte e grau de certeza. |
| Responsáveis e referentes | Preservar atores e objetos; não resolver referentes desconhecidos por inferência. |
| Negação e modalidade | Distinguir possibilidade, permissão, obrigação, ausência de obrigação e proibição. |
| Condições e exceções | Manter o alcance de cada condição, exceção e conector. |
| Tempo e sequência | Preservar ordem, duração e a diferença entre evento, relato e confirmação. |
| Quantidades | Preservar números, unidades, limites, proporções e cardinalidade. |
| Terminologia e literais | Respeitar o conceito, a precedência do glossário e os elementos protegidos. |
| Entrega | Cumprir idioma, formato, campos autorizados e limites sem suprimir conteúdo. |

## Registro e decisão

Registre um resultado por caso, inclusive os aprovados. Em cada falha, indique
a dimensão, o trecho da fonte, o trecho da resposta e a mudança de sentido ou
a violação observada. Dimensões não presentes no caso não exigem conteúdo novo.

- **Crítica:** inverter uma proibição, autorizar ação restrita ou inventar um fato
  que mude uma decisão operacional.
- **Material:** perder ou alterar informação, escolher uma ambiguidade sem base,
  usar conceito incorreto ou descumprir idioma/formato exigido.
- **Editorial:** redação pouco natural que preserva o sentido e o contrato.

Uma falha crítica ou material reprova o caso. Preferência estilística isolada
não reprova. Registre divergências entre revisores e resolva-as pela fonte e
pelo pedido; não por votação ou por preferência de redação. Uma correção deve
ser avaliada novamente, preservando o registro anterior.

## Comparação entre variações

Nos testes de estabilidade, compare também as respostas relacionadas:

- Reaplicar a revisão deve preservar fatos, condições e termos; igualdade literal
  é desejável para textos já claros, mas não é requisito universal.
- Substituir nomes e números deve alterar somente os fatos correspondentes.
- Mudar prosa para lista ou JSON deve manter o alcance das condições e a sequência.

A revisão por outro agente reduz o compartilhamento das decisões do gerador,
mas não equivale a validação humana independente ou medição estatística.

## Tradução e contrato incompatíveis

Classifique o desfecho separadamente da aprovação da conduta:

- `traducao`: tradução fiel no idioma e contrato pedidos, inclusive quando um
  equivalente conserva a ambiguidade sem precisar de nota.
- `bloqueio_autorizado`: sinal de impedimento previsto no contrato, sem fabricar
  uma tradução nem inventar campos ou o significado de um marcador.
- `esclarecimento`: suspensão anterior ao artefato, com comunicação do impedimento
  ou solicitação do contexto/ajuste necessário. Não conta como tradução concluída.
- `bloqueio_sem_canal`: comunicação mínima de impossibilidade quando não há canal
  de falha autorizado e perguntas foram proibidas. Não conta como contrato cumprido.

Para contratos incompatíveis, avalie a honestidade e a fidelidade do tratamento,
sem exigir uma solução inexistente. Não atribua falha material apenas pela falta
de uma pergunta depois de um impedimento claro. Uma pergunta em campo reservado
à tradução, sem autorização para notas, é uma falha de entrega: pode ser exibida
pelo consumidor como tradução final. Também confira se o modelo bloqueou uma
tradução possível ou declarou uma restrição impossível sem fundamento.

Os casos com suspensão preservam o contrato solicitado em `contrato_solicitado`
para auditoria; o verificador não aplica aquele limite à mensagem de suspensão.
Essa separação não é aprovação do artefato nem prova automática de impossibilidade.
