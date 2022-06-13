# COMANDO FOR

#Função1 range(ate_menor_do_que)
#Função2 range(começo, ate_menor_do_que)
#Função3 range(começo, ate_menor_do_que, passo)

""" Explicação do codigo for

# Range vai até menor do que 10
for variavel in range(10):
    print(variavel)

# Range vai até menor do que 10 começando com 1
for variavel in range(1, 10):
    print(variavel)

# Range vai até menor do que 10 começando com 1 e com passo 2
for variavel in range(1, 10, 2):
    print(variavel)

"""
#Problema proposto, use o laço de repetição for para fazer a média de três notas do estudante
nota = 0
contador_nota = 0

for contador in range(1, 4):
    nota += float(input(f'Digite a {contador} nota do aluno: '))
    contador_nota += 1

print('A media das notas é: ', (nota/contador_nota))