# LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 7.8, 5.3]

# Criando Listas
lista = []
lista = list()
lista = [26, 'Marcos Vinicius', False]
lista_de_listas = [10, [1, 2, 3]]

#Indexação e Slices (fatiamento)

lista = [10, 'Walisson', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) #Busca o último elemento da lista, o -2 o pnúltimo, sucessivamente.

#Slices

lista = [10, 50, 30, 40, 25, 60, 8]

print(lista[0:3]) # Exibir da posição 0 ate menor do que 3
print(lista[3:]) # Começa no três e vai até o final
print(lista[3:6:2]) # Exibir da posição 3 ate menor do que 6, com passo de 2

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])
