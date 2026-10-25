# Base de referências e critérios de aplicação

As três referências abaixo orientam partes diferentes da skill. Foram consultadas
em 25 de outubro de 2026. São fontes de orientação; a skill não oferece auditoria
de conformidade nem certificação.

## ABNT NBR ISO 24495-1:2024 — Linguagem simples

Aplicação das seções 4 e 5: considere o leitor e a tarefa; selecione informação
pertinente; organize-a para consulta; escreva de forma compreensível; confira se
o texto permite alcançar o objetivo. Use títulos e listas quando ajudarem.
Adapte explicações ao conhecimento do público. Aplique esses critérios juntos,
sem transformar a revisão em uma sequência rígida.

A conferência pelo agente é uma revisão editorial. Só relate teste com leitores
quando esse teste tiver ocorrido. Não atribua à norma os limites locais de
palavras desta skill ou as traduções do glossário.

Fontes: [escopo oficial da ISO 24495-1:2023](https://www.iso.org/standard/78907.html)
e [cópia pública da edição brasileira consultada](https://mwpt.com.br/wp-content/uploads/2025/11/Linguagem-Simples-ABNT.pdf),
seções 4 e 5 e anexos de revisão. A cópia foi usada para leitura, sem redistribuir
a norma no pacote.

## Microsoft — Portuguese (Brazil) Localization Style Guide

Das seções 2.1.3 e 2.1.4, use terminologia aprovada e tradução por contexto.
Da seção 4.1.2, adapte o tratamento de siglas ao público e mantenha formas
reconhecidas. Das seções 4.1.4, 5.5 e 5.6, aproveite a fluência dos artigos,
os nomes oficiais e a consistência da interface. Referências: páginas 8–9,
23–27 e 41 do PDF de 56 páginas consultado.

As escolhas corporativas e de voz da Microsoft não se tornam regras universais.
Em instruções sobre uma interface existente, mantenha seu rótulo real. Na
localização de uma interface autorizada, use a terminologia aprovada do produto.

Fontes: [catálogo oficial](https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides)
e [guia pt-BR consultado](https://download.microsoft.com/download/8/e/3/8e349e32-9eb9-4b63-9909-7586b94a24dd/por-bra-StyleGuide.pdf).

## Português Técnico Controlado — PTC

Fonte comunitária de Kayque Rotondo, sob MIT:
[repositório](https://github.com/kayquer/portugues-tecnico-controlado), versão
[95b74f559042ad5a7e411d6a21b566d23b048d82](https://github.com/kayquer/portugues-tecnico-controlado/tree/95b74f559042ad5a7e411d6a21b566d23b048d82).
Foram lidos o README, as seções pertinentes de `SKILL.md`, `references/lexico.md`
e a licença.

Aproveite as verificações de responsável, referência pronominal, modalidade,
conectores, restrição por vírgulas, posição de adjetivos e consistência lexical.
Use o formato de glossário com definição, artigo e alternativas a evitar.
Na localização de datas e números, confirme a convenção de origem e preserve os
elementos executáveis. Mantenha variantes regionais legítimas fora da categoria
de erro: a escolha desta skill é português brasileiro.

Esta adaptação não incorpora todas as proibições do PTC. Um gerúndio durativo,
uma voz passiva sem ator conhecido ou uma expressão técnica válida podem ficar.
Não reduza “pode” a permissão se a fonte expressar possibilidade. Não transforme
uma estimativa em prazo garantido para satisfazer uma regra de forma.

Aviso de licença preservado em [LICENSE-PTC](../LICENSE-PTC).

## Conflitos e precedência

1. Preserve o sentido, os contratos técnicos e os elementos literais no escopo do pedido.
2. Aplique preferências explícitas do usuário e o glossário do projeto.
3. Use a referência conforme a tarefa: linguagem simples para público e uso;
   Microsoft para localização; PTC para desambiguação do português.
4. Nas escolhas que restarem, aplique os modos e o glossário local da skill.

Exemplos de conciliação: a Microsoft admite sinônimos na prosa natural; mantenha
estáveis os nomes técnicos para não sugerir entidades diferentes. O PTC adota
limites próprios de frase; aqui, 20 e 25 palavras continuam metas locais. Se uma
regra de estilo mudar modalidade, escopo, tempo ou valor, preserve a precisão.
