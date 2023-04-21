# lista es una estructura para almacenar datos con un orden especifico

lista = [1, 2, 3, 4, 5, 6,]  # se define con corchetes []
lista_diferentes_valores = [8,"9", True, 10, lista]

print(lista)

# Para acceder a un elemento de la lista se utilizan los indices, los cuales comienzan por 0
# hasta n-1, si se utilizan numeros negativos se accede desde el ultimo elemento de la lista

print(lista[0])
print(lista[-3])

# metodos de las listas
# append() agrega valores al final de la lista
lista.append(7)  # se agrega un elemento al final de la lista
print(lista)    

# insertar por indice
lista.insert(0, 1)  # se inserta el elemento 1 al inicio de la lista

# remove() elimina un elemento de la lista 
lista.remove(5)  # se elimina el elemento 5
print(lista)

del(lista[0])  # se elimina el primer elemento de la lista
print(lista)


# para conocer el indice por el elemento
lista.index(5)  # se obtiene el indice del elemento 5
print(lista) 

