"""Confere contratos e elementos literais; não avalia equivalência semântica."""

import argparse
import json
from pathlib import Path
import re


def objeto_sem_duplicatas(pares):
    objeto = dict(pares)
    if len(objeto) != len(pares):
        raise ValueError("JSON contém chaves duplicadas")
    return objeto


def conferir(casos, resultados, parcial=False):
    erros = []
    if not isinstance(resultados, list) or not resultados:
        return ["Resultados devem ser uma lista não vazia"]
    por_id = {}
    for item in resultados:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            erros.append("Resultado sem id válido")
            continue
        if item["id"] in por_id:
            erros.append(f"{item['id']}: id duplicado")
        por_id[item["id"]] = item.get("resposta")
    conhecidos = {caso["id"] for caso in casos}
    erros.extend(f"{id_}: caso desconhecido" for id_ in por_id.keys() - conhecidos)
    for caso in casos:
        id_ = caso["id"]
        if id_ not in por_id:
            if not parcial:
                erros.append(f"{id_}: resultado ausente")
            continue
        texto = por_id[id_]
        if not isinstance(texto, str):
            erros.append(f"{id_}: resposta deve ser string")
            continue
        for literal in caso.get("literais", []):
            if literal not in texto:
                erros.append(f"{id_}: elemento literal alterado ou ausente: {literal!r}")
        formato = caso.get("formato")
        if formato == "exato" and texto != caso["esperado"]:
            erros.append(f"{id_}: saída difere do texto exigido")
        if formato == "tabela" and not re.search(
            r"^\s*\|(?:\s*:?-{3,}:?\s*\|){2,}\s*$", texto, re.MULTILINE
        ):
            erros.append(f"{id_}: tabela Markdown não encontrada")
        if formato != "json":
            continue
        try:
            objeto = json.loads(texto, object_pairs_hook=objeto_sem_duplicatas)
        except (ValueError, TypeError):
            erros.append(f"{id_}: JSON inválido, duplicado ou acompanhado de texto externo")
            continue
        if not isinstance(objeto, dict) or set(objeto) != set(caso["chaves"]):
            erros.append(f"{id_}: chaves do contrato alteradas")
            continue
        for chave, esperado in caso.get("valores_fixos", {}).items():
            valor = objeto[chave]
            if type(valor) is not type(esperado) or valor != esperado:
                erros.append(f"{id_}: valor ou tipo alterado em {chave}")
        for chave, tipo in caso.get("tipos", {}).items():
            valor = objeto[chave]
            valido = isinstance(valor, str) if tipo == "string" else (
                isinstance(valor, list) and all(isinstance(v, str) for v in valor)
            )
            if not valido:
                erros.append(f"{id_}: tipo incorreto em {chave}")
    return erros


def autoteste():
    casos = [{"id": "X", "formato": "json", "chaves": ["retry", "cmd"],
              "valores_fixos": {"retry": False}, "literais": ["a;b"]}]
    valido = [{"id": "X", "resposta": '{"retry":false,"cmd":"a;b"}'}]
    assert not conferir(casos, valido)
    ruins = [[], [{"id": "X", "resposta": '{"retry":0,"cmd":"a;b"}'}],
             [{"id": "X", "resposta": '{"retry":false,"cmd":"ab"}'}],
             [{"id": "X", "resposta": '```json\n{"retry":false,"cmd":"a;b"}\n```'}],
             [{"id": "X", "resposta": '{"retry":true,"retry":false,"cmd":"a;b"}'}],
             valido + valido]
    assert all(conferir(casos, resultado) for resultado in ruins)
    print("Autoteste: controle válido aprovado; seis controles inválidos rejeitados.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resultados", type=Path, nargs="?")
    parser.add_argument("--casos", type=Path, default=Path(__file__).with_name("casos.json"),
                        help="Arquivo da bateria; padrão: casos.json ao lado do verificador")
    parser.add_argument("--parcial", action="store_true", help="Aceita casos não executados")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        autoteste()
    else:
        if not args.resultados:
            parser.error("informe o arquivo de resultados ou --selftest")
        try:
            casos = json.loads(args.casos.read_text(encoding="utf-8"))
            resultados = json.loads(args.resultados.read_text(encoding="utf-8"))
        except (OSError, ValueError) as erro:
            parser.error(str(erro))
        erros = conferir(casos, resultados, args.parcial)
        if erros:
            print("\n".join(erros))
            raise SystemExit(1)
        print(f"Checagens mecânicas aprovadas: {len(resultados)} casos. Revisão semântica não incluída.")
