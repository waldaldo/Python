# Simulación de una bomba de tiempo. Ira el tiempo desde 5 a 1 en decremento.
# Al ejecutar el; programa, se imprimirá el mensaje Booom!

import time
t = 5

while t > 0:
    print(f"Faltan {t} segundos")
    t -= 1
    time.sleep(1)

print("Boom!") 
