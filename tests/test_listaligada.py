"""
Algoritmos de PCS3110 em Python
Testes / Exemplos
"""
from modulo1.listaligada import ListaLigada
from modulo1.listaligada import Elemento
import unittest

class TestListaLigada(unittest.TestCase):

    def setUp(self):
        self.lista = ListaLigada()

    def test_lista_vazia(self):
        self.assertEqual(self.lista.inicio, None)

    def test_insert_vazia(self):
        adicionado = Elemento(5)
        self.lista.insert(adicionado)

        self.assertEqual(self.lista.inicio, adicionado)

    def test_insert_varios_elementos(self):
        adicionado1 = Elemento(1)
        self.lista.insert(adicionado1)
        self.assertEqual(self.lista.search(1), adicionado1)

        adicionado2 = Elemento(2)
        self.lista.insert(adicionado2)
        self.assertEqual(self.lista.search(1), adicionado1)
        self.assertEqual(self.lista.search(2), adicionado2)

        adicionado3 = Elemento(3)
        self.lista.insert(adicionado3)
        self.assertEqual(self.lista.search(1), adicionado1)
        self.assertEqual(self.lista.search(2), adicionado2)
        self.assertEqual(self.lista.search(3), adicionado3)

        adicionado4 = Elemento(4)
        self.lista.insert(adicionado4)
        self.assertEqual(self.lista.search(1), adicionado1)
        self.assertEqual(self.lista.search(2), adicionado2)
        self.assertEqual(self.lista.search(3), adicionado3)
        self.assertEqual(self.lista.search(4), adicionado4)
    
    def test_delete_vazia(self):
        self.assertRaises(ValueError, self.lista.delete, (Elemento(5)))

    def test_delete_no_inicio(self):
        elementos = [Elemento(5), Elemento(4), Elemento(3), Elemento(2), Elemento(1)]
        for e in elementos:
            self.lista.insert(e)
        
        self.lista.delete(self.lista.search(elementos[0].chave))
        for e in elementos[1:]:
            self.assertEqual(self.lista.search(e.chave), e)
        self.assertIsNone(self.lista.search(elementos[0].chave))

        self.lista.delete(self.lista.search(elementos[1].chave))
        for e in elementos[2:]:
            self.assertEqual(self.lista.search(e.chave), e)
        self.assertIsNone(self.lista.search(elementos[1].chave))

    def test_delete_no_fim(self):
        elementos = [Elemento(5), Elemento(4), Elemento(3), Elemento(2), Elemento(1)]
        for e in elementos[::-1]:
            self.lista.insert(e)
        
        self.lista.delete(self.lista.search(elementos[0].chave))
        for e in elementos[1:]:
            self.assertEqual(self.lista.search(e.chave), e)
        self.assertIsNone(self.lista.search(elementos[0].chave))

        self.lista.delete(self.lista.search(elementos[1].chave))
        for e in elementos[2:]:
            self.assertEqual(self.lista.search(e.chave), e)
        self.assertIsNone(self.lista.search(elementos[1].chave))

    def test_delete_no_meio(self):
        elementos = [Elemento(5), Elemento(4), Elemento(3), Elemento(2), Elemento(1)]
        for e in elementos:
            self.lista.insert(e)
        
        self.lista.delete(self.lista.search(elementos[2].chave))
        for e in [x for x in elementos if x != elementos[2]]:
            self.assertEqual(self.lista.search(e.chave), e)
        self.assertIsNone(self.lista.search(elementos[2].chave))

        self.lista.delete(self.lista.search(elementos[1].chave))
        for e in [x for x in elementos if x != elementos[2] and x != elementos[1]]:
            self.assertEqual(self.lista.search(e.chave), e)
        self.assertIsNone(self.lista.search(elementos[1].chave))
        self.assertIsNone(self.lista.search(elementos[2].chave))

if __name__ == "__main__":
    unittest.main()