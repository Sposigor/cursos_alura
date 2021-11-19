''' Classe para retorna o URL '''
class ExtratorUrls:
    ''' Extrair parametros da URL '''
    def __init__(self, url):
        ''' Inicializar a classe '''
        self.url = self.sanitizar_url(url)

    def sanitizar_url(self, url):
        ''' Sanitizar a URL '''
        if type(url) == str:
            return url.strip()
        return ''

    def valida_url(self):
        ''' Validar a URL '''
        if not self.url:
            raise ValueError('URL vazia')

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
