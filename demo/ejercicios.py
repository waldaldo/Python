# rt = 1/((1/r1)+(1/r2)+(1/r3))

# Ingresar las resistencias

r1 = float(input("Ingrese la resistencia 1: "))
r2 = float(input("Ingrese la resistencia 2: "))
r3 = float(input("Ingrese la resistencia 3: "))

# Calcular la resistencia

rt = 3/((1/r1)+(1/r2)+(1/r3))

# Imprimir la resistencia

print("La resistencia total es: {:.3f}".format(rt))  # {:.3f} indica cuantos decimales se requieren, en este caso 3



