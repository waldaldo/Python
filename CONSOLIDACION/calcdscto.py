"""
calcular el precio total de la compra con un 10% de descuento
"""

lista = [25.50, 12.30, 36.40, 9.75, 15.20]
i = 0
suma = 0

while i < len(lista):
    suma += lista[i]
    i += 1
print("El valor total de la compra es {:.2f}".format(suma))
print("Y con un 10% de descuento queda en {:.2f}".format(suma * 0.9))

