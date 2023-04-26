# Realizar la ejecución de un menu utilizando Python
# donde se le indiquen varias opciones a seleccionar por el usuario 
# y una opción para salir del menu

# importar librería para expresiones regulares
import re

patron = re.compile("[1-5]")
while True:
    print("Bienvenido al menú")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir del menú")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print("Seleccionaste la opción 1")
    elif opcion == 2:
        print("Seleccionaste la opción 2")
    elif opcion == 3:
        print("Seleccionaste la opción 3")
    elif opcion == 4:
        print("Hasta luego")
        break

    else:
        print("Elegiste un valor erróneo")