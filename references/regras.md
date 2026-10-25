# Regras e exemplos de português técnico claro

Estas regras são convenções desta adaptação. Não constituem uma norma oficial.

## Público e uso

Use o objetivo e o conhecimento do leitor para escolher a ordem das informações
e explicar termos. Coloque requisitos e próximos passos onde o leitor os encontre.
Em uma revisão, reorganize o conteúdo sem apagar informações relevantes da fonte.
Na conferência final, verifique se o leitor consegue concluir a tarefa ou entender
a resposta. Revisão pelo agente não equivale a teste com leitores reais.
Aplicação dos princípios de linguagem simples: [base de referências](referencias.md).

## Frases e vocabulário

| Situação | Orientação |
|---|---|
| Ação escondida em um substantivo | Prefira “verifique o cadastro” a “realize a verificação do cadastro”. |
| Mesmo conceito com vários nomes | Escolha o termo do projeto. Não alterne “conta” e “perfil” se designarem a mesma entidade. |
| Conceitos diferentes | Preserve a distinção entre salvar, enviar, publicar e implantar. Não uniformize termos apenas por semelhança. |
| Sujeito conhecido | Prefira “O servidor rejeitou a solicitação” a “A solicitação foi rejeitada pelo servidor”. |
| Sujeito desconhecido | Preserve “O arquivo foi removido”. Não atribua a remoção ao servidor sem evidência. |
| Pronome com mais de um referente | Repita o nome quando o referente estiver estabelecido. Caso contrário, registre a pendência. |
| Jargão necessário | Siga o [glossário de tradução](glossario.md). Explique o termo se houver uma definição segura e isso ajudar o público. |
| Expressão burocrática | “Para” pode substituir “com a finalidade de”. “Em caso de” pode virar “se”. |
| Alegação de qualidade sem conteúdo concreto | Retire apenas o adjetivo ornamental. Preserve alegações técnicas. Não invente uma medição para justificá-las. |

Prefira pontos a frases longas ligadas por ponto e vírgula. Essa preferência se
aplica à prosa editável, sem alcançar código ou citações literais. Organize cada
parágrafo em torno de um assunto.

## Português continua sendo português

Preserve artigos e preposições que expressem relações: “o estado da conta” não
deve virar “estado conta”. Mantenha a flexão verbal e nominal adequada.

Não proíba palavras com mais de um sentido em todo o idioma. O compromisso é
usar termos consistentes e interpretações claras **dentro do documento**.
O glossário orienta equivalências técnicas; não é uma lista exaustiva de palavras
autorizadas no idioma.

Não aplique limites de substantivos consecutivos do inglês a expressões como
“válvula de entrada da bomba de combustível”. As preposições definem relações.
Reorganize a expressão apenas quando isso facilitar a compreensão sem alterar
qual peça ela identifica.

Mantenha aspectos verbais: “O serviço está processando os arquivos desde ontem”
indica continuidade. “O serviço processa os arquivos” perde essa informação.
“O serviço pode ter falhado” continua sendo hipótese sobre um evento passado.

## Condições e sequência

### Avisos e mensagens operacionais

Preserve nível, código e alcance de avisos como `AVISO [W-04]`. Não substitua
um aviso por uma observação informal para suavizar o tom. Coloque o aviso e suas
precondições antes das ações afetadas, sem inventar riscos, medidas ou valores.
Se a equivalência de um nível em outro idioma depender de uma norma ou produto,
use a convenção fornecida; não deduza uma classificação de segurança.

Quando passos puderem ocorrer em qualquer ordem, mantenha essa possibilidade.
Não transforme uma lista de verificações independentes em uma sequência obrigatória.
Em mensagens entregues isoladamente a agentes, cada trecho precisa identificar
os referentes conhecidos, sem depender de “ele”, “isso” ou “depois disso” fora
do trecho. Não invente referentes ausentes.

### Escopo compartilhado

Ao dividir uma instrução, escreva as condições compartilhadas em um cabeçalho
que governe explicitamente todos os passos. Mantenha as condições particulares
no passo correspondente. Não transforme uma condição cumulativa em alternativa.

**Original**

> Somente em homologação, após aprovação do responsável, exporte os registros e apague a cópia temporária apenas se a exportação terminar sem erros.

**Versão clara**

> Execute estes passos somente em homologação e após aprovação do responsável:
>
> 1. Exporte os registros.
> 2. Apague a cópia temporária apenas se a exportação terminar sem erros.

O cabeçalho restringe os dois passos. Colocar a condição apenas na primeira
frase deixaria a exclusão sem a mesma restrição explícita.

## Possibilidade, obrigação e evidência

**Original**

> O serviço pode tentar novamente a solicitação após 30 segundos, somente em homologação e se o administrador autorizar. Isso não garante o processamento. Se houver nova falha, não repita a solicitação.

**Versão clara**

> Somente em homologação, e se o administrador autorizar, o serviço pode repetir a solicitação após 30 segundos.
> A nova tentativa não garante o processamento.
> Se houver nova falha, não repita a solicitação.

“Pode” expressa possibilidade ou permissão conforme o contexto. Não o transforme
em certeza. Preserve “após 30 segundos”, sem trocar por “em até 30 segundos”.

**Original**

> A correção foi aplicada localmente, mas ainda não foi enviada ao repositório nem validada em produção. Os testes disponíveis passaram. O problema pode continuar em produção.

