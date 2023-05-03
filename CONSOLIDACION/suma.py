"""
Se tiene la siguiente lista de numeros

Calcular la suma de todos los numeros de la lista utilizando un bucle while

"""

lista = [3, 5, 2, 8, 1, 10]
i = 0
suma = 0

while i < len(lista):
    suma += lista[i]
    i += 1
print(f"El valor de la suma de todos los numeros de la lista es {suma}")
