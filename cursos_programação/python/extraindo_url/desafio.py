''' Desafio: Conversão de moedas - dólar e real - Alura '''

import requests # importando a biblioteca request

class DolarNow:
    ''' Trás a cotação do dolar atual '''

    def __init__(self):
        ''' Inicializando o valor do dólar '''
        self.dolar = self.get_dolar()

    def get_dolar(self):
        ''' Retorna o valor do dólar '''
        resposta = requests.get('https://economia.awesomeapi.com.br/json/USD-BRL')
        json = resposta.json()

        for cotacao in json:
            valor_dolar_em_reais = cotacao['high']
            break

        return float(valor_dolar_em_reais)

    def print_dolar(self):
        ''' Imprime o valor do dólar '''
        print(f'Valor do dólar em reais: R$ {self.dolar}')

dolar = DolarNow()
print(f'Atual valor do dolar: {float(dolar.dolar)}')

conversor = input('Digite o valor a ser convertido em reais: ')
print(f'Valor convertido em dólar: US$ {float(conversor) / dolar.dolar:.2f}')

conversor2 = input('Digite o valor a ser convertido em dólar: ')
print(f'Valor convertido em reais: R$ {float(conversor2) * dolar.dolar:.2f}')
