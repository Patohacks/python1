# elementos del diccionario

camiseta = {
    "color" : "rojo",
    "talla" : "grande",
    "precio" : 100,
    "unidades" : 10,
}
# obtiene la clave del color y busca el resultado 
dato_obtenido = camiseta ["color"]
print (dato_obtenido)

"""
 asiganacion de de las nuevas claves (agregar mas stok al codigo)
"""

# comprobamos stock
print(f"hay {camiseta['unidades']} unidades en almacen")

# modificamos unidades de stock
camiseta ["unidades"] = 25

# comprobamos stock
print(f"hay {camiseta['unidades']} unidades en almacen")

# crear nuevo clave valor despues de ya haber creado el diccionario

camiseta ["marca"] = "america"
print (camiseta)

# eliminar una clave y su valor en el diccionario

del camiseta["color"]

print (camiseta)

# y para eliminar todo el diccionario completo 

del camiseta
print (camiseta) # al ejecutarlo en directo maracara error porque fue elininada la lista 