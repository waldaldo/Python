def factorial(n):
    resultado = 1
    contador = n
    while contador > 0:
        resultado *= contador
        contador -= 1
    return resultado

a = int(input("ingresa un número: "))

print(f"El factorial es {factorial(a)}")