""""
Solicita al ususario ingresar una contraseña hasta que  la contraseña
coincida con una contraseña predefinida
"""

password = "password"
intentos = 3
while (intentos > 0):
    clave = input("Ingresa tu clave: ")
    if clave == password:
        print("Contraseña correcta")
        break
    else:
        print(f"Contraseña incorrecta, te quedan {intentos - 1} intentos")
        intentos -= 1
print("No hay mas intentos")