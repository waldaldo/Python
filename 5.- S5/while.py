# ciclo while
# ciclo while(condicion) la condición siempre será evaluada como True al menos que se cambie

i = 0
while i <= 5:
    i+=1 #contador
    print(f"Imprimiendo el valor de i {i}") 


i = 0
while i <= 5:
    i+=1 #contador
    if i == 1:
        continue
    print(f"Imprimiendo el valor de i {i} y probando continue") 


i = 0
while i <= 5:
    i+=1 #contador
    if i == 4:
        break
    print(f"Imprimiendo el valor de i {i} y probando el break") 
