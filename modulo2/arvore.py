"""
Algoritmos de PCS3110 em Python
Módulo 2 - Grafos
"""
from collections import deque
class No:
    """ Nó de uma árvore binária (e ABB).
    """
    def __init__(self, chave, pai = None, filho_esquerda = None, filho_direita = None):
        self.chave = chave
        self.pai = pai
        self.filho_esquerda = filho_esquerda
        self.filho_direita = filho_direita
    
class Arvore:
    def __init__(self, raiz = None):
        self.raiz = raiz

    def __str__(self):
        nivel_atual = deque()
        nivel = 0
        nivel_atual.append(self.raiz)
        proximos = deque()
        valor = ''

        while nivel_atual:
            atual = nivel_atual.popleft()
            if atual is not None:
                valor += ('\t' * nivel) + str(atual.chave) + '\n'
                proximos.append(atual.filho_esquerda)
                proximos.append(atual.filho_direita)
            else:
                valor += ('\t' * nivel) + '-\n'

            if not nivel_atual:
                nivel += 1
                nivel_atual = proximos
                proximos = deque()
        return valor

    def é_ancestral(self, no, ancestral):
        """ Retorna True se ancestral é ancestral de nó e False caso contrário.
        """
        acima = no.pai
        while acima is not None:
            if acima == ancestral:
                return True
            acima = acima.pai
        return False

    def altura_total(self):
        """ Retorna a altura total da árvore binária.
        """
        return self.altura(self.raiz)

    def altura(self, no):
        """ Retorna a altura da árvore ao considerar o nó como raiz.
        """
        if no is None:
            return -1
        altura_esquerda = self.altura(no.filho_esquerda)
        altura_direita = self. altura(no.filho_direita)
        if altura_esquerda > altura_direita:
            return altura_esquerda + 1
        else:
            return altura_direita + 1

    def pre_ordem(self):
        """ Retorna uma lista com nós em pré-ordem.
        """
        return self.__pre_ordem_aux(self.raiz, [])
    
    def __pre_ordem_aux(self, no, retorno):
        if no is not None:
            retorno.append(no.chave)
            self.__pre_ordem_aux(no.filho_esquerda, retorno)
            self.__pre_ordem_aux(no.filho_direita, retorno)
        return retorno

    def pos_ordem(self):
        """ Retorna uma lista com nós em pós-ordem.
        """
        return self.__pos_ordem_aux(self.raiz, [])
    
    def __pos_ordem_aux(self, no, retorno):
        if no is not None:
            self.__pos_ordem_aux(no.filho_esquerda, retorno)
            self.__pos_ordem_aux(no.filho_direita, retorno)
            retorno.append(no.chave)
        return retorno

    def em_ordem(self):
        """ Retorna uma lista com nós em ordem.
        """
        return self.__em_ordem_aux(self.raiz, [])
    
    def __em_ordem_aux(self, no, retorno):
        if no is not None:
            self.__em_ordem_aux(no.filho_esquerda, retorno)
            retorno.append(no.chave)
            self.__em_ordem_aux(no.filho_direita, retorno)
        return retorno

class ABB(Arvore):
    """ Árvore binária de Busca com alguns algoritmos básicos.
    """
    def __init__(self, raiz = None):
        self.raiz = raiz
    
    def adicionar(self, valor):
        """ Adiciona um valor à árvore mantendo a propriedade de ABB.
        """
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            pai = None
            atual = self.raiz
            while atual is not None:
                pai = atual
                if valor > atual.chave:
                    atual = atual.filho_direita
                else:
                    atual = atual.filho_esquerda

            if valor > pai.chave:
                pai.filho_direita = No(valor, pai)
            else:
                pai.filho_esquerda = No(valor, pai)

    def busca(self, valor):
        """ Retorna o nó cuja chave possui o valor ou None caso não
        haja nó com a chave na árvore.
        """
        return self.__busca(self.raiz, valor)
    
    def __busca(self, no, valor):
        if no is None or no.chave == valor:
            return no
        
        if valor > no.chave:
            return self.__busca(no.filho_direita, valor)
        else:
            return self.__busca(no.filho_esquerda, valor)

    def menor(self, no = None):
        """ Retorna o menor nó da subárvore com no como raiz.

        Caso não seja passado o nó, usa-se a raiz.
        """
        if no is None:
            no = self.raiz

        if self.raiz is None:
            return None
        
        while no.filho_esquerda is not None:
            no = no.filho_esquerda
        return no

    def maior(self, no = None):
        """ Retorna o maior nó da subárvore com no como raiz.

        Caso não seja passado o nó, usa-se a raiz.
        """
        if no is None:
            no = self.raiz

        if self.raiz is None:
            return None
        
        while no.filho_direita is not None:
            no = no.filho_direita
        return no

    def sucessor(self, no):
        """ Retorna o nó sucessor ao nó passado.
        """
        if no.filho_direita is not None:
            return self.menor(no.filho_direita)
        raiz = no.pai
        while raiz is not None and no == raiz.filho_direita:
            no = raiz
            raiz = raiz.pai
        return raiz