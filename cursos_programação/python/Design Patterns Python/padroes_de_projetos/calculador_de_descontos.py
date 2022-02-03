from descontos import DescontosCinco, DescontosQuinhentos, SemDesconto
from orçamento import Orcamento, Item
from impostos import ICMS, ISS, ICPP, IKCV
from calculador_impostos import CalculadorImpostos

class CalculadorDescontos(object):
    ''' Calcular os descontos '''
    def calcula(self, orcamento):
        ''' Calcula o desconto '''
        descontos = DescontosCinco(
            DescontosQuinhentos(SemDesconto())
            ).calcula(orcamento)
        return descontos


if __name__ == '__main__':
    calculador = CalculadorImpostos()
    x = Orcamento(500)
    x.adiciona_item(Item('Item 1', 100))
    x.adiciona_item(Item('Item 2', 100))
    x.adiciona_item(Item('Item 3', 250))
    
    print("ISS e ICMS")
    calculador.realizar_calculo(x, ISS)
    calculador.realizar_calculo(x, ICMS)
    
    print("ICPP e IKCV")
    calculador.realizar_calculo(x, ICPP)
    calculador.realizar_calculo(x, IKCV)