# Se definen utilizando la funcion  list()
# se encuadran en []

lista = [1, 2, 3, 4, 5, 1]
otra_lista = list() # lista vacía
otra_lista = []
otra_lista = [20, 1.75, "Fulanito", "Perez"]

#accedes a la longitud de la lista
print("La longitud de la lista es ", len(lista))

# identificando el tipo de dato del segundo index
print("El tipo de dato es ", type(lista[1]))

# acceder a un elemento de la lista por medio de su indice
print("El primer elemento es ", lista[0])
print("El elemento 2 es ", lista[1]) # la ubicacion del numero 2 en la lista

# Python permite accesar indices desde el final usando números positivos
print("El ultimo elemento es ", lista[-1])
print("El elemento 4 es ", lista[-2]) # la ubicación del número 4 en la list

# contar los elementos existentes de la lista cib ka función count() dado el elemento a buscar
print("La cantidad de veces que se repite 1 en la lista ", lista.count(1))

# acceder a un elemento de una lista por medio de la funcion index()
print("El elemento Fulanito en la lista es ", otra_lista.index("Fulanito"))

# desempaquetar los elementos de la lista en variables
edad, altura, nombre, apellido = otra_lista
print("La edad es ", edad)
print("La altura es ", altura)
print("El nombre es ", nombre)
print("El apellido es ", apellido)

# crear, inserttar, modificar y eliminar elementos de una lista
lista.append(7) # añade elemento al final de la lista
lista.insert(1, 20)  # insertar en el indice 1 el elemento 20
lista.remove(1)  # remover elemento por el elemento
lista.pop() # elimina el ultimo elemento de la lista
lista.clear() # elimina todos los elementos de la lista

lista = [1, 2, 3, 4, 5, 1]

# actualizar elemento de la lista por medio del indice
lista[0] = 10
# actualza el elemento de la lista por el elemento
lista[1] = 20

# Ordenar la lista
lista.sort(reverse=True)
print("La lista ordenada es ", lista)