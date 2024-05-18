"""
A diferencia de las listas, la tupla no puede modificarse.

"""


tupla_colores = ("rojo","azul","verde","amarillo","plateado")
#                  0      1        2        3         4    
print(tupla_colores[2])


"""
pero en tiempo de ejecucion del programa si puedes hacer lecturas de posiciones pero no borrar ni mofdificar
ejemplo

"""


tupla_playeras = ("grande", "mediana", "chica", "muy grande.")
#                   0         1           2           3    

print (tupla_playeras.index("mediana")) # o usar el metodo count para buscar concidencias.