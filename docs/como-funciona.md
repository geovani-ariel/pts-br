# Como a skill funciona

## Clareza com o mesmo conteúdo

A skill compara o original e a revisão fato a fato. Uma frase menor só é útil
se continuar dizendo quem age, em que condições, com qual resultado e com o
mesmo grau de certeza.

“A requisição pode ter falhado” é uma hipótese. “A requisição falhou” é uma
afirmação. Trocar uma pela outra altera o conteúdo, mesmo que o resultado pareça
mais direto. Da mesma forma, “disponível”, “fornecido” e “instalado” podem
designar estados diferentes.

## Por que adaptar ao português

As referências resolvem problemas diferentes. A linguagem simples orienta o
texto para as necessidades do leitor. O guia Microsoft pt-BR ajuda a localizar
conteúdo técnico. O PTC oferece verificações de ambiguidades do português.
A inspiração em ASD-STE100 não exige importar proibições gramaticais do inglês.

Por isso, artigos e preposições permanecem, gerúndios podem expressar duração e
a voz passiva continua válida quando o responsável é desconhecido. A skill
não inventa um ator para satisfazer uma preferência pela voz ativa.

## Modos de revisão

| Modo | Objetivo | Exemplo de uso |
|---|---|---|
| Rigoroso | Tornar ações, condições e resultados explícitos. | Procedimentos e descrições de ferramentas. |
| Natural | Manter precisão com o tom e a autoria do texto. | Documentação, explicações e comunicados. |

As metas de 20 palavras por instrução e 25 por descrição são convenções locais.
Se for necessário ultrapassá-las para conservar uma condição, preserve a
condição. A contagem não é uma medida suficiente de clareza.

## Tradução e glossário

A tradução depende do conceito e do público. Por exemplo:

- `request` pode ser “requisição” em HTTP e “solicitação” em um pedido humano.
- `job` pode significar uma vaga de emprego ou uma abstração de processamento.
- `support` pode indicar atendimento, compatibilidade ou capacidade de suportar carga.

O [glossário](../references/glossario.md) organiza três decisões: traduzir,
manter no original e decidir pelo contexto. Um glossário fornecido pelo usuário
prevalece sobre o do projeto; ambos prevalecem sobre a base local.

Essas preferências se aplicam à prosa. Não autorizam alterar `npm run build`,
o identificador `Request`, uma URL ou o texto real de um botão. Crases também
podem destacar termos comuns: o contexto decide se algo é código protegido.

## Condições que atravessam frases

Dividir um período pode retirar uma restrição da segunda ação. Quando duas
ações só são permitidas em homologação, essa condição precisa governar as duas.
Um cabeçalho comum ou a repetição da condição preserva o alcance original.

Confira também quantificadores, exceções e conectores. “Nem todos” não significa
“nenhum”. “Desde que” pode ser temporal ou condicional. Uma revisão não pode
escolher silenciosamente uma interpretação que a fonte não esclarece.

## Pendências e formatos de saída

Quando faltar informação necessária, a skill preserva o trecho afetado e
registra a pendência. Ela não inventa um titular para “seu acesso”, uma data
de referência para “amanhã” ou uma convenção para uma data ambígua.

Se houver contrato estruturado, a pendência deve caber nos campos autorizados.
A revisão não pode acrescentar propriedades ou texto depois de um JSON que
deveria ser a saída completa.

## Uso das referências

As instruções operacionais ficam em [SKILL.md](../SKILL.md). O glossário é
consultado quando houver tradução ou termos estrangeiros. As regras detalhadas
ajudam em ambiguidades e localização. A fundamentação das fontes é consultada
quando for necessário explicar decisões ou resolver conflitos.

Essa organização mantém as explicações disponíveis sem exigir sua releitura a
cada texto. Veja a [base documental](../references/referencias.md) para as
seções consultadas e os limites da adaptação.
