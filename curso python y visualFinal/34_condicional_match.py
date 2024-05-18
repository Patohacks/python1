


codigo = input("introduce un codigo http:")
match codigo:
    case "200":
        print("todo ok.")
    case "301":
        print("movimiento permanente de la pagina:")
    case "302":
        print("movimiento temporal de la pagina:")
    case "404":
        print("pagina no encontarda")   
    case "500":
        print("erroro interno del servidor:")
    case "503":
        print("pagina no disponible")   
    case _:
        print("codigo no disponible")