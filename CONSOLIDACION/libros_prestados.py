"""
Se solicita crear un programa en Python que permita Ilevar el registro
de los libros que han Sido prestados por una biblioteca.
Para ello, se pide crear un conjunto (set) con los nombres de los libros
prestados.

A continuación, se solicita imprimir en pantalla la cantidad total de libros
prestados.

Finalmente, se debe crear Otro conjunto con los nombres de los libros
que han Sido devueltos y mostrar en pantalla los libros que aün no han Sido
devueltos.

libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del c61era', 'La ciudad y los
perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Páramo', 'La tregua'}
"""

libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del có1era',
                    'La ciudad y los perros', 'La casa verde', 'El otoño del patriarca',
                    'Rayuela', 'Pedro Páramo', 'La tregua'}

print("Cantidad de libros prestados hasta el momento: ", len(libros_prestados))

libros_devueltos = ['Cien años de soledad', 'El amor en los tiempos del có1era',
                    'La ciudad y los perros']

# difference muestra la diferencia entre dos sets
libros_faltantes = libros_prestados.difference(libros_devueltos)
print(libros_faltantes)
