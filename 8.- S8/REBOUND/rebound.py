"""
En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es:
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
"""
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# Eliminar elementos duplicados
mi_lista = list(set(mi_lista))
print("Se eliminan los elementos duplicados: ", mi_lista)

# Ordenar la lista resultante en orden ascendente
mi_lista.sort()
print("Lista ordenada en forma ascendente ", mi_lista)

print(mi_lista)
