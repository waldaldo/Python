"""
Simula un juego de adivinanza donde el jugador debe adivinar un numero aleatorio generado por el programa
El programa le dará pistas al jugador sobre si el numero ingresado es mayor 
o menor que el numero generado y seguirá pidiendo al jugador que ingrese un numero hasta que adivine correctamente
"""

import random
import os

os.system('clear')

print("""
####### Probemos tus poderes mentales! #######

Te pediré dos números para establecer un rango,
tomaré un número y veamos si lo adivinas ;) 

""")

numero1 = int(input("Ingresa tu primer número: "))
numero2 = int(input("Ingresa tu segundo número: "))

adivinar = 0
intento = 0

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

numero_random = random.randint(menor, mayor)
# print(numero_random)


print(f""" 
Lo tengo, debes adivinar un número entre {menor} y {mayor}
""")

while adivinar != numero_random:
    adivinar = int(input('Ingresa tu número: '))
    intento += 1
    if adivinar >= menor and adivinar <= mayor:
        if adivinar > numero_random:
            print(
                f"Tu numero es mayor al número a adivinar, llevas {intento} intento(s)")
        elif adivinar < numero_random:
            print(
                f"Tu numero es menor al número a adivinar, llevas {intento} intento(s)")
        else:
            print(f"Excelente! Adivinaste en tu intento número {intento}")
    else:
        print(f"Ingresa un número entre {numero1} y {numero2}")
