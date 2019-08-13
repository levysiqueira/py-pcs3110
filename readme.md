# Algoritmos de PCS3110 em Python

## Escola Politécnica da USP - [PCS3110 - Algoritmos e Estruturas de Dados para a Engenharia Elétrica](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=pcs3110)

Os seguintes algoritmos usados em PCS3110 foram implementados em Python:

- Módulo 1 - Estruturas de dados
    - Recursão
    - Lista ligada simples
    - Lista duplamente ligada
    - Pilha
    - Fila
    - Tabela Hash
- Módulo 2 - Grafos
    - Grafo dirigo e não dirigido
    - Busca em largura
    - Busca em profundidade
    - Ordenação topológica
    - Árvore geradora mínima usando os algoritmos de Prim e Kruskal
    - Caminhos mínimos usando o algoritmo de Dijkstra
    - Árvore binária (altura, é ancestral, pré-ordem, pós-ordem e em ordem)
    - ABB (adicionar, busca, menor, maior e sucessor)
- Módulo 3 - Análise de algoritmo e ordenação
    - max-heap (é max-heap, max heapify, extrair maior e inserir)
    - InsertionSort
    - SelectionSort
    - MergeSort
    - QuickSort
    - HeapSort

Além das implementações são disponibilizados alguns testes simples usando a biblioteca `unittest` do Python. Note que não são testes de unidade *ideais*; devem ser vistos apenas como exemplos de uso das classes.

Para rodar todos os testes:

    python -m unittest -v

Para rodar um teste específico (por exemplo, os de recursão):

    python -m unittest tests/test_recursao.py -v

Caso haja algum problema de implementação, abra uma Issue no GitHub ou faça um Pull request. Qualquer coisa entre em [contato comigo](maito:fabio@levysiqueira.com.br).

[![Licença](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)