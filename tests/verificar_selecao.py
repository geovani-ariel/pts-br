"""Audita medições salvas de seleção; não promete acionamento nem chama modelos."""

import hashlib
import json
from pathlib import Path
import re
import shlex

PASTA = Path('tests/selecao-descricao')
IDS = {f'I{i:02}' for i in range(1, 13)}
FASES = {'original': IDS, 'candidata-a': IDS, 'candidata-b': IDS,
         'contexto-ampliado': {'I01', 'I03', 'I06', 'I08'}}


def ha_leitura_skill(comandos):
    for item in comandos:
        if item.get('status') != 'completed' or item.get('exit_code') != 0:
            continue
        trecho = item.get('trecho_skill', '')
        if 'name: pts-br' not in trecho or '# PTS-BR' not in trecho:
            continue
        comando = item.get('comando', '')
        try:
            partes = shlex.split(comando)
        except ValueError:
            continue
        if partes and Path(partes[0]).name in ['sh', 'bash', 'zsh'] and '-lc' in partes:
            comando = partes[-1]
        for segmento in re.split(r'[;\n|&]+', comando):
            if (re.match(r'^\s*(?:cat|sed|head|tail)\s', segmento)
                    and 'pts-br/SKILL.md' in segmento):
                return True
    return False


def conferir_correcoes(textos, falhas):
    if (not isinstance(textos, list) or len(textos) != len(falhas)
            or any(not isinstance(t, dict) for t in textos)
            or {t.get('id') for t in textos} != set(falhas)):
        return ['Seleção: correções editoriais ausentes, duplicadas ou de outro caso']
    if any(not isinstance(t.get('resposta_corrigida'), str)
           or not t['resposta_corrigida'].strip() for t in textos):
        return ['Seleção: correção editorial sem texto válido']
    return []


def conferir_selecao(raiz, registro):
    pasta = raiz / PASTA
    casos = json.loads((pasta / 'casos.json').read_text(encoding='utf-8'))
    if len(casos) != 12 or {c['id'] for c in casos} != IDS:
        return ['Seleção: casos ausentes ou duplicados']
    if any('pts-br' in c['prompt'].lower() for c in casos):
        return ['Seleção: pedido contém invocação nominal da skill']
    nomes = ['casos.json', 'revisao-semantica.json', 'correcoes-editoriais.json',
             'revisao-correcoes.json'] + [nome + '.json' for nome in FASES]
    exigidos = {(PASTA / nome).as_posix() for nome in nomes}
    erros = []
    if exigidos - registro['arquivos_sha256'].keys():
        erros.append('Seleção: hashes obrigatórios ausentes')
    atual = (raiz / 'SKILL.md').read_bytes()
    if registro['descricoes']['original']['skill_sha256'] != hashlib.sha256(atual).hexdigest():
        erros.append('Seleção: descrição original não corresponde à publicada')
    if len({d['corpo_sha256'] for d in registro['descricoes'].values()}) != 1:
        erros.append('Seleção: candidatas alteraram o corpo da skill')
    for descricao in registro['descricoes'].values():
        conteudo = (raiz / descricao['arquivo']).read_bytes()
        corpo = conteudo.decode('utf-8').partition('\n---\n')[2].encode('utf-8')
        if (hashlib.sha256(conteudo).hexdigest() != descricao['skill_sha256']
                or hashlib.sha256(corpo).hexdigest() != descricao['corpo_sha256']):
            erros.append('Seleção: snapshot da descrição não corresponde ao registro')
    controles = registro['controle_AGENTS']
    if (controles['0']['resposta'] != 'NÃO INFORMADO'
            or controles['32768']['resposta'] != 'PROJETO_CANARIO_Q7M4Z9'
            or any(c['exit_code'] != 0 or c['executou_comando'] for c in controles.values())):
        erros.append('Seleção: controle de isolamento de AGENTS não confirmado')
    if any('PROJETO_CANARIO_Q7M4Z9' in c['prompt'] for c in controles.values()):
        erros.append('Seleção: marcador de AGENTS vazou para o pedido do controle')
    esperados = {c['id']: c['selecionar'] for c in casos}
    for fase, ids in FASES.items():
        linhas = json.loads((pasta / (fase + '.json')).read_text(encoding='utf-8'))
        if len(linhas) != len(ids) or {r['id'] for r in linhas} != ids:
            erros.append(f'Seleção {fase}: execução incompleta ou duplicada')
            continue
        omitidos = []
        excessos = []
        positivos = sum(esperados[i] for i in ids)
        for linha in linhas:
            args = linha['argumentos']
            pares = list(zip(args, args[1:]))
            if (linha['exit_code'] != 0 or not linha['turno_concluido']
                    or not linha['resposta'].strip() or '--ignore-user-config' not in args
                    or ('-c', 'project_doc_max_bytes=0') not in pares
                    or ('--sandbox', 'read-only') not in pares or '--ephemeral' not in args):
                erros.append(f"Seleção {fase}/{linha['id']}: execução ou isolamento inválido")
            if (fase == 'contexto-ampliado') != (('-c', 'skills.max_context_tokens=10000') in pares):
                erros.append(f"Seleção {fase}/{linha['id']}: orçamento de contexto não corresponde à fase")
            if any('AGENTS.md' in c['comando'] for c in linha['comandos']):
                erros.append(f"Seleção {fase}/{linha['id']}: leitura manual de AGENTS contamina o caso")
            leu = ha_leitura_skill(linha['comandos'])
            if esperados[linha['id']] and not leu:
                omitidos.append(linha['id'])
            if not esperados[linha['id']] and leu:
                excessos.append(linha['id'])
        # A medição preserva as omissões; passar este gate não as resolve.
        print(f'Seleção {fase}: {positivos - len(omitidos)}/{positivos} positivos; '
              f'{len(ids) - positivos - len(excessos)}/{len(ids) - positivos} negativos. '
              f'Omissões: {", ".join(omitidos) or "nenhuma"}; excessos: {", ".join(excessos) or "nenhum"}.')
    revisao = json.loads((pasta / 'revisao-semantica.json').read_text(encoding='utf-8'))
    if len(revisao) != 12 or {r['id'] for r in revisao} != IDS:
        erros.append('Seleção: revisão sem cobertura dos 12 casos')
    if any(r['rotulo_de_escopo'] != 'coerente'
           or r['resultado_semantico'] not in ['aprovado', 'falha'] for r in revisao):
        erros.append('Seleção: revisão diverge do escopo ou tem resultado desconhecido')
    falhas = sorted(r['id'] for r in revisao if r['resultado_semantico'] == 'falha')
    if falhas != registro['falhas_semanticas_originais']:
        erros.append('Seleção: falhas semânticas não preservadas no registro')
    print('Falhas semânticas nas respostas automáticas originais: ' + ', '.join(falhas))
    textos = json.loads((pasta / 'correcoes-editoriais.json').read_text(encoding='utf-8'))
    erros.extend(conferir_correcoes(textos, falhas))
    correcoes = json.loads((pasta / 'revisao-correcoes.json').read_text(encoding='utf-8'))
    if (len(correcoes) != len(falhas) or {r['id'] for r in correcoes} != set(falhas)
            or any(r['resultado_semantico'] != 'aprovado' for r in correcoes)):
        erros.append('Seleção: correções editoriais sem revisão aprovada')
    return erros
