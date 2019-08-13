"""
Algoritmos de PCS3110 em Python
Módulo 1 - Estruturas de dados
"""
class Elemento:
    """ Elemento de uma lista duplamente ligada, com uma chave, um ponteiro
    para o proximo elemento e um ponteiro para o anterior"""

    def __init__(self, chave, proximo = None):
        self.chave = chave
        self.proximo = proximo
        self.anterior = proximo

class ListaDuplamenteLigada:
    """ Implementação de uma lista duplamente ligada, seguindo a definição do
    Cormen.
    """

    def __init__(self):
        self.inicio = None

    def search(self, chave):
        """Retorna o elemento que possui a chave informada ou None caso não
        haja elemento com essa chave
        """
        x = self.inicio
        while x is not None and x.chave != chave:
            x = x.proximo
        
        return x
    
    def insert(self, elemento):
        """Insere um elemento na lista duplamente ligada
        """
        elemento.proximo = self.inicio
        if self.inicio != None:
            self.inicio.anterior = elemento
        self.inicio = elemento
        elemento.anterior = None # Construtor já faz isso
    
    def delete(self, elemento):
        """Remove o elemento informado como parâmetro, retirando-o da lista
        """
        if elemento.anterior != None:
            elemento.anterior.proximo = elemento.proximo
        else:
            self.inicio = elemento.proximo
        if elemento.proximo != None:
            elemento.proximo.anterior = elemento.anterior

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