**Versão clara**

> A correção foi aplicada localmente.
> A correção ainda não foi enviada ao repositório nem validada em produção.
> Os testes disponíveis passaram.
> O problema pode continuar em produção.

O teste bem-sucedido não comprova publicação ou resolução em produção.

## Informação ausente

Verifique também ambiguidades próprias do português:

- Em “deve terminar”, distinga obrigação de estimativa. Se o contexto não decidir,
  mantenha a incerteza e registre a pendência.
- Em “desde que”, confira se a relação é temporal ou condicional. Não substitua
  por “se” sem que esse sentido esteja estabelecido.
- Em “os servidores que falharam”, a condição restringe quais servidores. Não
  acrescente vírgulas que passem a atribuir a falha a todos os servidores.
- Em “um simples teste”, não troque a posição do adjetivo automaticamente:
  “um teste simples” pode descrever a complexidade, em vez de minimizar o teste.
- Em “os contratos e anexos assinados”, confirme o alcance de “assinados” antes
  de repeti-lo nos dois substantivos. A repetição pode atribuir uma propriedade
  que a fonte não estabeleceu para ambos.
- “Uma vez que”, “como” e “inclusive” dependem do contexto. Não escolha uma
  relação causal, temporal ou de inclusão que a fonte não esclareça. Em `e/ou`,
  preserve a possibilidade de ambos quando isso estiver definido no texto.
- Explicite o responsável apenas quando a fonte ou o contexto o estabelecer.
  Não converta voz passiva ou sujeito omitido em uma atribuição inventada.

Essas verificações adaptam o PTC; não são proibições gerais de formas válidas do
idioma. Preserve gerúndios durativos e substantivos que nomeiem conceitos técnicos.

**Original**

> Marina avisou Carla que seu acesso seria removido amanhã.

**Entrega**

> Marina avisou Carla que seu acesso seria removido amanhã.
>
> Pendente: informar se o acesso é de Marina ou de Carla.

Não substitua “amanhã” por uma data sem conhecer a data de referência. Não
invente o titular do acesso, mesmo que uma leitura pareça mais provável.

## Elementos literais

### Tradução com sentido ainda não definido

Preservar a ambiguidade não exige deixar a entrega inteira no idioma de origem.
Se um equivalente no idioma pedido mantiver a mesma leitura aberta, use-o e
registre a pendência. Caso contrário, apresente as leituras condicionais, sem
escolher qual representa a intenção da fonte.

Por exemplo, sem contexto, “Requests may not be retried” pode indicar:

- Proibição: “As solicitações não podem ser repetidas.”
- Possibilidade: “As solicitações podem não ser repetidas.”

As duas linhas são hipóteses de tradução, não duas instruções simultâneas.
Registre qual sentido precisa ser esclarecido. Em JSON ou outro contrato,
coloque alternativas e pendências somente nos campos autorizados.

### Conteúdo que deve permanecer exato

Em “O erro `Permission denied; retry disabled` pode indicar ausência de
permissão”, preserve a mensagem entre crases. Não traduza a mensagem, retire o
ponto e vírgula ou converta a hipótese em diagnóstico confirmado.

Preserve opções como `--retry 0` e URLs que contenham `;`. Uma revisão de prosa
não autoriza alterar a operação de um comando.

## Revisão final

### Evento, relato e confirmação

Confira qual verbo cada marcador temporal modifica. “O timeout foi relatado antes
de a resposta chegar” situa o relato antes da chegada. “Foi relatado que o timeout
ocorreu antes da chegada” pode situar somente o timeout nesse intervalo e deixar
o momento do relato indefinido. Essa troca perde uma relação temporal.

Ao dividir ou traduzir a frase, preserve separadamente o momento do evento,
do relato e da confirmação. Uma informação em um log ou uma alegação não se
torna fato comprovado pela reescrita. Mantenha explícitas as verificações que
a fonte diz não terem ocorrido.

### Valores e comparação final

Em prosa localizada, ajuste números e datas somente quando a convenção de origem
estiver estabelecida. Preserve o valor, a unidade e o instante. Prefira data por
extenso ou ISO 8601 quando isso eliminar uma ambiguidade já resolvida. Se a origem
de `08/02/2026` for desconhecida, registre a pendência. Código e parâmetros como
`--limit 1.5` permanecem literais, mesmo quando a prosa usar `1,5`.

Confira o que cada ação exige e quais ações cada condição restringe. Compare
certeza, permissões, proibições, quantidades e ordem com o original. Confira os
elementos literais separadamente. A boa forma do texto, por si só, não prova
equivalência de sentido nem veracidade do conteúdo.

Preserve também limitações contextuais, como a impossibilidade de consultar uma
fonte. Uma nota de pendência não substitui esse fato. Confira os estados descritos:
suporte disponível não equivale a suporte fornecido, assim como envio não equivale
a recebimento. Uma paráfrase que troca esses estados muda o que o texto afirma.

Uma ressalva como “com base apenas no log fornecido” pode limitar a evidência.
Não a remova como metatexto sem conferir o efeito sobre a afirmação. Prefira
encurtar a ressalva preservando seu alcance. Formas legítimas como “assumir a
responsabilidade” e “suportar uma carga” não são erros por aparecerem em listas
de falsos amigos em outro sentido.
