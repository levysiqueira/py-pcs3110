"""
Algoritmos de PCS3110 em Python
Testes / Exemplos
"""
from modulo3.ordenacao import *
import unittest

class TestOrdenacao(unittest.TestCase):
    def setUp(self):
        self.ordenado = [1, 2, 3, 4, 5, 6, 7]
        self.a = [7, 6, 5, 4, 3, 2, 1]
        self.b = [1, 3, 2, 5, 4, 7, 6]
        self.c = [6, 3, 1, 7, 4, 5, 2]
        
        self.igual = [1, 1, 1, 1, 1, 1, 1]
        self.negativo = [-2, -3, -1, -6, -7, -5, -4]
        self.gabarito_negativo = [-7, -6, -5, -4, -3, -2, -1]

    def test_insertion(self):
        self.assertEqual(insertion_sort(self.ordenado.copy()), self.ordenado)
        self.assertEqual(insertion_sort(self.a), self.ordenado)
        self.assertEqual(insertion_sort(self.b), self.ordenado)
        self.assertEqual(insertion_sort(self.c), self.ordenado)
    
    def test_insertion_iguais(self):
        self.assertEqual(insertion_sort(self.igual.copy()), self.igual)
    
    def test_insertion_negativos(self):
        self.assertEqual(insertion_sort(self.negativo), self.gabarito_negativo)

    def test_selection(self):
        self.assertEqual(selection_sort(self.ordenado.copy()), self.ordenado)
        self.assertEqual(selection_sort(self.a), self.ordenado)
        self.assertEqual(selection_sort(self.b), self.ordenado)
        self.assertEqual(selection_sort(self.c), self.ordenado)
    
    def test_selection_iguais(self):
        self.assertEqual(selection_sort(self.igual.copy()), self.igual)
    
    def test_selection_negativos(self):
        self.assertEqual(selection_sort(self.negativo), self.gabarito_negativo)

    def test_mergesort(self):
        self.assertEqual(mergesort(self.ordenado.copy()), self.ordenado)
        self.assertEqual(mergesort(self.a), self.ordenado)
        self.assertEqual(mergesort(self.b), self.ordenado)
        self.assertEqual(mergesort(self.c), self.ordenado)
    
    def test_mergesort_iguais(self):
        self.assertEqual(mergesort(self.igual.copy()), self.igual)
    
    def test_mergesort_negativos(self):
        self.assertEqual(mergesort(self.negativo), self.gabarito_negativo)

    def test_quicksort(self):
        self.assertEqual(quicksort(self.ordenado.copy()), self.ordenado)
        self.assertEqual(quicksort(self.a), self.ordenado)
        self.assertEqual(quicksort(self.b), self.ordenado)
        self.assertEqual(quicksort(self.c), self.ordenado)
    
    def test_quicksort_iguais(self):
        self.assertEqual(quicksort(self.igual.copy()), self.igual)
    
    def test_quicksort_negativos(self):
        self.assertEqual(quicksort(self.negativo), self.gabarito_negativo)

    def test_heapsort(self):
        self.assertEqual(heapsort(self.ordenado.copy()), self.ordenado)
        self.assertEqual(heapsort(self.a), self.ordenado)
        self.assertEqual(heapsort(self.b), self.ordenado)
        self.assertEqual(heapsort(self.c), self.ordenado)
    
    def test_heapsort_iguais(self):
        self.assertEqual(heapsort(self.igual.copy()), self.igual)
    
    def test_heapsort_negativos(self):
        self.assertEqual(heapsort(self.negativo), self.gabarito_negativo)