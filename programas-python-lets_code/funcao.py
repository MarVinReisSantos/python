# > FUNÇÕES

# 1. O que são funções e por que utilizá-las

# Funções que já utilizamos anteriomente...
'''
print() # - Imprimi uma mensagem (int, float, str) no console
input() # - Retorna uma dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - Retorna o maior valor de uma lista
'''
# 2. Criação de Funções

# Função inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso')

saudacao()

# Função parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}')

saudacao('Marcos', 'Python')

# Função com parametro default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}')

saudacao('Marcos')

# Funções com retorno

def soma(soma1, soma2):
    return soma1+soma2

resultado = soma(5, 7)

print(f'O resultado da soma é {resultado}')

def calculadora(num1, num2, operacao='+'):
    if operacao=='+':
        return num1+num2

    elif operacao=='-':
        return num1-num2

    elif operacao=='*':
        return num1*num2

    elif operacao=='/':
        return num1/num2


print('A soma é ', calculadora(10,5))
print('A subtração é ', calculadora(10,5, '-'))
print('A divisão é ', calculadora(10,5, '/'))
print('A multiplicação é ', calculadora(10,5, '*'))
