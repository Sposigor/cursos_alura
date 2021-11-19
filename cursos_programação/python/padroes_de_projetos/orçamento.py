''' Orçamentos '''

class Orcamento(object):
    ''' Classe que representa um orçamento '''
    def __init__ (self, valor):
        ''' Inicializa '''
        self.__itens = []
    @property
    def valor(self):
        ''' Retorna o valor do orçamento '''
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total
    def obter_itens(self):
        ''' Retorna os itens do orçamento '''
        return tuple(self.__itens)
    @property
    def total_itens(self):
        ''' Retorna o total de itens do orçamento '''
        return len(self.__itens)
    def adiciona_item(self, item):
        self.__itens.append(item)

class Item(object):
    ''' Classe que representa um item de um orçamento '''
    def __init__(self, nome, valor):
        ''' Inicializa '''
        self.__nome = nome
        self.__valor = valor
    @property
    def valor(self):
        ''' Retorna o valor do item '''
        return self.__valor
    @property
    def nome(self):
        ''' Retorna o nome do item '''
        return self.__nome
