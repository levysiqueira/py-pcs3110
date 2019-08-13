"""
Algoritmos de PCS3110 em Python
Testes / Exemplos
"""
from modulo2.arvore import No, Arvore, ABB
import unittest

class TestArvore(unittest.TestCase):
    def setUp(self):
        self.a = Arvore(No(1))

        esq = No(2, self.a.raiz)
        self.a.raiz.filho_esquerda = esq

        dir = No(3, self.a.raiz)
        self.a.raiz.filho_direita = dir

        esq_esq = No(4, esq)
        esq.filho_esquerda = esq_esq

        esq_dir = No(5, esq)
        esq.filho_direita = esq_dir

        dir_esq = No(6, dir)
        dir.filho_esquerda = dir_esq

        esq_esq_dir = No(7, esq_dir)
        esq_dir.filho_direita = esq_esq_dir
    
    def test_altura_total(self):
        self.assertEqual(self.a.altura_total(), 3)

    def test_altura_vazio(self):
        a = Arvore()
        self.assertEqual(a.altura(a.raiz), -1)
    
    def test_altura_raiz(self):
        self.assertEqual(self.a.altura(self.a.raiz), 3)

    def test_altura_folha(self):
        self.a.raiz = No(4)
        self.a.raiz.filho_esquerda = No(5)
        self.a.raiz.filho_esquerda.pai = self.a.raiz

        self.assertEqual(self.a.altura(self.a.raiz.filho_esquerda), 0)

    def test_pre_ordem(self):
        self.assertEqual(self.a.pre_ordem(), [1, 2, 4, 5, 7, 3, 6])
    
    def test_pos_ordem(self):
        self.assertEqual(self.a.pos_ordem(), [4, 7, 5, 2, 6, 3, 1])

    def test_em_ordem(self):
        self.assertEqual(self.a.em_ordem(), [4, 2, 5, 7, 1, 6, 3])
    
    def test_busca_encontra(self):
        a = ABB()
        a.adicionar(5)
        a.adicionar(3)
        a.adicionar(4)
        a.adicionar(2)
        a.adicionar(7)
        a.adicionar(8)
        a.adicionar(9)
        self.assertTrue(a.busca(2).chave, 2)
        self.assertTrue(a.busca(3).chave, 3)
        self.assertTrue(a.busca(4).chave, 4)
        self.assertTrue(a.busca(7).chave, 7)
        self.assertTrue(a.busca(8).chave, 8)
        self.assertTrue(a.busca(9).chave, 9)

    def test_busca_encontra_raiz(self):
        a = ABB()
        a.adicionar(5)
        a.adicionar(3)
        a.adicionar(4)
        a.adicionar(2)
        a.adicionar(7)
        a.adicionar(8)
        a.adicionar(9)

        self.assertTrue(a.busca(5).chave, 5)

    def test_busca_não_encontra(self):
        a = ABB()
        a.adicionar(5)
        a.adicionar(3)
        a.adicionar(4)
        a.adicionar(2)
        a.adicionar(7)
        a.adicionar(8)
        a.adicionar(9)

        self.assertIsNone(a.busca(1))
        self.assertIsNone(a.busca(6))
        self.assertIsNone(a.busca(10))

    def test_menor(self):
        a = ABB()
        a.adicionar(5)
        a.adicionar(3)
        a.adicionar(4)
        a.adicionar(2)
        a.adicionar(7)
        a.adicionar(8)
        a.adicionar(9)

        self.assertTrue(a.menor().chave, 2)

    def test_menor_so_raiz(self):
        a = ABB()
        a.adicionar(5)

        self.assertTrue(a.menor().chave, 5)

    def test_menor_vazia(self):
        a = ABB()
        self.assertIsNone(a.menor())

    def test_maior(self):
        a = ABB()
        a.adicionar(5)
        a.adicionar(3)
        a.adicionar(4)
        a.adicionar(2)
        a.adicionar(7)
        a.adicionar(8)
        a.adicionar(9)

        self.assertTrue(a.maior().chave, 9)

    def test_maior_so_raiz(self):
        a = ABB()
        a.adicionar(5)

        self.assertTrue(a.maior().chave, 5)

    def test_maior_vazia(self):
        a = ABB()
        self.assertIsNone(a.maior())
    
    def test_sucessor(self):
        a = ABB()
        a.adicionar(5)
        a.adicionar(3)
        a.adicionar(4)
        a.adicionar(2)
        a.adicionar(7)
        a.adicionar(8)
        a.adicionar(9)

        proximo = a.sucessor(a.menor())
        self.assertEqual(proximo.chave, 3)

        proximo = a.sucessor(proximo)
        self.assertEqual(proximo.chave, 4)

        proximo = a.sucessor(proximo)
        self.assertEqual(proximo.chave, 5)

        proximo = a.sucessor(proximo)
        self.assertEqual(proximo.chave, 7)

        proximo = a.sucessor(proximo)
        self.assertEqual(proximo.chave, 8)

        proximo = a.sucessor(proximo)
        self.assertEqual(proximo.chave, 9)