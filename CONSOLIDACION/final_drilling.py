"""
Dada la siguiente lista de nombres:
•Harry Houdini
•Newton
•David Blaine
•Hawking
•Messi
•Teller
•Einstein
•Pele
•Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

"""
# Lista de nombres entregada
lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]


# Función hacer grandioso
def hacer_grandioso():
    for i in range(len(magos)):
        magos[i]= "El grandioso " + magos[i]

# Función para imprimir nombres
def imprimir_nombres(a):
    for i in a:
        print(i)

# Separamos los nombres en tres grupos: magos, científicos y otros
magos = []
cientificos = []
otros = []

for nombre in lista:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

print("Se imprime la lista completa de nombres.")
imprimir_nombres(lista)

print("""###########################
Los magos de la lista son...""")
hacer_grandioso()
imprimir_nombres(magos)

print("""###########################
Los científicos de la lista son...""")
imprimir_nombres(cientificos)

print("""###########################
Y los irrelevantes son...""")
imprimir_nombres(otros)
