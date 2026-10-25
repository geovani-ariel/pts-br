"""Testa a seleção de uma bateria externa sem silenciar violações."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class BateriaExternaTest(unittest.TestCase):
    def executar(self, resposta):
        with tempfile.TemporaryDirectory() as pasta:
            pasta = Path(pasta)
            casos = pasta / "casos.json"
            resultados = pasta / "resultados.json"
            casos.write_text(json.dumps([{"id": "EXTRA", "literais": ["--dry-run"]}]), encoding="utf-8")
            resultados.write_text(json.dumps([{"id": "EXTRA", "resposta": resposta}]), encoding="utf-8")
            return subprocess.run(
                [sys.executable, "-B", str(Path(__file__).with_name("verificar.py")),
                 "--casos", str(casos), str(resultados)],
                capture_output=True, text=True, check=False,
            )

    def test_aceita_bateria_externa_com_resultado_valido(self):
        resultado = self.executar("Execute com --dry-run.")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)

    def test_rejeita_literal_alterado_na_bateria_externa(self):
        resultado = self.executar("Execute sem essa opção.")
        self.assertEqual(resultado.returncode, 1, resultado.stderr)


if __name__ == "__main__":
    unittest.main()
