''' Classe para retorna o URL '''

import re

class ExtratorUrls:
    ''' Extrair parametros da URL '''
    def __init__(self, url):
        ''' Inicializar a classe '''
        self.url = self.sanitizar_url(url)
        self.valida_url()

    def sanitizar_url(self, url):
        ''' Sanitizar a URL '''
        if isinstance(url, str):
            return url.strip()
        return ''

    def valida_url(self):
        ''' Validar a URL '''
        if not self.url:
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        ''' Retorna a URL base sem query '''
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_params(self):
        ''' Retorna os parametros da URL '''
        indice_interrogacao = self.url.find('?')
        url_params = self.url[indice_interrogacao+1:]
        return url_params

    def get_valor_params(self, parametro_busca):
        ''' Retorna o valor de um parametro da URL '''
        indice_parametro = self.get_url_params().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_params().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_params()[indice_valor:]
        else:
            valor = self.get_url_params()[indice_valor:indice_e_comercial]
        return valor
    def __len__(self):
        ''' Retorna o tamanho da URL '''
        return len(self.url)
    def __str__(self):
        ''' Retorna a URL '''
        return self.url
    def __eq__(self, outra_url):
        ''' Compara se duas URLs são iguais '''
        return self.url == outra_url.url

url2 = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorUrls(url2)

### DESAFIO ###
# Conversão de dólar para real
valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_params("moedaOrigem")
moeda_destino = extrator_url.get_valor_params("moedaDestino")
quantidade = extrator_url.get_valor_params("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / valor_dolar
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * valor_dolar
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
