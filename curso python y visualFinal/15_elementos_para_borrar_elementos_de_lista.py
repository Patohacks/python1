# Metodo POP sirve para eliminar un elemento de una lista

colores = ["verde","rojo","amarillo","morado"]
#             0       1        2         3

colores.pop()  # este metodo elimina el ultimo color en la lista 
print(colores)

colores1 = ["verde","rojo","amarillo","morado"]
#              0       1        2         3   

colores1.pop(2) # Con el metodo int eliminas el color de la posicion que quieras
print(colores1)

# Metodo REMOVE elimina literalmente el valor elegido

colores2 = ["verde","rojo","amarillo","morado"]
#              0       1        2         3   

colores2.remove("rojo")  # ojo este metodo no elimina duplicados
print(colores2)


colores3 = ["rojo","amarillo","rojo","plateado","rojo"]
#              0        1        2       3         4 

colores3.remove("rojo")
print(colores3)

# Ejemplo para solucionar el eliminar valores duplicados 

colores4 = ["rojo","amarillo","rojo","plateado","rojo"]
#              0        1        2       3         4 

colores4.remove("rojo")
colores4.remove("rojo")
colores4.remove("rojo")
print(colores4)

# o aplicando eliminacion en bucle (aun no aprendido en clase)
