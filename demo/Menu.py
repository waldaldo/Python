# Realizar l;a ejecución de un menu utilizando Python
# donde se le indiquen varias opciones a seleccionar por el usuario 
# y una opción para salir del menu

import re # importar librería para expresiones regulares

patron = re.compile("[12345]")
while True:
    print("Bienvenido al menú")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir del menú")
    
    opción = int(input("Seleccione una opción: "))
    
    if opción == 1:
        print("Seleccionaste la opción 1")
    elif opción == 2:
        print("Seleccionaste la opción 2")
    elif opción == 3:
        print("Seleccionaste la opción 3")
    elif opción == 4:
        print("Hasta luego")
        break

    else:
        print("Elegiste un valor erróneo")

