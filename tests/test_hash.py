"""
Algoritmos de PCS3110 em Python
Testes / Exemplos
"""
from modulo1.hash import TabelaHash
from modulo1.hash import Elemento
import unittest

class TestHash(unittest.TestCase):
    def test_insere_e_busca_sem_colisao(self):
        hash = TabelaHash(10)
        elementos = [Elemento(3), Elemento(4), Elemento(2), Elemento(9)]
        for e in elementos:
            hash.insere(e)

        self.assertEqual(hash.busca(3), elementos[0])
        self.assertEqual(hash.busca(4), elementos[1])
        self.assertEqual(hash.busca(2), elementos[2])
        self.assertEqual(hash.busca(9), elementos[3])

    def test_insere_sem_espaco(self):
        hash = TabelaHash(4)
        elementos = [Elemento(3), Elemento(4), Elemento(2), Elemento(9)]
        for e in elementos:
            hash.insere(e)
        self.assertRaises(RuntimeError, hash.insere, Elemento(1))

    def test_insere_e_busca_com_colisao_sem_volta(self):
        hash = TabelaHash(10)
        elementos = [Elemento(3), Elemento(4), Elemento(2), Elemento(9), Elemento(14), Elemento(15)]
        for e in elementos:
            hash.insere(e)

        self.assertEqual(hash.busca(3), elementos[0])
        self.assertEqual(hash.busca(4), elementos[1])
        self.assertEqual(hash.busca(2), elementos[2])
        self.assertEqual(hash.busca(9), elementos[3])
        self.assertEqual(hash.busca(14), elementos[4])
        self.assertEqual(hash.busca(15), elementos[5])

    def test_insere_e_busca_com_colisao_com_volta(self):
        hash = TabelaHash(10)
        elementos = [Elemento(1), Elemento(9), Elemento(19), Elemento(29), Elemento(39)]
        for e in elementos:
            hash.insere(e)

        self.assertEqual(hash.busca(1), elementos[0])
        self.assertEqual(hash.busca(9), elementos[1])
        self.assertEqual(hash.busca(19), elementos[2])
        self.assertEqual(hash.busca(29), elementos[3])
        self.assertEqual(hash.busca(39), elementos[4])

    def test_remove(self):
        hash = TabelaHash(10)
        elementos = [Elemento(1), Elemento(9), Elemento(19), Elemento(29), Elemento(39)]
        for e in elementos:
            hash.insere(e)

        hash.remove(elementos[1])
        self.assertIsNone(hash.busca(9))
        hash.remove(elementos[3])
        self.assertIsNone(hash.busca(29))

    def test_remove_com_insercao(self):
        hash = TabelaHash(5)
        elementos = [Elemento(1), Elemento(9), Elemento(19), Elemento(29), Elemento(39)]
        for e in elementos:
            hash.insere(e)

        novo1 = Elemento(49)
        novo2 = Elemento(59)

        hash.remove(elementos[1])
        self.assertIsNone(hash.busca(9))
        hash.remove(elementos[2])
        self.assertIsNone(hash.busca(19))

        hash.insere(novo1)
        self.assertEqual(hash.busca(49), novo1)
        hash.insere(novo2)
        self.assertEqual(hash.busca(59), novo2)


def test_remove_elemento_inexistente(self):
    hash = TabelaHash(10)
    elementos = [Elemento(1), Elemento(9)]
    for e in elementos:
        hash.insere(e)
    
    self.assertRaises(ValueError, hash.remove, Elemento(2))
