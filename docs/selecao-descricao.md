# Seleção apenas pela descrição — v0.1.4

Avaliação de 27 de outubro de 2026, sem a regra obrigatória de `AGENTS.md` nos
processos de teste. **A seleção não foi confiável nesta amostra.** A descrição
original foi restaurada após duas candidatas não resolverem as omissões.

Não há correção comprovada do seletor nesta versão. Há evidências reproduzíveis,
correções editoriais separadas e uma limitação explícita de uso. A regra global
do usuário foi preservada.

## Como a regra foi retirada do ensaio

Cada pedido foi executado em contexto novo do Codex CLI 0.154.0 com:

```sh
codex exec --ignore-user-config --ephemeral --json --sandbox read-only \
  --skip-git-repo-check -c project_doc_max_bytes=0 \
  -C /caminho/da/pasta-do-caso -o /caminho/da/saida.txt - < pedido.txt
```

`--ignore-user-config` foi aplicado somente ao processo. O limite de zero bytes
foi usado para não carregar os arquivos de instruções. Os diretórios dos casos
não continham `AGENTS.md`. O catálogo foi consultado: havia uma PTS-BR habilitada,
de escopo de usuário, entre 46 skills. Os pedidos não mencionavam seu nome nem
recebiam o corpo de `SKILL.md`.

A [referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference)
descreve `project_doc_max_bytes` como o limite de leitura de `AGENTS.md`. Além do
parâmetro, um controle verificou o comportamento: um projeto local recebeu um
nome-canário desconhecido do pedido. Sem abrir arquivos, o CLI retornou o nome
quando o limite era 32.768 bytes e `NÃO INFORMADO` quando era zero. Esse controle
não definiu nenhuma regra de PTS-BR.

Os hashes de `config.toml` e do `AGENTS.md` globais permaneceram iguais antes e
depois. A skill instalada foi temporariamente usada para os ensaios das descrições
e depois restaurada byte a byte. Nenhum modelo foi escolhido por override:
foi usado o padrão do CLI sem a configuração do usuário. O identificador efetivo
não consta no JSONL utilizado; não foi inferido pelo cache do app.

## Resultados da seleção

Os seis positivos são pedidos compatíveis com o escopo da PTS-BR. Os seis
negativos cobrem literatura, publicidade, código puro, saída em inglês, conta
aritmética e bilhete não técnico. O revisor independente confirmou os 12 rótulos.

| Descrição ou controle | Positivos com leitura | Negativos sem leitura | Omissões |
|---|---:|---:|---|
| Original, ativa | 2 de 6 | 6 de 6 | I01, I03, I09, I10 |
| Candidata A, rejeitada | 3 de 6 | 6 de 6 | I01, I03, I10 |
| Candidata B, rejeitada | 2 de 6 | 6 de 6 | I01, I03, I09, I10 |
| Original com contexto ampliado, subconjunto | 0 de 2 | 2 de 2 | I01, I03 |

Na descrição original, houve leitura no procedimento operacional I02 e na
documentação de API I04. Não houve leitura na mensagem de erro curta I01, na
tradução técnica I03, na descrição de ferramenta I09 ou no relato técnico curto
I10. Não se observou leitura fora do escopo nos controles negativos.

A candidata A destacou tradução e trechos curtos; a B antecipou “melhorar a
clareza” e “uma única frase”. Nenhuma resolveu I01/I03/I10. A diferença de um caso
reservado em A não demonstra melhora estável. Não houve nova tentativa de
redação depois dessas duas candidatas; a descrição original foi mantida.

A descrição original foi medida em oito casos-base e quatro reservados após sua
restauração. Cada candidata foi executada nos 12 casos. São observações isoladas,
sem múltiplas repetições por pedido, identificador de modelo fixado ou significância
estatística. Elas não medem uma taxa geral de acerto de todos os modelos do Codex.

## Abreviação das descrições e controle de contexto

O CLI avisou que algumas descrições foram abreviadas para caber no orçamento de
contexto. O aviso informa que todas as skills continuavam visíveis; não capturamos
o trecho exato da descrição recebido pelo modelo em cada turno.

