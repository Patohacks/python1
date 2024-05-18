"""
TABLAS DE LAS REGLAS DE ((AND))

(true + true = true) 

(true + false = false) 
(false + true = false)
(false + false = false)
"""
a = 15
b = 17
c = 13

# conparaciones 

conparacion_1 = a < b and b > c
conparacion_2 = a > b and b < c

print (conparacion_1)
print (conparacion_2)

"""
TABLAS DE REGLAS DE ((OR))

(true + true = true) 
(true + false = true) 
(false + true = true)
(false + false = false)
"""

ejercicio2 = input ("sigiente ejercicio enter:")
print (ejercicio2)

a1 = 15
b1 = 17
c1 = 13

# conparaciones 

conparacion_3 = a1 < b1 or b1 > c1
conparacion_4 = a1 == b1 or b1 < c1

print (conparacion_1)
print (conparacion_2)