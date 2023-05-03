"""
Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
•Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
•Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.

•Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
•Finalmente, imprimiremos en pantalla el diccionario resultante.
Ejemplo de impresión en pantalla:
A:[1, 2, 3]
"""

import time

lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
# acá cada sublista es un item de la lista

diccionario = dict()
otro_diccionario = dict()
claves = ["A", "B", "C", "D"]

contador = 0  # conocer la posicion de la lista para las claves y agregar elementos al diccionario

for sbl in lista:  # toma las sublistas
    # insertar nombre_diccionario[clave] = valor
    diccionario[claves[contador]] = sbl
    otro_diccionario[claves[lista.index(sbl)]] = sbl
    contador += 1
    if sbl[0] == 0:  # Si primer indice es 0
        continue
    for numero in sbl:
        if numero == 0:  # Si existe cero en la posición
            continue
        print(numero)  # Imprimir el dato
        time.sleep(0.5)  # Esperar 0.5 segundos

# diccionario = {'A': lista[0], 'B': lista[1], 'C': lista[2], 'D': lista[3]}
print(diccionario)
