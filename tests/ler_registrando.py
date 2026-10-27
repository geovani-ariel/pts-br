"""Leitura instrumentada para a avaliação; imprime o arquivo e registra seu hash."""
import hashlib
import json
from pathlib import Path
import sys

arquivo = Path(sys.argv[1]).expanduser().resolve()
conteudo = arquivo.read_bytes()
registro = {"arquivo": str(arquivo), "sha256": hashlib.sha256(conteudo).hexdigest(), "bytes": len(conteudo)}
with Path("leituras.jsonl").open("a", encoding="utf-8") as log:
    log.write(json.dumps(registro, ensure_ascii=False) + "\n")
print(conteudo.decode("utf-8"), end="")
