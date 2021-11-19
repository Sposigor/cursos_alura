

class CalculadorDescontos(object):
    ''' Calcular os descontos '''
    def calcula(self, orcamento):
        ''' Calcula o desconto '''
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        elif orcamento.valor > 350:
            return orcamento.valor * 0.07


if __name__ == '__main__':
    from orçamento import Orcamento, Item

    x = Orcamento(500)
    x.adiciona_item(Item('Item 1', 100))
    x.adiciona_item(Item('Item 2', 50))
    x.adiciona_item(Item('Item 3', 250))
    
    print(x.valor)
    
    calculador = CalculadorDescontos()
    descontos = calculador.calcula(x)
    print(descontos)