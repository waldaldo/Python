"""
Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en
pantalla el valor de cada elemento indicando si es par, impar o cero.

"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in lista:
    if i == 0:
        print(f"El numero {i} es cero")
    elif i % 2 == 0:
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar")
