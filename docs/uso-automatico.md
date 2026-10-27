# Uso automático em documentos completos — v0.1.3

Rodada de 27 de outubro de 2026. Foram revisados três documentos fictícios
completos: um procedimento operacional, uma documentação de API e um relato de
incidente. Os pedidos de revisão não mencionam a PTS-BR. A aplicação foi orientada
pelo trecho de `AGENTS.md` que define as skills padrão do usuário.

## Resultado e alcance

| Documento | Palavras na entrada | Critérios de sentido | Resultado |
|---|---:|---:|---|
| Procedimento operacional | 536 | 9 | Leitura da skill registrada; critérios aprovados. |
| Documentação de API | 597 | 11 | Leitura da skill registrada; critérios aprovados. |
| Relato de incidente | 555 | 11 | Leitura da skill registrada; critérios aprovados. |

A contagem de palavras usa separação por espaços, incluindo exemplos. Não é uma
medida de qualidade ou economia de tokens. A revisão independente não identificou
perda material de sentido nos 31 critérios. As instruções linguísticas da v0.1.2
foram mantidas; esta versão acrescenta a bateria, suas evidências e as checagens.

Esse resultado valida a aplicação orientada por `AGENTS.md` nos três cenários.
Não testa a seleção apenas pela descrição, a interface do app ou todos os modelos.
A [documentação oficial de skills](https://learn.chatgpt.com/docs/build-skills)
distingue a invocação explícita da escolha implícita pela descrição. A política
local de aplicação automática é uma condição própria desta avaliação.

## Como a leitura foi observada

Os executores receberam somente a pasta da tarefa, o protocolo de leitura e o
pedido real. Cada contexto começou sem resultados ou critérios esperados. Os
acordos da pasta determinavam a aplicação das skills padrão, como no ambiente do
usuário; o pedido era apenas revisar `entrada.md`, sem resumir nem executar ações.

Um [leitor instrumentado](../tests/ler_registrando.py) abriu cada arquivo escolhido,
registrou caminho, tamanho e SHA-256 e entregou seu conteúdo ao executor. A PTS-BR
foi lida nos três casos, com o mesmo hash de `SKILL.md` publicado na v0.1.2.
O comando de revisão não recebeu o conteúdo da skill diretamente.

Esse registro comprova a leitura instrumentada, não a compreensão ou aplicação
correta. A preservação de sentido foi avaliada depois, por dois revisores em
contextos separados: um para procedimento/incidente e outro para API. Eles
verificaram cada critério contra entrada e saída, sem editar os resultados.

Os caminhos foram normalizados no registro público para remover diretórios
pessoais. O [trecho de acordos](../tests/uso-automatico/acordos.md) usa
`{{skills_root}}` no lugar do diretório do runtime. Os hashes das leituras dos
acordos correspondem à versão com esse caminho resolvido durante a execução.
As entradas dos documentos foram preservadas byte a byte.

## Edição intermediária do procedimento

O executor leu uma versão intermediária de `saida.md` com 3.831 bytes. Depois,
ajustou duas ações para que continuassem sob uma única condição:

```diff
-Se a conferência indicar uma exportação ainda em andamento com esse identificador, aguarde a conclusão dela.
-Não crie uma segunda exportação.
+Se a conferência indicar uma exportação ainda em andamento com esse identificador:
+
+- Aguarde a conclusão dela.
+- Não crie uma segunda exportação.
```

Essa edição gerou a versão final de 3.836 bytes, avaliada pelo revisor independente.
A versão intermediária foi [preservada](../tests/uso-automatico/intermediaria-procedimento.md):
sua reconstrução pela substituição exata confere com o hash já registrado pelo
leitor. O executor confirmou que fez a edição por Python, sem usar o leitor nessa
leitura final. Portanto, o protocolo não capturou todas as leituras da tarefa.

A revisão das ferramentas identificou que o gate aceitava a diferença sem
explicá-la. A correção distingue o recibo intermediário e um recibo de finalização,
obtido pelo coordenador após os executores concluírem. O gate agora associa cada
recibo à versão correspondente e confere os arquivos finais por tamanho e hash.
Um controle negativo rejeita o recibo anterior quando aplicado à versão final.
Isso não transforma o recibo do coordenador em evidência de que o executor releu
seu documento final.

## Tentativa de execução pelo CLI

Antes dos subagentes, foi tentado `codex exec --json --ephemeral` com sandbox de
somente leitura, sem sobrescrever o modelo da configuração. O CLI 0.154.0 recusou
`gpt-6.1-sol` para a conta ChatGPT utilizada, com `model_not_found`, antes de ler o
documento ou gerar uma revisão. A configuração global não foi alterada.

A execução final usou subagentes do runtime atual com o leitor instrumentado.
Não há um teste bem-sucedido do CLI nesta rodada. O identificador exato do modelo
desses subagentes não é exposto pela ferramenta e não foi inferido a partir da
configuração do CLI.

A [orientação oficial de avaliação de skills](https://developers.openai.com/blog/eval-skills)
recomenda observar execuções e avaliar os resultados separadamente. Nesta rodada,
a observação usou recibos do leitor, não eventos `command_execution` de uma
execução bem-sucedida do CLI.

## O que os documentos exercitam

- **Procedimento:** condições cumulativas valendo entre seções, uma exceção
  limitada à leitura de logs, ordem de execução, limites de consulta, distinção
  entre recebimento e conclusão, limpeza permitida somente após duas confirmações
  e retomada condicionada à janela e à ausência de outra execução.
- **API:** autenticação versus autorização, idempotência com prazo, estados
  assíncronos, disponibilidade versus entrega, paginação por snapshot, tipos JSON,
  limites, tabelas, cabeçalhos e novas tentativas sem autorização ilimitada.
- **Incidente:** requisições versus clientes, limites da amostra, relato versus
  ocorrência de timeout, hipóteses sem causalidade confirmada, homologação versus
  produção, testes locais versus deploy e ausência de alerta versus recuperação.

As tabelas, os comandos, os exemplos JSON e os elementos literais foram
conferidos mecanicamente. A avaliação editorial não executou nem validou o
comportamento do sistema fictício descrito nos documentos.

## Reproduzir a tarefa e conferir os registros

1. Crie uma pasta isolada por documento e copie a entrada como `entrada.md` e o
   [pedido](../tests/uso-automatico/pedido.txt) como `pedido.txt`.
2. Copie o trecho de acordos como `AGENTS.md`, substituindo `{{skills_root}}` pelo
   diretório de skills do runtime a testar.
3. Em um contexto novo do executor, peça a leitura dos acordos e o atendimento
   do pedido. Para instrumentar leituras, use `python3 /caminho/ler_registrando.py
   <arquivo>`, com diretório de trabalho na pasta do caso. O leitor entrega o
   conteúdo e grava `leituras.jsonl` ali. Não injete o texto da skill no pedido.
4. Salve o documento revisado como `saida.md`. Faça a avaliação de sentido em
   outro contexto, usando os [critérios](../tests/uso-automatico/casos.json).

Esse procedimento depende de um executor disponível e da configuração local.
Não promete reprodução determinística ou compatibilidade com o CLI que falhou.

Para conferir apenas os artefatos já registrados, sem chamar modelos:

```sh
python3 -B tests/checar.py
```

O gate verifica os três casos, a cobertura dos 31 critérios, leituras de entrada
com hash correto, leitura da PTS-BR, integridade dos artefatos e elementos literais.
Os controles negativos rejeitam ausência de leitura, hash de outra versão,
menção em outro arquivo, revisão com critério omitido ou duplicado e recibo
de uma versão intermediária apresentado como final. Essas
checagens não fazem uma nova revisão semântica.

Entradas, saídas, leituras e revisão estão em [tests/uso-automatico](../tests/uso-automatico).
O [registro](../tests/uso-automatico/registro.json) preserva a falha do CLI e os
limites do método. Os 108 casos focais anteriores continuam sendo conferidos
mecanicamente, sem nova geração de suas respostas nesta rodada.
