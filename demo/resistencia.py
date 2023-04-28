# rt = 1/((1/r1)+(1/r2)+(1/r3))

# Ingresar las resistencias

r1 = float(input("Ingrese la resistencia 1: "))
r2 = float(input("Ingrese la resistencia 2: "))
r3 = float(input("Ingrese la resistencia 3: "))

# Calcular la resistencia

rt = 3 / ((1 / r1) + (1 / r2) + (1 / r3))

# Imprimir la resistencia

print("La resistencia total es: {:.3f}".format(rt))  # {:.3f} indica cuantos decimales se requieren, en este caso

"""
Validar el ingreso de la resistencia, que sea mayor que 0, controlar error, y utilizar funciones
"""


# Funcion para validar el ingreso de la resistencia
def validate_input_float(texto):
    while True:
        try:
            r = float(input(texto))
            if r > 0:
                return r
            else:
                print("El valor es menor a 0")
        except Exception as e:
            print("Ha ocurrido un error: {}".format(e))
            print("Ingrese una resistencia valida")


r_1 = validate_input_float("Ingrese la resistencia 1: ")
r_2 = validate_input_float("Ingrese la resistencia 2: ")
r_3 = validate_input_float("Ingrese la resistencia 3: ")

# Calcular la resistencia

resistencia_total = 3 / ((1 / r_1) + (1 / r_2) + (1 / r_3))

print("La resistencia total es:", resistencia_total)
