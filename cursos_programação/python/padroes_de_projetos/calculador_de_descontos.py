from descontos import DescontosCinco, DescontosQuinhentos, SemDesconto 

class CalculadorDescontos(object):
    ''' Calcular os descontos '''
    def calcula(self, orcamento):
        ''' Calcula o desconto '''
        descontos = DescontosCinco(
            DescontosQuinhentos(SemDesconto())
            ).calcula(orcamento)
        return descontos


if __name__ == '__main__':
    from orçamento import Orcamento, Item

    x = Orcamento(500)
    x.adiciona_item(Item('Item 1', 100))
    x.adiciona_item(Item('Item 2', 100))
    x.adiciona_item(Item('Item 3', 250))
    
    print(x.valor)
    
    calculador = CalculadorDescontos()
    descontos = calculador.calcula(x)
    print(descontos)