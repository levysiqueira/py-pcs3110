"""
Algoritmos de PCS3110 em Python
Módulo 3 - Análise de algoritmo e ordenação
"""
import math
from modulo3.maxheap import MaxHeap

def insertion_sort(lista):
    """ Retorna a lista ordenada usando o algoritmo InsertionSort.
    """
    for j in range(len(lista))[1:]:
        chave = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = chave
    return lista

def selection_sort(lista):
    """ Retorna a lista ordenada usando o algoritmo SelectionSort.
    """
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        temp = lista[menor]
        lista[menor] = lista[i]
        lista[i] = temp
    return lista

def mergesort(lista):
    """ Retorna a lista ordenada usando o algoritmo MergeSort.
    """
    __mergesort(lista, 0, len(lista) - 1)

    return lista

def __mergesort(lista, inicio, fim):
    if inicio < fim:
        meio = int((inicio + fim) / 2)
        __mergesort(lista, inicio, meio)
        __mergesort(lista, meio + 1, fim)
        __merge(lista, inicio, meio, fim)

def __merge(lista, inicio, meio, fim):
    """ Algoritmo de intercalação usando sentinelas.
    """
    n1 = meio - inicio + 1
    n2 = fim - meio
    e = []
    d = []
    for i in range(n1):
        e.append(lista[inicio + i])
    for i in range(n2):
        d.append(lista[meio + 1 + i])
    e.append(math.inf)
    d.append(math.inf)

    i = 0
    j = 0
    for k in range(inicio, fim + 1):
        if e[i] <= d[j]:
            lista[k] = e[i]
            i += 1
        else:
            lista[k] = d[j]
            j += 1

def quicksort(lista):
    """ Retorna a lista ordenada usando o algoritmo QuickSort.
    """
    __quicksort(lista, 0, len(lista) - 1)
    return lista

def __quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = __partition(lista, inicio, fim)
        __quicksort(lista, inicio, pivo - 1)
        __quicksort(lista, pivo + 1, fim)

def __partition(lista, inicio, fim):
    """ Particiona a lista de início a fim usando como pivô o último elemento.
    """
    pivo = lista[fim]
    menor = inicio - 1
    for pos in range(inicio, fim):
        if lista[pos] <= pivo:
            menor += 1
            temp = lista[menor]
            lista[menor] = lista[pos]
            lista[pos] = temp
    lista[fim] = lista[menor + 1]
    lista[menor + 1] = pivo
    return menor + 1

def heapsort(lista):
    """ Retorna a lista ordenada usando o algoritmo HeapSort.
    """
    h = MaxHeap(lista)
    for i in range(len(lista) - 1, 0, -1):
        temp = lista[0]
        lista[0] = lista[i]
        lista[i] = temp
        h.heap_size -= 1
        h.max_heapify(0)
    return lista
