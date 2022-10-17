import sys
import random

from menu.menu import *


def adivina_numero():
    minimo, maximo, intento_maximo = opciones()
    numero=random.randint(minimo, maximo)
    n_intentos=0
    while n_intentos!=intento_maximo:
    
        n_intentos+=1
        intento= solicitar_intento(minimo, maximo, intento_maximo)

        if intento<numero:
            print("demasiado pequeño", "\n")
            minimo=intento+1
            print("Intento={}".format(n_intentos))
            victoria=False

        elif intento>numero:
            print("demasiado grande", "\n")
            print("Intento={}".format(n_intentos))
            maximo=intento-1
            victoria=False
               
        else: 
            print("Has ganado")
            print("Has adivinado el número en {} intento/s!".format(n_intentos))
            victoria=True
            break
        
    if numero!=intento:
        print("El numero pensado era {}".format(numero)) 
        no_intento=True 


    return   victoria, minimo, maximo, n_intentos, intento_maximo
    


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

def solicitar_intento(minimo, maximo, intento_maximo):
    invitacion="Adivine un número"
    while True:
        invitacion= "{} entre {} y {} incluídos. Tiene como maximo {} intentos".format(invitacion, minimo, maximo, intento_maximo)
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

""""
def IA(minimo, maximo, intento_maximo):
    dato=random.randint(minimo,maximo)
    print("El numero elegido es el {}".format(dato))
    return dato


def jugador(minimo, maximo, intento_maximo):
    while True:
        jugador=input("¿Quién juega? \n A.Persona \n B.IA \n")
        for letra in jugador:
            if letra=="a" or "A":
                dato=solicitar_intento(minimo, maximo, intento_maximo)
                break
    
            if letra=="b" or "B":
                dato=IA(minimo, maximo, intento_maximo)
                break
        
        break
        break
    

    return dato     
"""

SI=('si', 'Si', 'Yes', 'yes', 'verdadero', 'true', '1', 'YES', 'SI', 'VERDADERO', 'TRUE')
def desea_jugar(invite):
    if input(invite) in SI:
        return True
    else:
        return False 
