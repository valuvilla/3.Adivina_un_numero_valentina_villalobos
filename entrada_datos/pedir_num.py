import random
import sys
from menu.menu import *

def pedir_numero():
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

def solicitar_intento():
    minimo, maximo = opciones()
    invitacion="Adivine un número"
    while True:
        invitacion= "{} entre {} y {} incluídos".format(invitacion, minimo, maximo)
        print(invitacion)
        dato= pedir_numero()
        try:
            minimo<=dato<=maximo
        except:
            print("{} no está entre {} y {}".format(dato,minimo,maximo))
            pass
        else:
            break 
            sys.exit()
    
    return dato       

def IA():
    minimo, maximo=opciones()
    dato=random.randint(minimo,maximo)
    print("El numero elegido es el {}".fomat(dato))
    return dato

def jugador():
    jugador=input("¿Quién juega? \n A.Persona \n B.IA")
    for letra in jugador:
        if letra=="a" or "A":
            dato=solicitar_intento
        if letra=="b" or "B":
            dato=IA()
    return dato        

