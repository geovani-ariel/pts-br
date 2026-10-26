"""Testa baterias externas e contagem de marcadores sem silenciar violações."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from verificar import conferir


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


class OcorrenciasLiteraisTest(unittest.TestCase):
    casos = [{"id": "MARCADOR", "ocorrencias_literais": {"{name}": 2}}]

    def conferir_resposta(self, texto):
        return conferir(self.casos, [{"id": "MARCADOR", "resposta": texto}])

    def test_aceita_as_duas_ocorrencias_exigidas(self):
        self.assertEqual(self.conferir_resposta("{name} perguntou se {name} pode repetir."), [])

    def test_rejeita_perda_de_uma_ocorrencia(self):
        self.assertTrue(self.conferir_resposta("{name} perguntou se ele pode repetir."))

    def test_rejeita_uma_ocorrencia_adicional(self):
        self.assertTrue(self.conferir_resposta("{name} perguntou a {name} se {name} pode repetir."))


class LimiteCaracteresTest(unittest.TestCase):
    def test_aceita_limite_inclusivo(self):
        self.assertEqual(conferir(
            [{"id": "UI", "max_caracteres": 4}],
            [{"id": "UI", "resposta": "ação"}],
        ), [])

    def test_rejeita_texto_acima_do_limite(self):
        self.assertTrue(conferir(
            [{"id": "UI", "max_caracteres": 4}],
            [{"id": "UI", "resposta": "ações"}],
        ))


if __name__ == "__main__":
    unittest.main()
