# Listas e suas funções

# Para criar uma lista, simplesmente encerre os elementos entre colchetes:

# frutas = ['maça', "banana", 'laranja' ] 
# print(frutas[0])
# print(frutas[1])
# print(frutas[2])

# Para acessar os elementos de uma lista, utilize o índice do elemento entre colchetes. Os índices começam a partir de 0.

# Você também pode acessar os elementos a partir do final da lista utilizando índices negativos. O índice -1 representa o último elemento, -2 representa o penúltimo, e assim por diante.
# frutas = ['maça', 'banana','laranja']
# print(frutas[-1])
# print(frutas[-2])
# print(frutas[-3])

# Métodos de listas

# As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são:

# append(elemento): adiciona um elemento ao final da lista.
# insert(indice, elemento): insere um elemento em uma posição específica da lista.
# remove(elemento): remove a primeira ocorrência de um elemento na lista.
# pop(indice): remove e retorna o elemento em uma posição específica da lista.
# sort(): ordena os elementos da lista em ordem ascendente.
# reverse(): inverte a ordem dos elementos na lista.

# frutas = ['maçã', 'banana', 'laranja']
# frutas.append('pera') #append
# print(frutas)

# frutas.insert(1, 'uva') #insert
# print(frutas)

# frutas.remove('banana')
# print(frutas)

# fruta_removida = frutas.pop(2)
# print(frutas)
# print(fruta_removida)

# frutas.sort
# print(frutas)

# frutas.reverse
# print(frutas)

# Listas de compreensão
# As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.

# números = [1, 2, 3, 4, 5]
# quadrados = [x ** 2 for x in números if x % 2 == 0]
# print(quadrados)
