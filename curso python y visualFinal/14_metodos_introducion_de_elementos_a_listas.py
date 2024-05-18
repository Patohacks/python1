#reasignacion de elementos una manera de formatear un str individual.

colores = ["verde","rojo","amarillo","rojo"]
    #        0        1        2        3

colores[0] = "dorado"
print(colores)


# Ejemplo numero 2 con metodo APPEND, reasignacion de espacio final aun no creado

colores1 = ["amarillo","rojo","verde"]
   #           0          1       2       3

colores1.append("plateado")
print (colores1)


# Metodo insert funciona para reasignar un espacio ya creado y cambiarlo

colores2 = ["amarillo","rojo","verde"]
    #           0         1      3  

colores2.insert(0,"plateado")
print (colores2)

# metodo extend sirve para extender una lista

colores3 = ["verde","rojo","amarillo","morado"]
colores4 = ["naranja","cafe","azul"]
colores5 = ["rosa","fiusha","amaranto"]


colores3.extend(colores4 + colores5)
print(colores3)