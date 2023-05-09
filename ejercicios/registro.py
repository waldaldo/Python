"""
Se solicita crear un programa en Python que permita llevar el registro de los invitados a una fiesta.
Para ello, se pide crear dos conjuntos (set): uno con los nombres de los invitados confirmados y otro con los nombres de los invitados que han llegado a la fiesta.
A medida que los invitados van llegando a la fiesta, se deben ir agregando sus nombres al conjunto de los que asistieron.
Además, se debe imprimir en pantalla la cantidad de invitados confirmados y la cantidad de invitados que han asistido.
Finalmente, se debe imprimir en pantalla el nombre de los invitados que confirmaron su asistencia pero aún no han llegado a la fiesta, es decir, 
los nombres que se encuentran en el conjunto de confirmados pero no en el conjunto de los que asistieron.
"""


def agregar_confirmados():
    confirmados_set = set()
    while True:
        confirmados = input(
            "Ingrese el nombre de un invitado confirmado\n('S' para salir): ")
        if not confirmados.strip():
            print("Por favor ingrese un nombre válido.")
            continue
        if confirmados == "S":
            break
        confirmados_set.add(confirmados)
        return confirmados_set


def agregar_asistentes(set_asistentes):
    print("Ingrese el nombre del invitado: ", end="")
    set_asistentes.add(input())
    return set_asistentes


def agregar_invitados_asistentes(set_asistentes):
    print("Ingrese el nombre del invitado: ", end="")
    set_asistentes.add(input())
    return set_asistentes


def cantidad_confirmados_o_asistentes(datos):
    print("La cantidad es", len(datos))


def conocer_faltantes(invitados_confirmados, invitados_asistentes):
    faltantes = invitados_confirmados - invitados_asistentes
    print(f"Los invitados faltantes son:", faltantes)


def aplicacion_fiesta():
    invitados_confirmados = set()
    invitados_asistentes = set()
    print('Hola, bienvenido!')
    while True:
        opcion = int(input("Selecciona una opción\n"
                           "1.- agregar_invitados_confirmados\n"
                           "2.- agregar_invitados_asistentes\n"
                           "3.- cantidad_confirmados_o_asistentes\n"
                           "4.- conocer_faltantes\n"
                           "5.- Salir\n\n"
                           "Ingresa una opción => ")
                     )

        match opcion:
            case 1:
                invitados_confirmados = agregar_confirmados()
            case 2:
                invitados_asistentes = agregar_asistentes(invitados_asistentes)
            case 3:
                print("Desea conocer los invitados asistentes o confirmados")
                print("1.- Asistentes")
                print("2.- Confirmados ", end="")
                ingreso = input()
                if (ingreso == 1):
                    cantidad_confirmados_o_asistentes(invitados_asistentes)
                else:
                    cantidad_confirmados_o_asistentes(invitados_confirmados)
                print('\n')
            case 4:
                conocer_faltantes(invitados_confirmados, invitados_asistentes)
                print('\n')
            case 5:
                print("Nos vemos!")
                break
            case _:
                print("Esa opción no es válida!")


aplicacion_fiesta()
