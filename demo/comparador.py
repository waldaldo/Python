# Pedir el ingreso de dos textos al usuario por consola 
# y comparar si son iguales o del mismo tamaño

dato1 = input("ingrese el primer dato: ")
dato2 = input("ingrese el segundo dato: ")

# Comparar

if len(dato1) == len(dato2):
    print("Los datos tienen la misma longitud")
elif dato1 == dato2:
    print("Los datos son iguales")
else:
    print("Los datos ingresados son distintos")