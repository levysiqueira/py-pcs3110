# Algoritmos de PCS3110 em Python

## [PCS3110 - Algoritmos e Estruturas de Dados para a Engenharia Elétrica](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=pcs3110)

## Escola Politécnica da USP

Os seguintes algoritmos usados em PCS3110 foram implementados em Python:

- Módulo 1 - Estruturas de dados
    - [Recursão](modulo1/recursao.py)
    - [Lista ligada simples](modulo1/listaligada.py)
    - [Lista duplamente ligada](modulo1/listaduplamenteligada.py)
    - [Pilha](modulo1/pilha.py)
    - [Fila](modulo1/fila.py)
    - [Tabela Hash](modulo1/hash.py)
- Módulo 2 - Grafos
    - [Grafo dirigo e não dirigido](modulo2/grafo.py)
    - [Busca em largura](modulo2/grafo.py)
    - [Busca em profundidade](modulo2/grafo.py)
    - [Ordenação topológica](modulo2/grafo.py)
    - [Árvore geradora mínima usando os algoritmos de Prim e Kruskal](modulo2/grafo.py)
    - [Caminhos mínimos usando o algoritmo de Dijkstra](modulo2/grafo.py)
    - [Árvore binária (altura, é ancestral, pré-ordem, pós-ordem e em ordem)](modulo2/arvore.py)
    - [ABB (adicionar, busca, menor, maior e sucessor)](modulo2/arvore.py)
- Módulo 3 - Análise de algoritmo e ordenação
    - [Max-heap (é max-heap, max heapify, extrair maior e inserir)](modulo3/maxheap.py)
    - [InsertionSort](modulo3/ordenacao.py)
    - [SelectionSort](modulo3/ordenacao.py)
    - [MergeSort](modulo3/ordenacao.py)
    - [QuickSort](modulo3/ordenacao.py)
    - [HeapSort](modulo3/ordenacao.py)

Além das implementações são disponibilizados [alguns testes simples](https://github.com/levysiqueira/py-pcs3110/tree/master/tests) usando a biblioteca `unittest` do Python. Note que não são testes de unidade *ideais*; devem ser vistos apenas como exemplos de uso das classes.

Para rodar todos os testes:

    python -m unittest -v

Para rodar um teste específico (por exemplo, os de recursão):

    python -m unittest tests/test_recursao.py -v

Caso haja algum problema de implementação, abra uma Issue no GitHub ou faça um Pull request. Qualquer coisa entre em [contato comigo](maito:fabio@levysiqueira.com.br).

[![Licença](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
