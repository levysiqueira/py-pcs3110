"""
Algoritmos de PCS3110 em Python
Módulo 1 - Estruturas de dados
"""
class Elemento:
    """ Elemento de uma lista ligada simples, com uma chave e um ponteiro para o
    proximo elemento."""

    def __init__(self, chave, proximo = None):
        self.chave = chave
        self.proximo = proximo

class ListaLigada:
    """ Implementação de uma lista ligada simples, seguindo a definição do Cormen."""

    def __init__(self):
        self.inicio = None

    def search(self, chave):
        """Retorna o elemento que possui a chave informada ou None caso não
        haja elemento com essa chave"""
        x = self.inicio
        while x is not None and x.chave != chave:
            x = x.proximo
        
        return x
    
    def insert(self, elemento):
        """Insere um elemento na lista ligada
        """
        elemento.proximo = self.inicio
        self.inicio = elemento
    
    def delete(self, elemento):
        """Remove o elemento informado como parâmetro, retirando-o da lista.
        
        Caso o elemento não pertença à lista ligada, joga um ValueError
        """
        if self.inicio == elemento:
            self.inicio = elemento.proximo
        else:
            anterior = self.inicio
            
            while anterior is not None and anterior.proximo != elemento:
                anterior = anterior.proximo

            if anterior is None:
                raise ValueError('Valor inexistente')
            else:
                anterior.proximo = elemento.proximo

    def print(self):
        """Imprime todos os valores, em ordem, na lista ligada
        """
        x = self.inicio
        
        if x == None:
            print('Lista vazia')
        else:
            while x is not None:
                print(x.chave, end = ' ')
                x = x.proximo