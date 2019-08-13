from modulo1.pilha import Pilha
import unittest

class TestPilha(unittest.TestCase):
    def setUp(self):
        self.pilha = Pilha()

    def test_pop_vazia(self):
        self.assertRaises(ValueError, self.pilha.pop)
    
    def test_len(self):
        self.assertEqual(len(self.pilha), 0)

        self.pilha.push(4)
        self.assertEqual(len(self.pilha), 1)

        self.pilha.push(4)
        self.pilha.push(4)
        self.assertEqual(len(self.pilha), 3)


    def test_pop(self):
        self.pilha.push(4)
        self.pilha.push(3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 4)

        self.assertRaises(ValueError, self.pilha.pop)