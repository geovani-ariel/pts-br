"""Controles negativos para a integridade da avaliação e os links locais."""

import hashlib
from pathlib import Path
import tempfile
import unittest

from checar import BATERIAS, REVISOES, conferir_integridade, conferir_links, conferir_manifesto


class ArtefatosTest(unittest.TestCase):
    def test_rejeita_manifesto_vazio(self):
        with tempfile.TemporaryDirectory() as pasta:
            self.assertTrue(conferir_manifesto(Path(pasta), {
                'arquivos_sha256': {}, 'baterias': [], 'revisoes': [],
            }))

    def test_rejeita_avaliacao_sem_hashes(self):
        with tempfile.TemporaryDirectory() as pasta:
            self.assertTrue(conferir_manifesto(Path(pasta), {
                'arquivos_sha256': {}, 'baterias': BATERIAS, 'revisoes': REVISOES,
            }))

    def test_detecta_resposta_alterada_ou_ausente(self):
        with tempfile.TemporaryDirectory() as pasta:
            raiz = Path(pasta)
            arquivo = raiz / 'respostas.json'
            arquivo.write_text('original', encoding='utf-8')
            hashes = {'respostas.json': hashlib.sha256(arquivo.read_bytes()).hexdigest()}
            self.assertEqual(conferir_integridade(raiz, hashes), [])
            arquivo.write_text('alterado', encoding='utf-8')
            self.assertTrue(conferir_integridade(raiz, hashes))
            arquivo.unlink()
            self.assertTrue(conferir_integridade(raiz, hashes))

    def test_detecta_link_local_quebrado_sem_exigir_rede(self):
        with tempfile.TemporaryDirectory() as pasta:
            raiz = Path(pasta)
            (raiz / 'README.md').write_text('[Guia](guia.md) [Web](https://example.com)', encoding='utf-8')
            self.assertEqual(len(conferir_links(raiz)), 1)
            (raiz / 'guia.md').write_text('# Guia', encoding='utf-8')
            self.assertEqual(conferir_links(raiz), [])


if __name__ == '__main__':
    unittest.main()
