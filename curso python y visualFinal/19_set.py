"""
los SET son como listas desordenadas pero tampoco pueden modificarse. podemos eliminar o agregar pero 
nunca reasignar. cada ves que ejecutes el acomodo sera diferente, EN LOS SET LOS ELEMENTOS SON UNICOS NO PUEDE HAVER DUPLICADOS.

"""

set_colores = {"rojo", "amarillo", "plateado", "dorado", "verde", "azul"}
print(set_colores)


"""
esto pasa porque no tienen valores como las listas o las duplas 
ejemplo:
Numeros = [10,20,30,40,50,60,70,80,90,100.]
#           0  1  2  3  4  5  6  7  8  9

el set no tien el acomodo de listas o duplas
set_colores = {"rojo", "amarillo", "plateado", "dorado", "verde", "azul"}

"""

# pero se pueden agregar con el metodo add

set_colores2 = {"rojo", "amarillo", "plateado", "dorado", "verde", "azul"}

set_colores2.add("arcoiris")

print(set_colores2)

# y para eliminar

set_colores3 = {"rojo", "amarillo", "plateado", "dorado", "verde", "azul"}

set_colores3.remove("rojo")

print(set_colores3)