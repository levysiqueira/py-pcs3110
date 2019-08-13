from modulo3.maxheap import MaxHeap
import unittest

class TestHeap(unittest.TestCase):
    def test_is_max_heap_ordenado(self):
        h1 = MaxHeap()
        h1.lista = [9, 8, 7, 6 , 5, 4, 3, 2, 1]
        h1.heap_size = len(h1.lista)
        self.assertTrue(h1.is_max_heap())

    def test_is_max_heap_nao_ordenado(self):
        h1 = MaxHeap()
        h1.lista = [9, 8, 3, 7 , 4, 1, 2, 5, 6]
        h1.heap_size = len(h1.lista)
        self.assertTrue(h1.is_max_heap())

    def test_is_max_heap_iguais(self):
        h1 = MaxHeap()
        h1.lista = [9, 9, 9, 9 , 9, 1, 2, 5, 6]
        h1.heap_size = len(h1.lista)
        self.assertTrue(h1.is_max_heap())
    
    def test_is_max_heap_não_é(self):
        h1 = MaxHeap()
        h1.lista = [1, 2, 3, 4 , 5, 6, 7, 8, 9]
        h1.heap_size = len(h1.lista)
        self.assertFalse(h1.is_max_heap())

        h1.lista = [9, 8, 3, 7, 4, 1, 5, 2, 6]
        h1.heap_size = len(h1.lista)
        self.assertFalse(h1.is_max_heap())
    
    def test_build_crescente(self):
        h1 = MaxHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertTrue(h1.is_max_heap())

    def test_build_aleatorio(self):
        h1 = MaxHeap([5, 2, 3, 7, 9, 4, 8, 1, 6])
        self.assertTrue(h1.is_max_heap())

    def test_build_decrescente(self):
        h1 = MaxHeap([9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertTrue(h1.is_max_heap())

    def test_build_já_é_heap(self):
        h1 = MaxHeap([9, 8, 3, 7 , 4, 1, 2, 5, 6])
        self.assertTrue(h1.is_max_heap())
    
    def test_extrair_maior(self):
        h1 = MaxHeap([5, 2, 3, 7, 9, 4, 8, 1, 6])

        self.assertEqual(h1.extrair_maior(), 9)
        self.assertEqual(h1.extrair_maior(), 8)
        self.assertEqual(h1.extrair_maior(), 7)
        self.assertEqual(h1.extrair_maior(), 6)
        self.assertEqual(h1.extrair_maior(), 5)
        self.assertEqual(h1.extrair_maior(), 4)
        self.assertEqual(h1.extrair_maior(), 3)
        self.assertEqual(h1.extrair_maior(), 2)
        self.assertEqual(h1.extrair_maior(), 1)
        self.assertRaises(ValueError, h1.extrair_maior)
    
    def test_extrair_maior_underflow(self):
        h = MaxHeap()
        self.assertRaises(ValueError, h.extrair_maior)
    
    def test_inserir_em_ordem(self):
        h = MaxHeap()
        h.inserir(1)
        self.assertTrue(h.is_max_heap())
        h.inserir(2)
        self.assertTrue(h.is_max_heap())
        h.inserir(3)
        self.assertTrue(h.is_max_heap())
        h.inserir(4)
        self.assertTrue(h.is_max_heap())
        h.inserir(5)
        self.assertTrue(h.is_max_heap())
        h.inserir(6)
        self.assertTrue(h.is_max_heap())
        h.inserir(7)
        self.assertTrue(h.is_max_heap())
        h.inserir(8)
        self.assertTrue(h.is_max_heap())

    def test_inserir_já_em_max_heap(self):
        h = MaxHeap()
        h.inserir(9)
        self.assertTrue(h.is_max_heap())
        h.inserir(8)
        self.assertTrue(h.is_max_heap())
        h.inserir(3)
        self.assertTrue(h.is_max_heap())
        h.inserir(7)
        self.assertTrue(h.is_max_heap())
        h.inserir(4)
        self.assertTrue(h.is_max_heap())
        h.inserir(1)
        self.assertTrue(h.is_max_heap())
        h.inserir(2)
        self.assertTrue(h.is_max_heap())
        h.inserir(5)
        self.assertTrue(h.is_max_heap())
        h.inserir(6)
        self.assertTrue(h.is_max_heap())