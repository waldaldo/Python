#  estructuras condicionales
# El método de ingreso por consola se realiza con el método input()

numero = int(input("Ingrese un numero entero: "))
print(type(numero))

# if(condición), donde condición siempre es True, al menos que se cambie o modifique
if (numero > 0):
    print(f"El numero {numero} es mayor a 0")
elif (numero == 0):
    print(f"El numero {numero} es igual a 0")
else:
    print(f"El numero {numero} es menor a 0")

