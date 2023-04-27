"""
Ciclo for
"""
import time
lista = [1, 2, 3, 4, 5, 6]

# recorriendo cada uno de los elementos
for item in lista:
    print("Recorriendo el elemento de la lista ", item)
    time.sleep(1)

for item in range(len(lista)):
    print("Recorriendo el indice de la lista ", item)
    print("Recorriendo el elemento de la lista ", lista[item])
    #lista.[item] muestra el valor, lista solo muestra el indice
    time.sleep(1)
