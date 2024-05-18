"""
lo mismo que el ejercicio anteriorr, pero andeves de que sea individual 
sera en conjunto de resultados 
"""

codigo = int(input("introdusca el codigo http: "))

match codigo:
    case 100 | 101 | 102:
        print("codigo de tipo informativo.")
    case 200 | 201 | 202 | 203:
        print("codigo de exito")
    case 300 | 301 | 302 | 303:
        print("codigo de redireccion")
    case 400 | 404 | 407:
        print("codigo de error al cliente")
    case 500 | 502 | 599:
        print("codigo de error en el servidor")
    case _:
        print("codigo no disponible")