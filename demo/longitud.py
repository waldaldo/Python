"""
Se tiene una lista ["gato", "perro", "elefante", "jirafa", "tigre"]
crear una lista de números donde cada número es la longitud de una palabra.
"""

lista = ["gato", "perro", "elefante", "jirafa", "tigre"]

numeros = []
for i in lista:
    numeros.append(len(i))

print(numeros)
