# Histórico de versões

## 0.1.4 — 2026-10-27

- Avaliação de seleção implícita sem a regra de `AGENTS.md`, com 12 casos,
  controle de isolamento e comparação de duas descrições candidatas.
- As candidatas não resolveram as omissões; descrição original restaurada.
- Duas respostas automáticas com perda de sentido preservadas como falhas, com
  correções editoriais revisadas em arquivos separados.
- Oito controles unitários para distinguir leitura efetiva de menções e comandos
  incompletos ou falhos, e rejeitar correções editoriais ausentes ou vazias.
- CI distingue integridade dos artefatos de sucesso de seleção.

Não há correção comprovada do seletor nesta versão. Regras linguísticas e
configuração global foram preservadas. Veja o [relatório](docs/selecao-descricao.md).

## 0.1.3 — 2026-10-27

- Três documentos completos para avaliar aplicação automática orientada por
  `AGENTS.md`: procedimento operacional, API e incidente.
- Leitura instrumentada com hashes e revisão independente de 31 critérios.
- Oito controles unitários para evidência de leitura, cobertura dos critérios
  e associação dos recibos às versões intermediária e final.
- Correção da associação entre o recibo intermediário do procedimento e sua
  edição final; as duas versões foram identificadas.
- Resultado e limitação do CLI registrados sem alterar a configuração global.

Os três documentos foram aprovados sem perda material identificada. As instruções
linguísticas da v0.1.2 permanecem iguais. Veja a [rodada de uso automático](docs/uso-automatico.md).

## 0.1.2 — 2026-10-26

- Tradução ambígua com equivalente fiel pode ser entregue sem nota quando o
  contrato proibir explicações.
- Contratos incompatíveis usam o impedimento autorizado ou suspendem a entrega
  antes do artefato, sem disfarçar perguntas em campos de tradução.
- Solicitação de contexto ou ajuste restrita à necessidade demonstrada.
- Vinte casos de ambiguidade e formato, com desfechos separados, além da
  reexecução das quatro baterias anteriores.
- Verificação de limites dos valores textuais decodificados em JSON.

Método, resultados e limites: [contratos ambíguos](docs/contratos-ambiguos.md).

## 0.1.1 — 2026-10-26

- Instruções de atualização, instalação por tag, retorno à versão anterior e
  migração de cópia local para origem remota.
- Alerta sobre o comportamento mutável de `check` observado no Skills CLI 1.7.4.
- Validação de instalação e recuperação em pastas de projeto isoladas.

As regras linguísticas, referências e resultados semânticos da v0.1.0 não foram
alterados. Procedimento e limites: [guia de atualização](docs/atualizacao.md).

## 0.1.0 — 2026-10-26

Primeira versão numerada da PTS-BR. As publicações anteriores permanecem
identificáveis pelos commits e relatórios de cada rodada.

- Avaliação completa das três baterias existentes e 12 casos de estabilidade.
- Ficha semântica com critérios, evidências e gravidade das falhas.
- Orientações para preservar a entidade qualificada e a força de uma expectativa.
- Modelo copiável de glossário do projeto.
- Verificação de limites de caracteres, integridade dos artefatos e links locais.
- Comando único de checagem e workflow do GitHub Actions com permissões de leitura.

Resultados, correções e limites: [avaliação v0.1.0](docs/avaliacao-v0.1.0.md).

## Política de versões

Use uma nova versão para publicar alterações. Registre mudanças de regras,
terminologia e contratos que possam mudar a resposta, além das validações feitas.
Uma versão de correção pode ajustar instruções sem garantir respostas idênticas:
a geração depende do modelo e do contexto. Não sobrescreva resultados históricos.
