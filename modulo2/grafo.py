"""
Algoritmos de PCS3110 em Python
Módulo 2 - Grafos
"""
import operator
import heapq
import math
from collections import deque

class GrafoDirigido:
    """ Representa um grafo dirigido seguindo a definição usada em PCS3110
    """
    def __init__(self, nos = None):
        """ Cria um grafo. Opcionalmente pode-se passar uma tupla com os nos.
        """
        self.nos = []
        self.adjacencia = {}

        if nos is not None:
            for no in nos:
                self.adiciona(no)
    
    def adiciona(self, no):
        """Adiciona o no ao grafo.
        """
        self.nos.append(no)
        self.adjacencia[no] = {}
    
    def conecta(self, origem, destino, peso = 1):
        """ Adiciona a aresta (origem, destino) ao grafo.

        Joga ValueError se origem ou destino forem inválidos."""
        if origem not in self.nos:
            raise ValueError('Origem invalida')
        if destino not in self.nos:
            raise ValueError('Destino invalido')

        self.adjacencia[origem][destino] = peso
    
    def desconecta(self, origem, destino):
        """Remove a aresta (origem, destino).

        Joga ValueError se origem ou destino forem inválidos."""
        if origem not in self.nos:
            raise ValueError('Origem invalida')
        if destino not in self.nos:
            raise ValueError('Destino invalido')

        del self.adjacencia[origem][destino]
    
    def possui_aresta(self, origem, destino):
        """Informa se o grafo possui a areseta (origem, destino).

        Joga ValueError se origem ou destino forem inválidos."""
        if origem not in self.nos:
            raise ValueError('Origem invalida')
        if destino not in self.nos:
            raise ValueError('Destino invalido')

        return destino in self.adjacencia[origem]

    def peso(self, origem, destino):
        """Retorna o peso da aresta entre os vértices ou None se não possui
        a aresta.

        Joga ValueError se origem ou destino forem inválidos."""
        if not self.possui_aresta(origem, destino):
            return None

        return self.adjacencia[origem][destino]
    
    def busca_em_largura(self, inicio, procurado):
        """ Retorna o caminho para o vértice procurado a partir do início usando
        uma busca em largura.
        """
        descobertos = {inicio: None}
        para_visitar = deque(inicio)

        while para_visitar:
            atual = para_visitar.popleft()

            for v in sorted(self.adjacencia[atual]): # para seguir ordem crescente de vertices
                if v not in descobertos:
                    if v == procurado:
                        # gerando o caminho
                        caminho = [v]
                        intermediario = atual
                        while not intermediario is None:
                            caminho.append(intermediario)
                            intermediario = descobertos[intermediario]
                        return caminho[::-1]

                    descobertos[v] = atual
                    para_visitar.append(v)
        return None

    def busca_em_profundidade(self, inicio, procurado):
        """ Retorna o caminho para o vértice procurado a partir do início usando
        uma busca em profundidade recursiva.
        """
        descobertos = {inicio: None}
        if self.__busca_em_profundidade_recursiva(inicio, procurado, descobertos):
            # gerando o caminho
            caminho = [procurado]
            intermediario = descobertos[procurado]
            while not intermediario is None:
                caminho.append(intermediario)
                intermediario = descobertos[intermediario]
            return caminho[::-1]
        else:
            return None

    def __busca_em_profundidade_recursiva(self, inicio, procurado, descobertos):
        """ Algoritmo auxiliar para busca em profundidade.
        """
        for v in sorted(self.adjacencia[inicio]): # para seguir ordem crescente de vertices
            if not v in descobertos:
                descobertos[v] = inicio
                if v == procurado:
                    return True
                if self.__busca_em_profundidade_recursiva(v, procurado, descobertos):
                    return True
        return False
    
    def ordenacao_topologica(self):
        """ Retorna uma dos vértices do grafo em ordenação topológica.
        """
        ordem = []
        descobertos = set()
        for v in sorted(self.nos):
            if not v in descobertos:
                self.__ordenar(v, descobertos, ordem)
        return ordem[::-1]
    
    def __ordenar(self, atual, descobertos, ordem):
        """ Algoritmo auxiliar da ordenção topológica.
        """
        descobertos.add(atual)
        for v in sorted(self.adjacencia[atual]):
            if not v in descobertos:
                self.__ordenar(v, descobertos, ordem)
        ordem.append(atual)

    def dijkstra(self, inicial):
        """ Calcula as distâncias mínimas entre o vértice inicial e os demais
        usando o algoritmo de Dijkstra.

        O resultado é um dicionário em que para cada nó tem-se o par (custo, adjacente).
        """
        distancias = {}
        prioridade = []

        for no in self.nos:
            if no == inicial:
                prioridade.append((0, inicial, None))
            else:
                prioridade.append((math.inf, no, None))
        distancias[inicial] = (0, None)

        while prioridade:
            custo, no, adjacente = min(prioridade)
            prioridade.remove((custo, no, adjacente))

            if no != inicial:
                distancias[no] = (custo, adjacente)

            if custo is math.inf:
                # o resto não foi alcançado
                for c, n, a in prioridade:
                    distancias[n] = (math.inf, None)
                return distancias

            novo = []
            for c, n, a in prioridade:
                if n in self.adjacencia[no] and c > self.peso(no, n) + custo:
                    novo.append((self.peso(no, n) + custo, n, no))
                else:
                    novo.append((c, n, a))
            prioridade = novo
        return distancias

class GrafoNaoDirigido(GrafoDirigido):
    """ Representa um grafo não dirigido seguindo a definição usada em PCS3110
    """
    def conecta(self, origem, destino, peso = 1):
        super(GrafoNaoDirigido, self).conecta(origem, destino, peso)
        self.adjacencia[destino][origem] = peso
    
    def desconecta(self, origem, destino):
        super(GrafoNaoDirigido, self).desconecta(origem, destino)
        del self.adjacencia[destino][origem]

    def kruskal(self):
        """ Retorna a árvore geradora mínima usando o algoritmo de Kruskal.
        """
        arvore = []
        
        conjuntos = {}
        arestas = []
        for numero, v in enumerate(sorted(self.nos)):
            conjuntos[v] = numero
            for d in self.adjacencia[v]:
                if v < d:
                    arestas.append((v, d, self.peso(v, d)))
        arestas.sort(key=operator.itemgetter(2)) # ordenando pelo peso

        for o, d, peso in arestas:
            if conjuntos[o] != conjuntos[d]:
                arvore.append((o, d))
                # unir o com d
                agrupar = conjuntos[d]
                for no, conjunto in conjuntos.items():
                    if conjunto == agrupar:
                        conjuntos[no] = conjuntos[o]
        return arvore

    def prim(self, inicial):
        """ Retorna a árvore geradora mínima usando o algoritmo de Prim.
        """
        arvore = []
        prioridade = []

        for no in self.nos:
            if no == inicial:
                prioridade.append((0, inicial, None))
            else:
                prioridade.append((math.inf, no, None))

        while prioridade:
            custo, no, adjacente = min(prioridade)
            prioridade.remove((custo, no, adjacente))

            if custo is math.inf:
                # o resto não foi alcançado
                return arvore

            if no != inicial:
                arvore.append((adjacente, no))
            novo = []
            for c, n, a in prioridade:
                if n in self.adjacencia[no] and c > self.peso(no, n):
                    novo.append((self.peso(no, n), n, no))
                else:
                    novo.append((c, n, a))
            prioridade = novo
        return arvore