# Glossário do projeto

Copie este arquivo para o projeto e informe seu caminho ao pedir uma revisão com
PTS-BR. Substitua as linhas de exemplo pelas decisões reais da equipe. Não é
necessário preencher termos que o projeto não usa.

- Projeto: preencher.
- Público: preencher.
- Escopo: documentação, interface, API ou outro conjunto de textos definido pela equipe.
- Responsável e data da revisão: preencher.

O glossário explícito do pedido prevalece sobre este arquivo; este arquivo
prevalece sobre a base da PTS-BR. Uma decisão de prosa não autoriza alterar
identificadores, comandos, mensagens citadas ou rótulos reais de interface.

| Origem | Conceito e contexto | Forma preferida em pt-BR | Decisão | Artigo | Formas a evitar | Elementos literais protegidos | Fonte da decisão |
|---|---|---|---|---|---|---|---|
| request | Mensagem enviada a uma API HTTP | requisição | Traduzir na prosa | a | solicitação, se designar pedido humano no projeto | `Request`, `request_id` | Exemplo editável |
| request | Pedido feito por uma pessoa | solicitação | Traduzir na prosa | a | requisição HTTP | Nenhum definido neste exemplo | Exemplo editável |
| endpoint | Ponto de acesso a uma operação da API | endpoint | Manter na prosa técnica | o | ponto final | `/health`, `GET /users` | Exemplo editável |

Use uma linha por conceito. Registre separadamente os sentidos de uma palavra.
Se a escolha ainda depender de contexto ausente, marque a decisão como pendente
em vez de declarar uma equivalência universal.

Exemplo de pedido:

```text
Use $pts-br e o glossário em docs/glossario-projeto.md para revisar o texto abaixo.
Preserve nomes de campos e rótulos reais de interface.
[texto]
```
