from modulo2.grafo import GrafoDirigido
from modulo2.grafo import GrafoNaoDirigido
import unittest

class TestGrafo(unittest.TestCase):
    def test_adiciona_no(self):
        grafo = GrafoDirigido()
        self.assertEqual(len(grafo.nos), 0)

        grafo.adiciona('a')
        self.assertEqual(len(grafo.nos), 1)

        grafo.adiciona('b')
        self.assertEqual(len(grafo.nos), 2)

        grafo2 = GrafoDirigido(('a', 'b'))
        self.assertEqual(len(grafo2.nos), 2)


    def test_conecta(self):
        grafo = GrafoDirigido(('a', 'b'))

        self.assertFalse(grafo.possui_aresta('a', 'b'))
        self.assertFalse(grafo.possui_aresta('b', 'a'))

        grafo.conecta('a', 'b')
        
        self.assertTrue(grafo.possui_aresta('a', 'b'))
        self.assertFalse(grafo.possui_aresta('b', 'a'))

    def test_desconecta(self):
        grafo = GrafoDirigido(('a', 'b', 'c'))
        grafo.conecta('a', 'b')
        grafo.conecta('b', 'a')
        grafo.conecta('b', 'c')
        grafo.conecta('a', 'c')

        self.assertTrue(grafo.possui_aresta('a', 'b'))
        self.assertTrue(grafo.possui_aresta('b', 'a'))
        self.assertTrue(grafo.possui_aresta('b', 'c'))
        self.assertTrue(grafo.possui_aresta('a', 'c'))

        grafo.desconecta('a', 'c')
        self.assertTrue(grafo.possui_aresta('a', 'b'))
        self.assertTrue(grafo.possui_aresta('b', 'a'))
        self.assertTrue(grafo.possui_aresta('b', 'c'))
        self.assertFalse(grafo.possui_aresta('a', 'c'))

        grafo.desconecta('a', 'b')
        self.assertFalse(grafo.possui_aresta('a', 'b'))
        self.assertTrue(grafo.possui_aresta('b', 'a'))
        self.assertTrue(grafo.possui_aresta('b', 'c'))
        self.assertFalse(grafo.possui_aresta('a', 'c'))

    def test_peso(self):
        grafo = GrafoDirigido(('a', 'b', 'c'))

        grafo.conecta('a', 'b')
        self.assertTrue(grafo.peso('a', 'b'), 1)

        grafo.conecta('b', 'c', 3)
        self.assertTrue(grafo.peso('b', 'c'), 3)

        grafo.conecta('b', 'a', 7)
        self.assertTrue(grafo.peso('b', 'a'), 7)
        self.assertTrue(grafo.peso('b', 'c'), 3)
        self.assertTrue(grafo.peso('a', 'b'), 1)

    def test_busca_em_largura_encontrou(self):
        grafo = GrafoDirigido(('a', 'b', 'c', 'd', 'e', 'f'))
        grafo.conecta('a', 'b')
        grafo.conecta('a', 'c')
        grafo.conecta('b', 'c')
        grafo.conecta('c', 'd')
        grafo.conecta('c', 'e')
        grafo.conecta('e', 'f')

        self.assertEqual(grafo.busca_em_largura('a', 'd'), ['a', 'c', 'd'])
        self.assertEqual(grafo.busca_em_largura('a', 'f'), ['a', 'c', 'e', 'f'])

    def test_busca_em_largura_nao_encontrou(self):
        grafo = GrafoDirigido(('a', 'b', 'c', 'd', 'e', 'f'))
        grafo.conecta('a', 'b')
        grafo.conecta('a', 'c')
        grafo.conecta('b', 'c')
        grafo.conecta('c', 'd')
        grafo.conecta('c', 'e')

        self.assertEqual(grafo.busca_em_largura('a', 'f'), None)
        self.assertEqual(grafo.busca_em_largura('c', 'b'), None)

    def test_busca_em_profundidade_encontrou(self):
        grafo = GrafoDirigido(('a', 'b', 'c', 'd', 'e', 'f'))
        grafo.conecta('a', 'b')
        grafo.conecta('a', 'c')
        grafo.conecta('b', 'c')
        grafo.conecta('c', 'd')
        grafo.conecta('c', 'e')
        grafo.conecta('e', 'f')

        self.assertEqual(grafo.busca_em_profundidade('a', 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(grafo.busca_em_profundidade('a', 'f'), ['a', 'b', 'c', 'e', 'f'])

    def test_busca_em_profundidade_nao_encontrou(self):
        grafo = GrafoDirigido(('a', 'b', 'c', 'd', 'e', 'f'))
        grafo.conecta('a', 'b')
        grafo.conecta('a', 'c')
        grafo.conecta('b', 'c')
        grafo.conecta('c', 'd')
        grafo.conecta('c', 'e')

        self.assertEqual(grafo.busca_em_profundidade('a', 'f'), None)
        self.assertEqual(grafo.busca_em_profundidade('c', 'b'), None)

    def test_ordenacao(self):
        grafo = GrafoDirigido(('a', 'b', 'c', 'd', 'e', 'f'))
        grafo.conecta('a', 'b')
        grafo.conecta('a', 'c')
        grafo.conecta('b', 'c')
        grafo.conecta('b', 'f')
        grafo.conecta('c', 'd')
        grafo.conecta('c', 'e')

        self.assertEqual(grafo.ordenacao_topologica(), ['a', 'b', 'f' , 'c', 'e', 'd'])

        grafo.conecta('c', 'f')
        self.assertEqual(grafo.ordenacao_topologica(), ['a', 'b', 'c' , 'f', 'e', 'd'])

    def test_kruskal(self):
        grafo = GrafoNaoDirigido(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'))
        grafo.conecta('a', 'b', 4)
        grafo.conecta('a', 'h', 8)
        grafo.conecta('b', 'h', 11)
        grafo.conecta('b', 'c', 8)
        grafo.conecta('c', 'd', 7)
        grafo.conecta('c', 'i', 2)
        grafo.conecta('c', 'f', 4)
        grafo.conecta('d', 'f', 14)
        grafo.conecta('d', 'e', 9)
        grafo.conecta('e', 'f', 10)
        grafo.conecta('f', 'g', 2)
        grafo.conecta('g', 'i', 6)
        grafo.conecta('g', 'h', 1)
        grafo.conecta('h', 'i', 7)

        self.assertEqual(sorted(grafo.kruskal()), [('a', 'b'), ('a', 'h'), ('c', 'd'), ('c', 'f'), ('c', 'i'), ('d', 'e'), ('f', 'g'), ('g', 'h')])

    def test_prim(self):
        grafo = GrafoNaoDirigido(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'))
        grafo.conecta('a', 'b', 4)
        grafo.conecta('a', 'h', 8)
        grafo.conecta('b', 'h', 11)
        grafo.conecta('b', 'c', 8)
        grafo.conecta('c', 'd', 7)
        grafo.conecta('c', 'i', 2)
        grafo.conecta('c', 'f', 4)
        grafo.conecta('d', 'f', 14)
        grafo.conecta('d', 'e', 9)
        grafo.conecta('e', 'f', 10)
        grafo.conecta('f', 'g', 2)
        grafo.conecta('g', 'i', 6)
        grafo.conecta('g', 'h', 1)
        grafo.conecta('h', 'i', 7)

        self.assertEqual(sorted(grafo.prim('a')), [('a', 'b'), ('b', 'c'), ('c', 'd'), ('c', 'f'), ('c', 'i'), ('d', 'e'), ('f', 'g'), ('g', 'h')])