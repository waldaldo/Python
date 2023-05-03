# las tuplas son una estructura de datos que se puede acceder por el indice
# se definen con la funcion tuple(), se define con  ()
# las tuplas tambien se pueden declarar sin ()

otra_tupla = 1, 2, 3, 4, 5
sub_tupla = otra_tupla[0:3] # se copian elementos a una nueva tupla, la tupla original noi se modifica
print(sub_tupla)

nombre_tupla = ('Juan', 'Pablo', 'Juan', 'Pedro', 'Jeronimo')
print(nombre_tupla)
# acceso a los indices
print("El elemento en el indice 0 es: ", nombre_tupla[0])
print("El elemento en el indice 1 es: ", nombre_tupla[-1])

# Metodos de las tuplas: count() index()
print("El elemento Juan se repite {} veces".format(nombre_tupla.count('Juan')))
