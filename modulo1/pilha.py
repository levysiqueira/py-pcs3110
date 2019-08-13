"""
Algoritmos de PCS3110 em Python
Módulo 1 - Estruturas de dados
"""
class Pilha:
    '''Uma pilha implementada com uma lista, com as operações push e pop.'''
    def __init__(self):
        self.topo = -1
        self.elementos = []

    def __len__(self):
        return self.topo + 1

    def pop(self):
        '''Retira o elemento no topo da pilha e o retorna.

        Caso a pilha esteja vazia, joga um ValueError'''
        if self.topo == -1:
            raise ValueError('Underflow')
        #return self.elementos.pop(self.topo)
        retorno = self.elementos[self.topo]
        del self.elementos[self.topo]
        self.topo -= 1
        return retorno

    def push(self, valor):
        '''Adiciona o valor ao topo da pilha.'''
        self.topo += 1
        self.elementos.append(valor)

    def is_empty(self):
        '''Retorna True caso a pilha esteja vazia ou False
        caso contrário.'''
        return len(self.elementos) == 0