Para investigar esse fator, quatro casos foram repetidos com a descrição original
e `-c skills.max_context_tokens=10000`, somente nesses processos, mantendo a regra
de `AGENTS.md` desativada. I01 e I03 continuaram sem leitura; I06 e I08 respeitaram
a ausência de seleção. Portanto, ampliar o contexto não resolveu os dois positivos
testados. O ensaio não isola todas as causas possíveis das omissões.

## Evidência usada para contar uma seleção

A medição usa eventos `command_execution` concluídos com código zero, com comando
de leitura do arquivo e trecho de saída contendo a identificação da PTS-BR.
Uma menção ao caminho, um `echo`, um evento ainda em execução ou um comando que
falhou não conta como leitura. O parser cobre as formas de leitura observadas
nesta rodada, não qualquer ferramenta possível de um runtime futuro.

Leitura não prova aplicação correta. Ausência de leitura também não prova, sozinha,
que a resposta esteja errada. Por isso, as respostas da descrição original foram
avaliadas separadamente contra o pedido e a fonte.

## Duas falhas de sentido e suas correções editoriais

Dez respostas originais foram aprovadas; duas tiveram falhas materiais:

- **I09:** “A ferramenta pode remover” virou “Remova”, convertendo permissão em
  ordem. As condições `dry_run=false` e aprovação foram preservadas, mas a
  modalidade mudou.
- **I10:** a resposta acrescentou “pois”, criando causalidade, e “nesse ambiente”,
  restringindo a ausência geral de deploy à produção. A fonte não dizia isso.

As [correções editoriais](../tests/selecao-descricao/correcoes-editoriais.json)
foram aprovadas pelo revisor. Elas não substituem os resultados automáticos e não
comprovam correção do roteamento. A skill já contém instruções para preservar
permissão e grau de certeza; não se acrescentou outra regra ao corpo que deixou
de ser lido nesses casos.

## Ajuste do pedido de API

Uma primeira execução de I04 foi excluída da matriz: “Não execute comandos” foi
entendido como proibição até de ler o arquivo. O pedido foi corrigido para
permitir leitura e proibir apenas a execução dos exemplos do documento. A nova
execução leu o arquivo e a skill. O pedido e a resposta invalidados permanecem
no registro, sem serem contados como uma omissão causada pela descrição.

## Consequência para o uso

A [documentação oficial](https://learn.chatgpt.com/docs/build-skills) descreve a
escolha implícita por correspondência com a descrição e informa que ela é permitida
por padrão. Estar habilitada não comprova que a skill foi lida em um turno.

Para o uso obrigatório configurado pelo usuário, mantenha a política de
`AGENTS.md` já existente. Esta rodada não demonstra que a descrição, sozinha,
substitua essa política. Também não demonstra o comportamento do app com o modelo
configurado no ambiente do usuário: a execução usou o padrão do CLI com a
configuração do usuário ignorada.

## Conferência e artefatos

Execute na raiz:

```sh
python3 -B tests/checar.py
```

O CI verifica integridade, estrutura, isolamento registrado e classificação das
evidências. Ele imprime as omissões e as falhas semânticas conhecidas, sem tratá-las
como resolvidas. **Um CI verde não significa que todos os pedidos acionaram a skill.**
Ele não executa novamente os modelos.

[Casos](../tests/selecao-descricao/casos.json),
[matriz original](../tests/selecao-descricao/original.json),
[candidata A](../tests/selecao-descricao/candidata-a.json),
[candidata B](../tests/selecao-descricao/candidata-b.json),
[controle de contexto](../tests/selecao-descricao/contexto-ampliado.json),
[revisão semântica](../tests/selecao-descricao/revisao-semantica.json),
[revisão das correções](../tests/selecao-descricao/revisao-correcoes.json) e
[registro](../tests/selecao-descricao/registro.json) estão preservados. As candidatas
arquivadas em `.txt` são evidência do experimento, não skills ativas adicionais.
