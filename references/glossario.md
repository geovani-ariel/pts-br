# Glossário de tradução técnica

Base inicial para textos de software em português brasileiro. As decisões abaixo
são convenções desta skill, editáveis pelo usuário. Outros domínios podem exigir
glossários próprios. Não apresente estas escolhas como exigências da ABNT,
Microsoft, ASD ou da gramática portuguesa.

## Como decidir

1. Separe prosa editável de elementos literais. Preserve comandos, identificadores,
   nomes oficiais, mensagens citadas e rótulos reais de interface. Um glossário
   de prosa não autoriza mudar esses elementos.
2. Aplique o glossário explicitamente fornecido pelo usuário. Na ausência dele,
   use o glossário adotado pelo projeto. Para entradas não cobertas, use esta base.
3. Identifique o conceito, não apenas a grafia. A mesma palavra pode exigir
   decisões diferentes em HTTP, interfaces, negócios e operações.
4. Use a mesma equivalência para o mesmo conceito no texto. Flexione verbos e
   substantivos conforme a frase. Não faça substituições mecânicas de strings.
5. Para termos não listados, traduza se o equivalente for claro, conhecido pelo
   público e preservar o conceito. Caso contrário, mantenha o termo original.
   Acrescente uma explicação curta na primeira ocorrência se isso ajudar.
   Se faltar contexto e a escolha puder mudar o sentido, registre `Pendente:`.

Não transforme revisão em tradução integral de outro idioma sem que o pedido
inclua isso. Estas decisões também se aplicam a estrangeirismos em prosa já
escrita em português. Marcas, padrões e nomes de recursos podem ter nomenclatura
oficial própria.

## Localização e glossário do projeto

Do guia Microsoft pt-BR, aplique a tradução por contexto, a terminologia aprovada
do produto e o tratamento de siglas. Evite traduzir palavra por palavra. Use nomes
oficiais localizados quando estiverem confirmados; preserve marcas sem tradução
oficial e rótulos que o leitor precise reconhecer exatamente na interface.

Mantenha siglas técnicas reconhecidas pelo público. Explique uma sigla na primeira
ocorrência quando isso ajudar, sem expandir automaticamente formas familiares
como USB ou formatos de arquivo. Use plurais como `APIs`, sem apóstrofo, e um
artigo consistente para cada termo. Não altere siglas dentro de identificadores.

Inspirado no glossário do PTC, registre decisões de domínio com contexto, forma
preferida, artigo, definição e alternativas a evitar. Por exemplo:

| Termo EN | Forma PT-BR | Decisão | Artigo | Contexto e definição | Não usar | Origem |
|---|---|---|---|---|---|---|
| request | requisição | traduzir | a | Mensagem enviada a uma API HTTP. | solicitação, quando o projeto distinguir pedidos humanos | Convenção do projeto |
| endpoint | endpoint | manter | o | Ponto de acesso a uma operação da API. | ponto final | Convenção do projeto |

Essas entradas ilustram decisões locais, não traduções impostas pelas referências.
Mantenha termos técnicos estáveis nos dois modos. O modo natural permite variedade
na prosa comum, sem trocar os nomes de entidades, ações ou estados do domínio.

## Traduzir na prosa

Use estas formas quando o termo tiver o sentido indicado. Não acrescente a
forma inglesa entre parênteses em toda ocorrência.

| Termo de origem | Forma preferida | Contexto |
|---|---|---|
| file | arquivo | Documento ou arquivo de sistema. |
| folder | pasta | Organização de arquivos. |
| directory | diretório | Estrutura de sistema de arquivos. |
| settings | configurações | Opções de produto ou sistema. |
| default | padrão | Valor ou comportamento predefinido. |
| database | banco de dados | Armazenamento estruturado de dados. |
| query | consulta | Consulta a dados; preserve o SQL literal. |
| response | resposta | Resposta de serviço ou ao usuário. |
| error | erro | Prosa sobre uma falha; preserve a mensagem literal. |
| warning | aviso | Categoria genérica de mensagem de software; preserve classificações específicas de segurança. |
| user | usuário | Pessoa que usa o sistema. |
| account | conta | Conta de acesso ou de produto. |
| password | senha | Credencial descrita em prosa. |
| permission | permissão | Direito de executar uma ação. |
| authentication | autenticação | Verificação de identidade. |
| authorization | autorização | Permissão de acesso ou ação; não confundir com autenticação. |
| encryption | criptografia | Proteção criptográfica de dados. |
| repository | repositório | Repositório de código. |
| screenshot | captura de tela | Imagem de uma tela. |
| retry | nova tentativa; tentar novamente | Substantivo ou verbo em prosa. |
| update | atualização; atualizar | Substantivo ou verbo em prosa. |
| status code | código de status | Código, por exemplo, de resposta HTTP. |

