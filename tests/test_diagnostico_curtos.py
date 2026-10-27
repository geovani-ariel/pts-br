import unittest

from verificar_diagnostico import cobertura_diagnostico, conferir_cobertura


class CoberturaDiagnosticoTest(unittest.TestCase):
    def setUp(self):
        self.linhas = [{'fase': f, 'id': i, 'repeticao': r}
                       for f, i, r in cobertura_diagnostico()]

    def test_aceita_162_execucoes_distintas(self):
        self.assertEqual(len(self.linhas), 162)
        self.assertEqual(conferir_cobertura(self.linhas), [])

    def test_rejeita_execucao_ausente(self):
        self.assertTrue(conferir_cobertura(self.linhas[:-1]))

    def test_rejeita_duplicata_no_lugar_de_outro_caso(self):
        self.linhas[-1] = self.linhas[0]
        self.assertTrue(conferir_cobertura(self.linhas))


if __name__ == '__main__':
    unittest.main()
