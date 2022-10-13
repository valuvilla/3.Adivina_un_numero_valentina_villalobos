
import sys

from definirlimites import minimo, maximo
minimo, maximo

print("Hola")

def pedir_numero(invitacion):

    invitacion+= '{} entre {} y {}'.format(invitacion, minimo, maximo)

    while True:
        numero=input("Introduce un número")
        try:
            numero = int(numero)
        except:
            print("Elemento no válido", file=sys.stderr)
            pass
        else:
            if minimo<=numero<=maximo:
                break   
            sys.exit()


    
