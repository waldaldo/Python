# colección de elementos que se pueden modificar, se pueden remover, pero son unicos

nombre_set = set({1, 2, 3, 4, 5, 6, 7,8,9,10,11})
set = {1,1,2,3}

print(set) #{1,2,3}

# metodos del set
# agregar elemento
set.add(4)
print(set) #{1,2,3,4}

#remover .remove(elemento)
set.remove(1)
print(set) #{2,3}
