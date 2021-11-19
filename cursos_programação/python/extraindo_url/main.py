''' Curso sobre string no python da Alura '''

# Url e imprimindo o resultado
url = 'https://twitter.com/search?q=alura&src=typed_query'
print(url)

# Fatiado a url
url_sem_protocolo = url[8:]
url_base = url_sem_protocolo.split('?')[0]
print(url_base)

# Método find
interrogação = url.find('?')
url_base1 = url[0:interrogação]
url_query1 = url[interrogação+1:]
print(url_base1, url_query1)

