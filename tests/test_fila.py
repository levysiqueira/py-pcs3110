"""
Algoritmos de PCS3110 em Python
Testes / Exemplos
"""
from modulo1.fila import Fila
import unittest

class TestFila(unittest.TestCase):
    def setUp(self):
        self.fila = Fila()
    
    def test_dequeue_fila_vazia(self):
        self.assertRaises(ValueError, self.fila.dequeue)

    def test_enqueue(self):
        self.fila.enqueue(3)
        self.assertEqual(len(self.fila), 1)
        self.fila.enqueue(2)
        self.assertEqual(len(self.fila), 2)
        self.fila.enqueue(1)
        self.assertEqual(len(self.fila), 3)

    def test_enqueue_valores_iguais(self):
        self.fila.enqueue(1)
        self.assertEqual(len(self.fila), 1)
        self.fila.enqueue(1)
        self.assertEqual(len(self.fila), 2)
        self.fila.enqueue(1)
        self.assertEqual(len(self.fila), 3)

    def test_enqueue_e_dequeue(self):
        self.fila = Fila(4)
        self.fila.enqueue(1)
        self.assertEqual(self.fila.dequeue(), 1)

        self.fila.enqueue(2)
        self.fila.enqueue(3)
        self.assertEqual(self.fila.dequeue(), 2)

        self.fila.enqueue(4)
        self.fila.enqueue(5)
        self.fila.enqueue(6)
        self.assertEqual(self.fila.dequeue(), 3)
        self.assertEqual(self.fila.dequeue(), 4)
        self.assertEqual(self.fila.dequeue(), 5)
        self.assertEqual(self.fila.dequeue(), 6)
    
    def test_enqueue_overflow(self):
        self.fila = Fila(2)
        self.fila.enqueue(3)
        self.fila.enqueue(2)
        self.assertRaises(ValueError, self.fila.enqueue, 1)

    def test_dequeue_ate_acabar(self):
        self.fila.enqueue(1)
        self.fila.enqueue(2)
        self.assertEqual(self.fila.dequeue(), 1)
        self.assertEqual(self.fila.dequeue(), 2)
        self.assertRaises(ValueError, self.fila.dequeue)
    
    def test_is_empty(self):
        self.fila = Fila(2)
        self.assertTrue(self.fila.is_empty())

        self.fila.enqueue(1)
        self.assertFalse(self.fila.is_empty())

        self.fila.enqueue(2)
        self.assertFalse(self.fila.is_empty())

        self.fila.dequeue()
        self.assertFalse(self.fila.is_empty())
        
        self.fila.enqueue(3)

        self.fila.dequeue()
        self.assertFalse(self.fila.is_empty())

        self.fila.dequeue()
        self.assertTrue(self.fila.is_empty())

    def test_len(self):
        self.fila = Fila(2)

        self.fila.enqueue(1)
        self.assertEqual(len(self.fila), 1)

        self.fila.enqueue(2)
        self.assertEqual(len(self.fila), 2)

        self.fila.dequeue()
        self.assertEqual(len(self.fila), 1)

        self.fila.enqueue(2)
        self.assertEqual(len(self.fila), 2)

        self.fila.dequeue()
        self.assertEqual(len(self.fila), 1)