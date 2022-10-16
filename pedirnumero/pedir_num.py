import sys

from limites.limites import MIN1, MAX1


def pedir_numero(valor):
    while True:
        valor=input("Introduce un valor: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
        else:
            break
            sys.exit()
    return valor

def solicitar_intento(valor, minimo=MIN1, maximo=MAX1):
    invitacion="Adivine un número"
    while True:
        invitacion= "{} entre {} y {} incluídos".format(invitacion, minimo, maximo)
        print(invitacion)
        intento= pedir_numero(valor)
        try:
            minimo<=intento<=maximo
        except:
            print("{} no está entre {} y {}".format(intento,minimo,maximo ))
            pass
        else: 
            sys.exit()
            
print(solicitar_intento(minimo=MIN1, maximo=MAX1)) 
