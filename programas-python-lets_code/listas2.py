# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2] 

# append -> Adiciona item ao final da lista

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# insert -> Escolhe a posição no qual vamos adicionar o novo elemento

lista.insert(2, 10)

print('Depois do insert: ', lista)

# extend -> Junta duas listas

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

# pop -> Remove o último elemento, se caso não especificamos qual elemento desejamos remover.

lista.pop()

print('Lista após o prop: ', lista)

lista.pop(0) # remover da posição 0
print('Lista após o prop: ', lista)

# remove -> para removemos um elemento especifico.

lista.remove(3); # remover apenas o primeiro 3 que ele encontrar na lista

# count -> quantos numeros x tem na lista?

print('Quantidade de 2 na lista: ', lista.count(2))

# index -> para encontrar o index de um determinado elemento

print('Indice do elemento 12: ', lista.index(12))

# sort -> usando para ordenar a lista de forma crescente. Podemos usar o parâmetro lista.sort(reverse=True) para ordenar de forma descrescente

lista.sort() 


# FUNÇÕES PARA LISTAS

# len -> retorna o tamanho da lista
print(len(lista))

# sum -> retorna a soma dos elementos da lista

print(sum(lista))

# max -> retorna o maior valor da lista

print(max(lista))

# min -> retorna o menor valor da lista

print(min(lista))


