edad = 76

if edad < 18:
    print ("es menor de edad.")
if edad > 18:
    print ("es adulto.")
if edad >= 18:
    print("es maduro")
if edad > 75:
    print("es anciano")

# una manera mas correcta pero no la mejor  (solo da una solucion)

edad = 76

if edad < 18:
    print ("es menor de edad.")
if edad >= 18 and edad <= 65:
    print ("es adulto.")
if edad > 65 and edad <= 75:
    print("es maduro")
if edad > 75:
    print("es anciano")