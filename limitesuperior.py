import sys


def limite_sup():
    while True:
        maximo=input('¿Cuál es el número más grande del intervalo?: ')
        try:
             maximo=int(maximo)
        except:
            print("Tiene que ser un número")
            pass 
        else:
            if int(maximo)>0:
                break
        sys.exit()
    return maximo