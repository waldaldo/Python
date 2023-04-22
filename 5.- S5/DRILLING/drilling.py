"""
Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las
consonantes restantes y su posición dentro de dicha palabra.
"""
palabra = "paralelepípedo"
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] not in "aeiíouAEIÍOU":
        consonantes += palabra[i]
        print(f"La letra {palabra[i]} se encuentra en la posicion {i}")
        
print(consonantes)