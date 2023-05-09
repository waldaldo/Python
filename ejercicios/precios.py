"""
Se solicita crear un diccionario en Python para almacenar los precios de diferentes productos en una tienda en línea.
Las claves del diccionario serán los nombres de los productos y los valores serán los precios de los productos.
A continuación, se solicita recorrer el diccionario e imprimir los productos cuyos precios son superiores a 50 dólares. 
Finalmente, se debe calcular el precio total de los productos cuyos nombres empiezan con la letra 'C' y mostrarlo en pantalla.

precios = {
    'camisa': 30,
    'pantalon': 50,
    'zapatos': 80,
    'calcetines': 10,
    'chaqueta': 100
    }

"""


def crear_producto():
    listado = {}
    print("Creando el listado de productos (S para salir)")
    while True:
        producto = input("Ingresa el producto: ")
        if producto == "S":
            break
        precio = int(input("Ingresa el precio: "))
        listado[producto] = precio
    return listado


# Se llama a la funcion para crear el diccionario
productos = crear_producto()

# Imprime productos con precio superior a 50
print("\n================================")
print('Los productos con precio mayor a 50 son:')
for producto, precio in productos.items():
    if precio >= 50:
        print(f"{producto}: {precio}")


print("\n================================")
print("Imprime los productos que comiencen con la letra C")
for producto, precio in productos.items():
    if producto.startswith("C"):
        print(f"{producto}: {precio}")


# Imprimimos el listado de productos
print("\n================================")
print("Listado de productos:")
for producto, precio in productos.items():
    print(f"{producto}: {precio}")
