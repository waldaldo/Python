"""
De una lista dada, encontrar el numero mas grande utilzando bucle for

"""
import math


lista = [45, 23, 67,90, 89, 12, 56, 78]
num = lista[0]

for elemento in lista:
    if elemento > num:
        num = elemento
print(num)

