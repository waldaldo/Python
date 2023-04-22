# Operadores Lógicos
# and or not
# evlauar booleanos

a = True
b = False

print(a and b) #False, se deben cumplir ambas condiciones
print(a or b)  #True, debe cumplirse alguna de las condiciones
print(not a)   #False 
print(not (a or b)) #False, primero se evalúa el paréntesis y luego se cambia con not

# Operadores de comparación
# Evalúan valores, largos de una cadena, etc
# < > = != >= <=

c = 10
d = 5

print(c < d) #False
print(c > d) #True

print(c <= d) #True, no es menor o igual que d
print(c >= d) #False, c no es mayor o igual que d
print(c == d) #False, no son iguales
print(c!= d) #True, son distintos

