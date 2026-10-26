"""Executa checagens locais e de CI; não gera respostas nem julga seu sentido."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from verificar import conferir

RAIZ = Path(__file__).resolve().parents[1]
AVALIACAO = Path('tests/avaliacoes/v0.1.0')
BATERIAS = [
    {'casos': f'tests/{casos}.json',
     'resultados': (AVALIACAO / f'respostas-{nome}.json').as_posix()}
    for casos, nome in [('casos', 'original'), ('casos-asd', 'asd'),
                        ('casos-dificeis', 'dificeis'), ('casos-estabilidade', 'estabilidade')]
]
REVISOES = [(AVALIACAO / f'revisao-{nome}.json').as_posix()
            for nome in ['original-asd', 'dificeis-estabilidade']]


def conferir_manifesto(raiz, manifesto):
    erros = []
    if manifesto['baterias'] != BATERIAS or manifesto['revisoes'] != REVISOES:
        erros.append('Manifesto deve registrar as quatro baterias e as duas revisões da versão')
    obrigatorios = {'SKILL.md', *REVISOES}
    obrigatorios.update(p.relative_to(raiz).as_posix() for p in (raiz / 'references').glob('*.md'))
    obrigatorios.update(nome for bateria in BATERIAS for nome in bateria.values())
    ausentes = obrigatorios - manifesto['arquivos_sha256'].keys()
    if ausentes:
        erros.append('Hashes obrigatórios ausentes: ' + ', '.join(sorted(ausentes)))
    return erros


def conferir_integridade(raiz, arquivos):
    erros = []
    for nome, esperado in arquivos.items():
        arquivo = raiz / nome
        if not arquivo.is_file():
            erros.append(f'Arquivo ausente: {nome}')
        elif hashlib.sha256(arquivo.read_bytes()).hexdigest() != esperado:
            erros.append(f'Hash divergente; requer nova avaliação ou registro: {nome}')
    return erros


def conferir_links(raiz):
    arquivos = list(raiz.glob('*.md'))
    for pasta in ['docs', 'references', 'examples', 'templates']:
        arquivos.extend((raiz / pasta).rglob('*.md'))
    erros = []
    for arquivo in arquivos:
        for destino in re.findall(r'\]\(([^\s)]+)\)', arquivo.read_text(encoding='utf-8')):
            destino = destino.strip('<>')
            url = urlsplit(destino)
            if url.scheme or url.netloc or not url.path:
                continue
            if not (arquivo.parent / unquote(url.path)).exists():
                erros.append(f'{arquivo.relative_to(raiz)}: link local ausente: {destino}')
    return erros


def ler_json(caminho):
    return json.loads(caminho.read_text(encoding='utf-8'))


def checar(raiz):
    erros = conferir_links(raiz)
    manifesto = ler_json(raiz / AVALIACAO / 'manifesto.json')
    erros.extend(conferir_manifesto(raiz, manifesto))
    if erros:
        return erros
    erros.extend(conferir_integridade(raiz, manifesto['arquivos_sha256']))
    # As amostras históricas continuam sendo conferidas, sem sobrescrevê-las.
    baterias = [('casos.json', 'resultados.json'),
                ('casos-asd.json', 'resultados-asd.json'),
                ('casos-dificeis.json', 'resultados-dificeis.json')]
    for casos, resultados in baterias:
        erros.extend(conferir(ler_json(raiz / 'tests' / casos),
                              ler_json(raiz / 'tests' / resultados)))
    ids = set()
    for bateria in manifesto['baterias']:
        casos = ler_json(raiz / bateria['casos'])
        resultados = ler_json(raiz / bateria['resultados'])
        erros.extend(conferir(casos, resultados))
        atuais = {r['id'] for r in resultados}
        if ids & atuais:
            erros.append('IDs repetidos entre baterias da avaliação')
        ids.update(atuais)
    revisoes = [item for nome in manifesto['revisoes'] for item in ler_json(raiz / nome)]
    if len(revisoes) != len(ids) or {r['id'] for r in revisoes} != ids:
        erros.append('Revisão sem cobertura exata dos resultados da avaliação')
    for item in revisoes:
        if item['resultado'] != 'aprovado' or any(
            f['gravidade'] in ['crítica', 'material'] for f in item['falhas']
        ):
            erros.append(f"{item['id']}: revisão registra falha ou resultado pendente")
    return erros


if __name__ == '__main__':
    subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                    '-s', str(RAIZ / 'tests'), '-v'], check=True)
    subprocess.run([sys.executable, '-B', str(RAIZ / 'tests/verificar.py'), '--selftest'], check=True)
    try:
        erros = checar(RAIZ)
    except (OSError, ValueError, KeyError, TypeError) as erro:
        raise SystemExit(f'Não foi possível conferir os artefatos: {erro}')
    if erros:
        raise SystemExit('\n'.join(erros))
    print('Checagens aprovadas: amostras históricas, avaliação registrada, hashes e links locais.')
    print('As revisões semânticas salvas foram conferidas; nenhuma nova revisão por modelo foi executada.')
