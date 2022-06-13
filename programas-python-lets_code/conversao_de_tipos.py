# CONVERSÃO DE TIPOS

idade = '26'

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

""""
Outras funções de conversão
int()
str()
float()
bool()
"""

# Problema, a entrada receber apenas string
altura = input('Informe sua altura: ')

print(altura, type(altura))

# Solução, é necessário fazer a conversão da entrada
altura2 = float(input('Informe sua altura: ')) 

print(altura2, type(altura2))


