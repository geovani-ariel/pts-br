# Avaliação v0.1.0

Rodada de 26 de outubro de 2026. As três baterias existentes foram executadas
novamente, junto de 12 casos de estabilidade, contra a mesma cópia final de
`SKILL.md` e das referências. As respostas históricas permanecem preservadas.

## Método e rastreabilidade

Os geradores receberam somente `id` e `prompt`, sem critérios, respostas
anteriores ou conclusões dos revisores. Cada bateria usou um agente com contexto
novo; os pedidos foram tratados independentemente dentro desse contexto. Isso
não equivale a abrir um contexto separado para cada caso.

As reaplicações E10–E12 foram geradas por outro agente a partir das respostas
reais de E01, E02 e E06. Dois revisores com contextos novos avaliaram, respectivamente,
52 e 36 casos usando a [ficha semântica](avaliacao-semantica.md), sem consultar
as revisões exploratórias. O coordenador conferiu os registros e os artefatos.

O [manifesto](../tests/avaliacoes/v0.1.0/manifesto.json) registra data, ambiente,
commit de partida e hashes SHA-256 das instruções, referências, casos, respostas
e revisões. O commit de partida é anterior às correções; os hashes identificam
a cópia efetivamente avaliada, sem depender de um hash de commit circular.

A execução usou subagentes do Codex com configuração herdada. A ferramenta não
expõe o identificador exato do modelo, sua revisão ou parâmetros de amostragem;
esses campos ficam nulos no manifesto. Os arquivos permitem auditar os resultados,
mas não prometem reprodução determinística. Custo, tokens faturados e latência
não foram medidos.

## Cobertura

| Bateria | Casos | Respostas da nova execução |
|---|---:|---|
| Original | 28 | [Respostas](../tests/avaliacoes/v0.1.0/respostas-original.json) |
| ASD e PTC | 24 | [Respostas](../tests/avaliacoes/v0.1.0/respostas-asd.json) |
| Tradução e ambiguidade | 24 | [Respostas](../tests/avaliacoes/v0.1.0/respostas-dificeis.json) |
| Estabilidade | 12 | [Casos](../tests/casos-estabilidade.json) e [respostas](../tests/avaliacoes/v0.1.0/respostas-estabilidade.json) |

A bateria de estabilidade cobre preservação de texto claro, substituições de
nomes e valores, equivalência entre prosa/lista/JSON e reaplicação da revisão.
Também verifica ambiguidade dentro de um campo JSON autorizado e um rótulo de
interface com limite de 45 caracteres. Não há exigência universal de igualdade
literal entre redações semanticamente equivalentes.

## Resultado final

Os 88 resultados passaram nas checagens mecânicas. As duas revisões semânticas
registraram 88 aprovações, sem falha crítica ou material identificada nesta
amostra final. Veja os registros [original/ASD](../tests/avaliacoes/v0.1.0/revisao-original-asd.json)
e [difíceis/estabilidade](../tests/avaliacoes/v0.1.0/revisao-dificeis-estabilidade.json).
Os três pares de reaplicação também mantiveram igualdade literal. Isso descreve
a execução registrada, sem garantir o comportamento em novos textos.

## Correções demonstradas

Duas execuções exploratórias completas precederam a execução final. O
[registro dos ajustes](../tests/avaliacoes/v0.1.0/ajustes.json) preserva as respostas
problemáticas e as respectivas avaliações, sem substituir os resultados antigos.

- **C05:** a resposta transferiu atributos da experiência para a solução.
  A instrução passou a exigir que cada atributo permaneça ligado à entidade
  qualificada. Na resposta final, os qualificadores ornamentais foram removidos,
  como permite a regra específica, sem inventar propriedades técnicas.
- **L05:** uma previsão incerta, explicitamente definida no pedido, virou mera
  possibilidade. A comparação final agora exige preservar a força da certeza
  nos dois sentidos. A nova resposta usa “Espera-se que o serviço volte em breve”
  e conserva a ausência de autorização para reiniciar.

A correção de C05 também foi explorada em cinco pedidos de atributos com e sem
a orientação; são amostras diagnósticas, não cinco repetições estatísticas do
mesmo pedido nem parte dos 88 casos da execução final.

## Checagens automáticas

Execute na raiz do repositório, com Python 3:

```sh
python3 -B tests/checar.py
```

O comando executa os testes unitários e o autoteste; confere as três baterias
históricas e as quatro baterias da avaliação; verifica cobertura dos registros
de revisão, hashes e existência dos destinos dos links locais em Markdown.
Não consulta links externos nem valida âncoras dentro de páginas.

O verificador ganhou `max_caracteres`: a contagem usa `len()` de strings Python
(pontos de código Unicode), não largura visual nem bytes. O limite é inclusivo.
O teste negativo excedeu o limite antes do ajuste e passou a ser rejeitado depois.

O gate rejeita manifesto vazio, ausência de hashes obrigatórios, mudanças nos
arquivos avaliados e revisão com falha material ou crítica. Alterar uma resposta
exige nova revisão, em vez de apenas recalcular seu hash para obter aprovação.
O CI verifica a consistência dos registros salvos; não comprova que um revisor
esteja correto nem executa modelos automaticamente.

## Limites

Estas são amostras sintéticas revisadas por agentes. Não representam taxa de
acerto, certificação normativa, teste com leitores humanos ou validação de
procedimentos reais. Geradores e revisores podem compartilhar vieses do modelo.
A checagem literal e estrutural não substitui a avaliação de sentido.
