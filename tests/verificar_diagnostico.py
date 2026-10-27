"""Confere o diagnóstico salvo; não executa modelos nem transforma omissões em acertos."""

import hashlib
import json
from pathlib import Path

from verificar_selecao import ha_leitura_skill

PASTA = Path('tests/diagnostico-curtos')
CURTOS = {'I01', 'I03', 'I05', 'I06', 'I07', 'I08', 'I09', 'I10', 'I11', 'I12'}
SUBCONJUNTO = {'I01', 'I03', 'I06', 'I08'}
FASES = {'original': CURTOS, 'curta': CURTOS, 'leia': SUBCONJUNTO,
         'original-contexto': SUBCONJUNTO, 'original-alto': SUBCONJUNTO,
         'explicita': {'I01', 'I03'}}


def cobertura_diagnostico():
    return {(f, i, r) for f, ids in FASES.items() for i in ids
            for r in range(1, 2 if f == 'explicita' else 6)}


def conferir_cobertura(linhas):
    esperado = cobertura_diagnostico()
    observado = {(r['fase'], r['id'], r['repeticao']) for r in linhas}
    if len(linhas) != len(esperado) or observado != esperado:
        return ['Diagnóstico: execuções ausentes, duplicadas ou inesperadas']
    return []


def conferir_diagnostico(raiz, registro):
    linhas = json.loads((raiz / PASTA / 'resultados.json').read_text(encoding='utf-8'))
    erros = conferir_cobertura(linhas)
    casos = {c['id']: c for c in json.loads((raiz / registro['arquivo_casos']).read_text(encoding='utf-8'))}
    snapshots = {k: (raiz / v).read_bytes() for k, v in registro['snapshots'].items()}
    obrigatorios = {PASTA / n for n in ['resultados.json', 'skill-curta.txt', 'skill-leia.txt',
                                       'revisao-independente.json', 'catalogo-local.json']}
    if {p.as_posix() for p in obrigatorios} - registro['arquivos_sha256'].keys():
        erros.append('Diagnóstico: hashes obrigatórios ausentes')
    if (hashlib.sha256(snapshots['original']).hexdigest() != registro['skill_original_sha256']
            or len({s.partition(b'\n---\n')[2] for s in snapshots.values()}) != 1):
        erros.append('Diagnóstico: fonte original ou corpo das candidatas diverge')
    revisoes = json.loads((raiz / PASTA / 'revisao-independente.json').read_text(encoding='utf-8'))['resultados']
    textos = {(r['fase'], r['id'], r['repeticao']): r['resposta'] for r in linhas}
    esperadas = {(r['fase'], r['id'], r['repeticao']) for r in linhas if casos[r['id']]['selecionar']}
    if (len(revisoes) != len(esperadas)
            or {(r['fase'], r['id'], r['repeticao']) for r in revisoes} != esperadas
            or any(r['resultado_semantico'] not in ['aprovado', 'falha'] for r in revisoes)):
        erros.append('Diagnóstico: revisão sem cobertura exata das respostas técnicas')
    for revisao in revisoes:
        chave = (revisao['fase'], revisao['id'], revisao['repeticao'])
        if hashlib.sha256(textos.get(chave, '').encode()).hexdigest() != revisao['resposta_sha256']:
            erros.append('Diagnóstico: revisão diverge da resposta avaliada')
    for r in linhas:
        args = r['argumentos']
        pares = list(zip(args, args[1:]))
        fase = r['fase']
        fonte = fase if fase in ['curta', 'leia'] else 'original'
        prompt = ('Use $pts-br. ' if fase == 'explicita' else '') + casos[r['id']]['prompt']
        if (r['exit_code'] != 0 or not r['turno_concluido'] or not r['resposta'].strip()
                or r['prompt'] != prompt or '--ignore-user-config' not in args
                or '--ephemeral' not in args or ('--sandbox', 'read-only') not in pares
                or ('-m', 'gpt-6-astra') not in pares or ('-c', 'project_doc_max_bytes=0') not in pares
                or ('-c', 'model_reasoning_effort="high"' if fase == 'original-alto'
                    else 'model_reasoning_effort="low"') not in pares
                or ((fase == 'original-contexto') != (('-c', 'skills.max_context_tokens=10000') in pares))
                or r['skill_sha256'] != hashlib.sha256(snapshots[fonte]).hexdigest()
                or any('AGENTS.md' in c['comando'] for c in r['comandos'])):
            erros.append(f"Diagnóstico: execução inválida {fase}/{r['id']}/{r['repeticao']}")
    for fase in FASES:
        if fase == 'explicita':
            continue  # O runtime pode injetar o corpo sem comando de leitura.
        grupo = [r for r in linhas if r['fase'] == fase]
        positivos = [r for r in grupo if casos[r['id']]['selecionar']]
        negativos = [r for r in grupo if not casos[r['id']]['selecionar']]
        print(f'Diagnóstico {fase}: leitura em {sum(ha_leitura_skill(r["comandos"]) for r in positivos)}'
              f'/{len(positivos)} positivos; '
              f'{sum(ha_leitura_skill(r["comandos"]) for r in negativos)}/{len(negativos)} excessos.')
    print('Controle explícito separado: ausência de comando não mede ausência de injeção pelo runtime.')
    return erros
