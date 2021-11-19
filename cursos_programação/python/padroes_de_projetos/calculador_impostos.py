from impostos import ICMS, ISS


class CalculadorImpostos(object):
    ''' Classe para calcular impostos '''
    def realizar_calculo(self, orcamento, imposto):
        ''' Método para realizar o cálculo do imposto '''
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':
    from orçamento import Orcamento

    calculador = CalculadorImpostos()
    orçamento = Orcamento(500)
    calculador.realizar_calculo(orçamento, ISS)
    calculador.realizar_calculo(orçamento, ICMS)
