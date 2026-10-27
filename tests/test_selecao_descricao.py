"""Evita contar menções ou comandos malsucedidos como leitura de uma skill."""

import unittest

from verificar_selecao import conferir_correcoes, ha_leitura_skill


class EvidenciaSelecaoTest(unittest.TestCase):
    def evento(self, comando='cat <runtime>/skills/pts-br/SKILL.md', **mudancas):
        item = {'comando': comando, 'status': 'completed', 'exit_code': 0,
                'trecho_skill': 'name: pts-br\n# PTS-BR — Português Técnico Simplificado Brasileiro'}
        item.update(mudancas)
        return item

    def test_aceita_leitura_concluida_com_conteudo(self):
        self.assertTrue(ha_leitura_skill([self.evento()]))

    def test_rejeita_mencao_em_echo(self):
        self.assertFalse(ha_leitura_skill([self.evento('echo <runtime>/skills/pts-br/SKILL.md')]))

    def test_rejeita_comando_que_falhou(self):
        self.assertFalse(ha_leitura_skill([self.evento(exit_code=1)]))

    def test_rejeita_evento_sem_conclusao(self):
        self.assertFalse(ha_leitura_skill([self.evento(status='in_progress')]))

    def test_rejeita_caminho_ou_conteudo_incorreto(self):
        self.assertFalse(ha_leitura_skill([self.evento('cat <runtime>/skills/pts-br/references/glossario.md')]))
        self.assertFalse(ha_leitura_skill([self.evento(trecho_skill='outro texto')]))
        self.assertFalse(ha_leitura_skill([]))


class CorrecoesEditoriaisTest(unittest.TestCase):
    def test_aceita_textos_para_as_duas_falhas(self):
        self.assertEqual(conferir_correcoes([
            {'id': 'I09', 'resposta_corrigida': 'A ferramenta pode remover.'},
            {'id': 'I10', 'resposta_corrigida': 'Não houve deploy.'},
        ], ['I09', 'I10']), [])

    def test_rejeita_correcao_ausente_ou_duplicada(self):
        for textos in [[], [{'id': 'I09', 'resposta_corrigida': 'Texto.'}] * 2]:
            with self.subTest(textos=textos):
                self.assertTrue(conferir_correcoes(textos, ['I09', 'I10']))

    def test_rejeita_correcao_sem_texto_valido(self):
        for texto in ['', '  ', None, 3]:
            with self.subTest(texto=texto):
                self.assertTrue(conferir_correcoes([
                    {'id': 'I09', 'resposta_corrigida': texto},
                ], ['I09']))


if __name__ == '__main__':
    unittest.main()
