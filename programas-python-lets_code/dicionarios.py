# > DICIONARIOS

# Criando dicionários

from this import d


dicionario = {}
dicionario = dict()

dicionario = {'nome':'Marcos', 'idade':24, 'altura':1.84}

print(dicionario)
print(dicionario['nome'])

# Adicionando elemento em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# Iteração sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)