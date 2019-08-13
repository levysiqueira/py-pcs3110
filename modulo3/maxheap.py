class MaxHeap:
    """ Implementação de um max-heap.
    """
    def __init__(self, lista = None):
        if lista == None:
            self.lista = []
        else:
            self.lista = lista

        self.heap_size = len(self.lista)

        for i in range(MaxHeap.pai(self.heap_size - 1), -1, -1):
            self.max_heapify(i)
    
    def __str__(self):
        return str(self.lista[:self.heap_size])
    
    @staticmethod
    def pai(i):
        """ Retorna a posição do pai de i.
        """
        return int((i - 1) / 2)
    
    @staticmethod
    def filho_esquerda(i):
        """ Retorna a posição do filho da esquerda de i.
        """
        return 2 * i + 1

    @staticmethod
    def filho_direita(i):
        """ Retorna a posição do filho da direita de i.
        """
        return 2 * i + 2
    
    def is_max_heap(self):
        """ Retorna True se o Heap é um max-heap. ou False caso contrário.
        """
        for i in range(self.heap_size - 1, 0, -1):
            if self.lista[i] > self.lista[MaxHeap.pai(i)]:
                return False
        return True

    def max_heapify(self, i):
        """ Algoritmo que corrige a posição i de um max-heap.
        """
        e = MaxHeap.filho_esquerda(i)
        d = MaxHeap.filho_direita(i)
        if e < self.heap_size and self.lista[e] > self.lista[i]:
            maior = e
        else:
            maior = i
        
        if d < self.heap_size and self.lista[d] > self.lista[maior]:
            maior = d

        if maior != i:
            temp = self.lista[i]
            self.lista[i] = self.lista[maior]
            self.lista[maior] = temp
            self.max_heapify(maior)
    
    def extrair_maior(self):
        """ Extrai o maior elemento de um max-heap.

        Joga um ValueError em caso de underflow.
        """
        if self.heap_size < 1:
            raise ValueError('underflow')
        maior = self.lista[0]
        self.lista[0] = self.lista[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return maior
    
    def inserir(self, chave):
        """ Insere o valor da chave no max-heap.
        """
        self.heap_size += 1
        if len(self.lista) < self.heap_size:
            self.lista.append(chave)
        else:
            self.lista[self.heap_size - 1] = chave

        i = self.heap_size - 1
        while i > 0 and self.lista[MaxHeap.pai(i)] < chave:
            self.lista[i] = self.lista[MaxHeap.pai(i)]
            self.lista[MaxHeap.pai(i)] = chave
            i = MaxHeap.pai(i)