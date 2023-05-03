"""
Simula un programa que permite a los usuarios adivinar una palabra secreta
"""
import random

palabras_secretas = ["arroz", "pure", "pollo", "chorrillana"]
ingreso = ""
adivinar = random.choice(palabras_secretas)
intentos = 5
turno = 0
while adivinar != ingreso and turno < intentos:
    ingreso = input("Ingrese su palabra: ")
    turno += 1
    if ingreso == adivinar:
        print(f"Ya ganaste! Encontraste la palabra secreta en {turno}")
    elif turno == intentos:
        print(f"No tienes mas intentos, la palabra secreta era {adivinar}")
    else:
        print(f"Sigue intentando, este es tu {turno} intento de 5")
