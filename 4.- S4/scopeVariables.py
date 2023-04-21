# Scope o alcance de una variable

# alcance global, variables que se encuentran fuera de una estructura
variable_global = "Se puede acceder a una variable global en todo el codigo"

# Alcance local, están dentro de una estructura como una función
#def funcion_local(parametros_entrada):
def suma(a,b):
    suma_valores = a + b # suma es una variable local
    variable_global = suma_valores # Aqui sele asigna suma a la variable global
    return suma_valores  # despues de la función, suma_valores no se puede acceder

print(suma(1,2)) # devuelve 3 porque se accede como metodo

print(variable_global) # devuelve "Se puede acceder a una variable global en todo el codigo"

#print(suma_valores) # Devuelve variable no definida porque no puede acceder a la variable local

#

