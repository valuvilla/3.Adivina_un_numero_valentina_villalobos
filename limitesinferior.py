import sys



def limite_inf():
    while True:
        minimo=input('¿Cuál es el número más pequeño del intervalo?: ')
        try:
             minimo=int(minimo)
        except:
            print("Tiene que ser un número")
            pass 
        else:
            if int(minimo)>0:
                break
        sys.exit()
    return minimo

