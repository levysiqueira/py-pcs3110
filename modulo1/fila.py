"""
Algoritmos de PCS3110 em Python
Módulo 1 - Estruturas de dados
"""
class Fila:
    """Uma fila implementada com uma lista, com as operações
    enqueue e dequeue.
    """

    def __init__(self, tamanho = 10):
        """Cria uma fila com a capacidade definida
        """
        self.tamanho = tamanho + 1
        self.inicio = 0
        self.fim = 0
        self.fila = [None] * (tamanho + 1)
    
    def __len__(self):
        if self.inicio <= self.fim:
            return self.fim - self.inicio
        else:
            return self.tamanho - self.inicio + self.fim
    
    def enqueue(self, valor):
        """ Adiciona o valor no final da fila.

        Joga um ValueError caso não haja mais espaço na fila.
        """
        if self.inicio == (self.fim + 1) % self.tamanho:
            raise ValueError('Overflow')
        self.fila[self.fim] = valor
        self.fim = (self.fim + 1) % self.tamanho
    
    def dequeue(self):
        """ Retira e retorna o valor no início da fila.

        Joga um ValueError caso não haja valores na fila.
        """
        if self.is_empty():
            raise ValueError('Underflow')
        retorno = self.fila[self.inicio]
        self.fila[self.inicio] = None # para o garbage collector
        self.inicio = (self.inicio + 1) % self.tamanho
        return retorno

    def is_empty(self):
        return self.inicio == self.fim