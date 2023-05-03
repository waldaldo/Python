"""
De una lista de números se requiere encontrar el primer número par
en la lista utilizando el bucle while
"""

lista = [3, 5, 1, 6, 7, 1, 11]
i = 0
while i < len(lista):
    if lista[i] % 2 != 0:
        i += 1
    else:
        print(f"El primer numero par es {lista[i]}")
        break
else:
    print("No hay numero par")
