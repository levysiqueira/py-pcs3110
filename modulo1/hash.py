class TabelaHash:
    """ Implementação de uma tabela Hash usando o método da divisão e endereçamento aberto 
    com sondagem linear para resolver colisões.
    """
    def __init__(self, tamanho = 10):
        self.lista = [None] * tamanho

    def insere(self, elemento):
        """ Insere o elemento na tabela Hash.
        """
        pos = elemento.chave % len(self.lista)
        deu_volta = False

        while not deu_volta:
            if self.lista[pos] is None or \
              self.lista[pos] is TabelaHash.VAZIO: #
                self.lista[pos] = elemento
                return
            pos = (pos + 1) % len(self.lista)
            deu_volta = pos == elemento.chave % len(self.lista)
        
        raise RuntimeError('Sem espaço disponível')
    
    def busca(self, chave):
        """ Busca o elemento com a chave na tabela Hash e o retorna.
        """
        pos = chave % len(self.lista)
        deu_volta = False

        while not deu_volta:
            if self.lista[pos] is None:
                return None
            elif self.lista[pos] is TabelaHash.VAZIO: #
                pass
            elif self.lista[pos].chave == chave:
                return self.lista[pos]

            pos = (pos + 1) % len(self.lista)
            deu_volta = pos == chave % len(self.lista)
        return None
    
    class Vazio:
        """ Marcador de elemento removido.
        """
        pass
    VAZIO = Vazio()

    def remove(self, elemento):
        """ Remove um elemento na tabela Hash (usando o Vazio como marcador.)
        """
        pos = elemento.chave % len(self.lista)
        deu_volta = False

        while not deu_volta:
            if self.lista[pos] is None:
                raise ValueError('Elemento inexistente')
            elif self.lista[pos] is elemento:
                self.lista[pos] = TabelaHash.VAZIO
                return

            pos = (pos + 1) % len(self.lista)
            deu_volta = pos == elemento.chave % len(self.lista)
        
        raise ValueError('Elemento inexistente')

class Elemento:
    """ Classe simples que possui o atributo chave.
    """
    def __init__(self, chave):
        self.chave = chave
