"""
Algoritmos de PCS3110 em Python
Módulo 1 - Estruturas de dados básicas
"""
def maior(a, b, c):
    """ Retorna o valor maior entre a, b e c.
    """
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

def max(lista, n):
    """ Retorna o maior valor entre os n primeiros elementos da lista.
    """
    maior = lista[0]
    for e in lista[1:n]:
        if e > maior:
            maior = e
    return maior

def mdc(a, b):
    """ Retorna o MDC entre a e b.
    """
    if a < b:
        temp = a
        a = b
        b = temp
    
    while b != 0:
        r = a % b
        a = b
        b = r

    return a

def fatorial(n):
    """ Retorna o fatorial de n.
    """
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

def mdc_recursivo(a, b):
    """ Retorna o MDC entre a e b.
    """
    if b == 0:
        return a
    r = a % b
    return mdc_recursivo(b, r)

def hanoi(n, origem, auxiliar, destino):
    """ Apresenta as instruções para resolver o problema da torre de Hanói
    usando as torres origem, auxiliar e destino para n discos.
    """
    if n == 1:
        print('Mover disco %d de %s para %s' % (n, origem, destino))
    elif n > 1:
        hanoi (n - 1, origem, destino, auxiliar)
        print('Mover disco %d de %s para %s' % (n, origem, destino))
        hanoi (n - 1, auxiliar, origem, destino)

if __name__ == '__main__':
    hanoi(5, 'A', 'B', 'C')