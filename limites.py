import sys


maximo=MAX
minimo=MIN

def limites():
    while True:
        print("Define los limites", "\n")

        minimo=input('¿Cuál es el número más pequeño del intervalo?: ')
        maximo=input('¿Cuál es el número más grande del intervalo? ')

        try:
            minimo=int(minimo)
            maximo=int(maximo)
        except:
            print("Tiene que ser un número")
            pass
        else:
            if int(minimo)<int(maximo):
                break
        sys.exit()
        
    return maximo, minimo     


