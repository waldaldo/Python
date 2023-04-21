# Estructura de un diccionario es clave, valor
# colección de datos ordenados por la clave valor

mi_diccionario = {
    'nombre': 'Eduardo', 'apellido': 'Hurtado','edad': 45
    }

estudiantes = {
    #clave: valor,
    'Fulanito':25,
    'Juan':30,
    'Pedro':25,
    'Maria':25,
    'Juan':25,
    'Pedro':25,    
}

print(estudiantes) #{'Fulanito':25, 'Juan':30, 'Pedro 

# Para acceder a una clave de un diccionario
# nombre_diccionario["clave"] 
print(estudiantes['Fulanito'])

# Remover clave de un diccionario
del estudiantes['Fulanito'] 
print(estudiantes)

# para obtener las claves de un diccionario
claves = estudiantes.keys()
print(claves)   

# borrar un diccionario 
estudiantes.clear()
print(estudiantes)