"""Controles negativos para leitura registrada e cobertura da revisão longa."""

import hashlib
import unittest

from verificar_documentos import conferir_criterios, leitura_registrada, recibo_corresponde


class LeituraRegistradaTest(unittest.TestCase):
    def test_aceita_arquivo_e_hash_corretos(self):
        self.assertTrue(leitura_registrada([{'arquivo': 'runtime/skills/pts-br/SKILL.md',
                                            'sha256': 'abc'}],
                                          'runtime/skills/pts-br/SKILL.md', 'abc'))

    def test_rejeita_ausencia_de_leitura(self):
        self.assertFalse(leitura_registrada([], 'runtime/skills/pts-br/SKILL.md', 'abc'))

    def test_rejeita_hash_de_outra_versao(self):
        self.assertFalse(leitura_registrada([{'arquivo': 'runtime/skills/pts-br/SKILL.md',
                                             'sha256': 'antigo'}],
                                           'runtime/skills/pts-br/SKILL.md', 'abc'))

    def test_rejeita_mencao_em_outro_arquivo(self):
        self.assertFalse(leitura_registrada([{'arquivo': 'caso/pedido.txt', 'sha256': 'abc'}],
                                           'runtime/skills/pts-br/SKILL.md', 'abc'))


class CoberturaCriteriosTest(unittest.TestCase):
    caso = {'id': 'U01', 'criterios_semanticos': ['Condição', 'Exceção']}

    def test_aceita_cobertura_completa(self):
        self.assertEqual(conferir_criterios(self.caso, [
            {'indice': 1, 'resultado': 'aprovado'}, {'indice': 2, 'resultado': 'aprovado'},
        ]), [])

    def test_rejeita_criterio_omitido_ou_duplicado(self):
        for indices in [[1], [1, 1]]:
            with self.subTest(indices=indices):
                self.assertTrue(conferir_criterios(self.caso, [
                    {'indice': i, 'resultado': 'aprovado'} for i in indices
                ]))


class FinalizacaoTest(unittest.TestCase):
    def test_aceita_recibo_do_artefato_final(self):
        corpo = b'documento final'
        recibo = {'arquivo': 'saida.md', 'bytes': len(corpo),
                  'sha256': hashlib.sha256(corpo).hexdigest()}
        self.assertTrue(recibo_corresponde(recibo, 'saida.md', corpo))

    def test_rejeita_recibo_anterior_a_edicao(self):
        corpo = b'versao intermediaria'
        recibo = {'arquivo': 'saida.md', 'bytes': len(corpo),
                  'sha256': hashlib.sha256(corpo).hexdigest()}
        self.assertFalse(recibo_corresponde(recibo, 'saida.md', b'versao final'))
        self.assertFalse(recibo_corresponde({}, 'saida.md', b'versao final'))


if __name__ == '__main__':
    unittest.main()
