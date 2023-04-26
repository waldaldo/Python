"""
Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor.
"""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if len({num1, num2, num3}) != 3:
    print("Debe ingresar números diferentes")
else:
    ordenados = sorted([num1, num2, num3], reverse=True)
    print(ordenados)