## Manter no original na prosa técnica

Mantenha estes termos com o mesmo sentido e a mesma grafia no documento. Não
os traduza para expressões literais pouco reconhecíveis pelo público técnico.

| Termo | Evitar nesta base |
|---|---|
| commit | comprometimento, confirmação como substituição do objeto Git |
| branch | ramo, ramificação como nome do objeto Git |
| merge | fusão como nome da operação Git |
| pull request; PR | pedido de puxar, solicitação de alteração como substituição do objeto da plataforma |
| deploy | desdobramento; publicação como sinônimo automático |
| build | construção; compilação como equivalência de todo processo de build |
| backend; frontend | retaguarda; frente final |
| endpoint | ponto final |
| webhook | gancho da web |
| framework | estrutura como substituição automática do componente de software |
| worker | trabalhador |
| job | emprego; processo agendado quando o agendamento não estiver estabelecido |
| cache | esconderijo |
| token | ficha |
| cookie | biscoito |
| log | diário como substituição automática do registro técnico |
| prompt | estímulo como substituição automática da instrução a um modelo |
| pipeline | encanamento |
| plugin; skill | plugue; habilidade como substituição do recurso de um agente |
| API; SDK; CLI; SQL; JSON; HTTP; URL | Traduções ou expansões inventadas das siglas. |

“Manter no original” vale para o sentido técnico da entrada. Não mantenha
“job” em inglês se o assunto for uma vaga de emprego. Uma tradução explicitamente
solicitada pelo usuário pode substituir esta preferência na prosa.

## Decidir pelo contexto

| Termo | Decisão |
|---|---|
| request | “Requisição” em HTTP/API; “solicitação” para pedido de uma pessoa. Preserve nomes literais como `Request`. |
| issue | Mantenha `issue` para o objeto do GitHub. Use a nomenclatura adotada na plataforma para outros rastreadores. Fora desse contexto, traduza como problema, questão ou pendência conforme o sentido. |
| bug | “Erro” ou “defeito” em texto para público geral. Mantenha `bug` se designar uma categoria do rastreador ou se o glossário técnico do projeto o adotar. |
| task | “Tarefa” em prosa genérica. Preserve o termo ou identificador quando designar uma abstração específica, distinta de `job`. |
| login; logout | Para ações do usuário, prefira “entrar” e “sair”. Preserve comandos, eventos, rotas e rótulos reais, como `login` ou “Sign in”. |
| timeout | “Tempo limite” para o intervalo. “O tempo limite foi excedido” para o evento. Preserve nomes de parâmetros, erros literais e categorias do projeto. |
| deadline | “Prazo” ou “prazo final”. Não trate como sinônimo de timeout: preserve a distinção entre um prazo e um intervalo de espera. |
| backup | “Cópia de segurança” em texto geral. Mantenha `backup` em prosa para operações de software se esse for o termo do projeto. |
| deployment | Use `deploy` para a operação técnica nesta base. “Implantação” pode ser usada quando adotada no projeto. Preserve nomes oficiais e rótulos da plataforma. |
| release | “Versão” quando indicar uma versão; “lançamento” quando indicar o evento. Preserve `release` para o objeto da plataforma. Não confunda com deploy. |
| state; status | “Estado” para a condição de uma entidade; “status” quando for a nomenclatura do produto ou contrato. Não os unifique se houver dois conceitos distintos. |
| stream | “Fluxo” quando isso explicar o conceito. Preserve `stream` para um tipo, API ou abstração nomeada no projeto. |
| support | “Suporte técnico” para atendimento; “ser compatível com” para compatibilidade; “suportar” para carga ou capacidade. Preserve nomes oficiais. |
| available; provided | “Disponível” e “fornecido”, respectivamente, conforme o contexto. Não são estados equivalentes: algo disponível pode ainda não ter sido fornecido. |

## Exemplo

**Entrada**

> Check the settings before the deploy. Open the pull request and review the branch before the merge. The database backup may be incomplete.

**Pedido:** traduzir para português brasileiro, para um público geral, usando esta base.

**Resultado**

> Verifique as configurações antes do deploy.
> Abra o pull request.
> Revise a branch antes do merge.
> A cópia de segurança do banco de dados pode estar incompleta.

Preserve `npm run build`, o rótulo “Create deployment”, o caminho `/health` e o
erro literal “Request timeout” em instruções sobre esses elementos. A prosa
ao redor pode usar “requisição HTTP” e “tempo limite”.

## Referências e limites

A [base de referências](referencias.md) identifica os documentos lidos, as seções
aproveitadas e como os conflitos foram resolvidos. As orientações de localização
e a estrutura do glossário usam Microsoft pt-BR e PTC. As equivalências das
tabelas continuam sendo uma base editorial própria, sem alegação de conformidade
integral com esses documentos ou com a ABNT.
