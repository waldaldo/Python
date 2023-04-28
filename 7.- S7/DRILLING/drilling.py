"""
Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
•Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
•Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.

"""
import time

lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
# acá cada sublista es un item de la lista

# nueva lista eliminando subliustas que comiencen con 0
lista2 = []
for sbl in lista:
    if sbl[0] == 0:
        continue
    lista2.append(sbl)
print(lista2)



for sbl in lista: # toma las sublistas
    if sbl[0] == 0:  # Si primer indice es 0
        continue
    for numero in sbl:
        if numero == 0: # Si existe cero en la posición
            continue
        print(numero) # Imprimir el dato
        time.sleep(0.5) # Esperar 0.5 segundos