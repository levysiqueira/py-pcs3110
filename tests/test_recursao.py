"""
Algoritmos de PCS3110 em Python
Testes / Exemplos
"""
from modulo1.recursao import *
import unittest

class TestRecursao(unittest.TestCase):
    # maior
    def test_ultimo_maior(self):
        entrada = (1, 2, 3)
        self.assertEqual(maior(*entrada), 3)
    
    def test_meio_maior(self):
        entrada = (1, 2, -1)
        self.assertEqual(maior(*entrada), 2)
    
    def test_primeiro_maior(self):
        entrada = (8, 1, 0)
        self.assertEqual(maior(*entrada), 8)

    def test_maior_e_negativo(self):
        entrada = (-1, -2, -3)
        self.assertEqual(maior(*entrada), -1)

    # max
    def test_max_fora_do_limite(self):
        entrada = (1, 2, 3, 4, 5)
        self.assertEqual(max(entrada, 4), 4)

    def test_ultimo_max(self):
        entrada = (1, 2, 3, 4)
        self.assertEqual(max(entrada, 4), 4)
    
    def test_meio_max(self):
        entrada = (3, -2, 5, 3, 4)
        self.assertEqual(max(entrada, 5), 5)
    
    def test_primeiro_max(self):
        entrada = (8, 1, 0, 7, 1)
        self.assertEqual(max(entrada, 5), 8)

    def test_max_e_negativo(self):
        entrada = (-1, -2, -3, -4 , -5)
        self.assertEqual(max(entrada, 5), -1)

    def test_mdc(self):
        self.assertEqual(mdc(8, 6), 2)

        self.assertEqual(mdc(8, 4), 4)

        self.assertEqual(mdc(8, 5), 1)

    def test_mdc_a_menor_que_b(self):
        self.assertEqual(mdc(6, 8), 2)

        self.assertEqual(mdc(2, 16), 2)

        self.assertEqual(mdc(8, 16), 8)

    # fatorial
    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)

        self.assertEqual(fatorial(4), 24)

    def test_fatorial_de_0_e_1(self):
        self.assertEqual(fatorial(0), 1)

        self.assertEqual(fatorial(1), 1)

    # mdc_recursivo
    def test_mdc_recursivo(self):
        self.assertEqual(mdc_recursivo(35, 15), 5)

        self.assertEqual(mdc_recursivo(120, 80), 40)

    def test_mdc_recursivo_a_menor_que_b(self):
        self.assertEqual(mdc_recursivo(15, 35), 5)

        self.assertEqual(mdc_recursivo(80, 120), 40)

if __name__ == '__main__':
    unittest.main()