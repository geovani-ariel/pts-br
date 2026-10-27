"""Confere evidência de leitura e registros salvos; não seleciona skills nem julga sentido."""

import hashlib
import json
from pathlib import Path

from verificar import conferir

PASTA = Path('tests/uso-automatico')
DOCUMENTOS = {'U01': 'procedimento', 'U02': 'api', 'U03': 'incidente'}


def leitura_registrada(leituras, arquivo, sha256):
    return any(item.get('arquivo') == arquivo and item.get('sha256') == sha256
               for item in leituras)


def recibo_corresponde(recibo, arquivo, conteudo):
    return (recibo.get('arquivo') == arquivo and recibo.get('bytes') == len(conteudo)
            and recibo.get('sha256') == hashlib.sha256(conteudo).hexdigest())


def conferir_criterios(caso, criterios):
    esperados = set(range(1, len(caso['criterios_semanticos']) + 1))
    if len(criterios) != len(esperados) or {c['indice'] for c in criterios} != esperados:
        return [f"{caso['id']}: cobertura incompleta ou duplicada dos critérios"]
    if any(c['resultado'] != 'aprovado' for c in criterios):
        return [f"{caso['id']}: critério sem aprovação registrada"]
    return []


def conferir_documentos(raiz, registro):
    pasta = raiz / PASTA
    casos = json.loads((pasta / 'casos.json').read_text(encoding='utf-8'))
    if len(casos) != 3 or {c['id']: c['documento'] for c in casos} != DOCUMENTOS:
        return ['A rodada deve conter os três documentos U01, U02 e U03']
    nomes = ['casos.json', 'pedido.txt', 'acordos.md', 'revisao.json',
             'intermediaria-procedimento.md']
    nomes += [f'{grupo}/{nome}.md' for grupo in ['entradas', 'saidas']
              for nome in DOCUMENTOS.values()]
    exigidos = {(PASTA / nome).as_posix() for nome in nomes} | {'tests/ler_registrando.py'}
    erros = []
    if exigidos - registro['arquivos_sha256'].keys():
        erros.append('Hashes obrigatórios ausentes na rodada de documentos')
    if set(registro['leituras']) != set(DOCUMENTOS):
        erros.append('Evidência de leitura incompleta nos três documentos')
    if set(registro['finalizacao']) != set(DOCUMENTOS):
        erros.append('Finalização incompleta nos três documentos')
    pedido = (pasta / 'pedido.txt').read_text(encoding='utf-8')
    if 'pts-br' in pedido.lower():
        erros.append('Pedido menciona a skill; não caracteriza esta avaliação de uso automático')
    sha_skill = hashlib.sha256((raiz / 'SKILL.md').read_bytes()).hexdigest()
    if registro['skill_sha256'] != sha_skill:
        erros.append('As instruções atuais diferem das instruções lidas nesta rodada')
    revisoes = json.loads((pasta / 'revisao.json').read_text(encoding='utf-8'))
    if len(revisoes) != 3 or {r['id'] for r in revisoes} != set(DOCUMENTOS):
        return erros + ['Revisão sem cobertura exata dos três documentos']
    por_id = {r['id']: r for r in revisoes}
    resultados = []
    for caso in casos:
        id_ = caso['id']
        if caso['prompt'] != pedido.strip():
            erros.append(f'{id_}: pedido registrado difere do pedido executado')
        entrada = pasta / 'entradas' / f"{caso['documento']}.md"
        sha_entrada = hashlib.sha256(entrada.read_bytes()).hexdigest()
        leituras = registro['leituras'].get(id_, [])
        if not leitura_registrada(leituras, 'runtime/skills/pts-br/SKILL.md', sha_skill):
            erros.append(f'{id_}: leitura das instruções da PTS-BR não registrada')
        if not leitura_registrada(leituras, 'caso/entrada.md', sha_entrada):
            erros.append(f'{id_}: leitura do documento de entrada não registrada')
        if not any(r.get('arquivo') == 'caso/AGENTS.md' for r in leituras):
            erros.append(f'{id_}: leitura dos acordos não registrada')
        revisao = por_id[id_]
        erros.extend(conferir_criterios(caso, revisao['criterios']))
        if revisao['resultado'] != 'aprovado' or any(
            f['gravidade'] in ['material', 'crítica'] for f in revisao['falhas']
        ):
            erros.append(f'{id_}: revisão com falha ou pendência')
        saida = pasta / 'saidas' / f"{caso['documento']}.md"
        if not recibo_corresponde(registro['finalizacao'].get(id_, {}),
                                 saida.relative_to(raiz).as_posix(), saida.read_bytes()):
            erros.append(f'{id_}: finalização diverge do artefato publicado')
        lida = pasta / 'intermediaria-procedimento.md' if id_ == 'U01' else saida
        recibos_saida = [r for r in leituras if r.get('arquivo') == 'caso/saida.md']
        if not recibos_saida or not all(
            recibo_corresponde(r, 'caso/saida.md', lida.read_bytes()) for r in recibos_saida
        ):
            erros.append(f'{id_}: recibo da saída lida diverge da versão identificada')
        texto = saida.read_text(encoding='utf-8')
        resultados.append({'id': id_, 'resposta': texto})
    erros.extend(conferir(casos, resultados))
    return erros
