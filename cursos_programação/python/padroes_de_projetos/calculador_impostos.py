from descontos import DescontosCinco, DescontosQuinhentos, SemDesconto
from orçamento import Orcamento, Item
from impostos import ICMS, ISS, ICPP, IKCV, template_de_imposto_condicional


class CalculadorImpostos(object):
    ''' Classe para calcular impostos '''
    def realizar_calculo(self, orcamento, imposto):
        ''' Método para realizar o cálculo do imposto '''
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':

    calculador = CalculadorImpostos()
    orcamento = Orcamento(750)
    orcamento.adiciona_item(Item('Item 1', 100))
    orcamento.adiciona_item(Item('Item 2', 100))
    orcamento.adiciona_item(Item('Item 3', 250))
    
    print("ISS e ICMS")
    calculador.realizar_calculo(orcamento, ISS())
    calculador.realizar_calculo(orcamento, ICMS())
    
    print("ICPP e IKCV")
    calculador.realizar_calculo(orcamento, ICPP())
    calculador.realizar_calculo(orcamento, IKCV())
