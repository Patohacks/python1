# metodo index (no busca todas las concidencias )

Numeros = [10,20,30,40,50,60,70,80,90,100.]
#           0  1  2  3  4  5  6  7  8  9
print (Numeros)

busca_numero = Numeros.index(50)
print (busca_numero)

# metodo count (busca todas las concidencias)

ejercicio2 = input("enter para ejercicio 2")

Numeros2 = [5,10,15,20,20,20,4,50,20,20,5,6]

valor_busqueda = (20)

concidencias = Numeros2.count(valor_busqueda)
print(f"en total, el valor de busqueda {valor_busqueda}, tiene {concidencias} concidencias.")

# metodo mas avansado (aun no visto totalmente en clase) INPORTANTEEEEEEE

ejercicio3 = input("enter siguiente ejercicio")
print(ejercicio3)
numeros = [87,10,5,7,378,10,10,65,10,]

valor_busqueda = int(input("introdusca un valor a buscar:"))

concidencias = numeros.count(valor_busqueda)

print(f"en total, el valor de busqueda {valor_busqueda}, tiene {concidencias} concidencias.")
