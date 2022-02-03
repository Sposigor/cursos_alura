''' Curso sobre string no python da Alura '''

# Exemplo dado pela Alura para extrair o endereço de uma URL
# URL
url = ""

# Sanitizando a URL
url = url.strip()


# validação da URL
if url == "":
    raise ValueError("URL está vazia/invalida")

# Extraindo os parametros da url
indice_interrogacao = url.find('?') # retorna o indice da primeira ocorrencia
url_base = url[:indice_interrogacao] # retorna a string até o indice
url_parametros = url[indice_interrogacao+1:] # retorna a string a partir do indice

# Buscando os parametros
parametro_busca = 'quantidade' # parametro a ser buscado
indice_parametro = url_parametros.find(parametro_busca) # retorna o indice da primeira ocorrencia
indice_valor = indice_parametro + len(parametro_busca) + 1  # retorna o indice do valor

# Extraindo o parametro &
indice_e_comercial = url_parametros.find('&', indice_valor) # retor. o indice da primeira ocorrencia

# Extraindo o valor
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
