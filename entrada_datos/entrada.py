import sys
import random

from entrada_menu.menu import *


def adivina_numero():
    #mediante la función opciones definimos el nivel de dificultad
    minimo, maximo, intento_maximo = opciones()
    #generamos aleatoriomente un numero a adivinar
    numero=random.randint(minimo, maximo)
    
    n_intentos=0
    #Bucle para evaluar el intento
    while n_intentos!=intento_maximo:
    
        n_intentos+=1
        #llamamos a la funcion solicitar intentos.
        intento= solicitar_intento(minimo, maximo, intento_maximo)

        if intento<numero:
            print("demasiado pequeño", "\n")
            #Acortara el rango
            minimo=intento+1
            print("Intento={}".format(n_intentos))
            victoria=False

        elif intento>numero:
            print("demasiado grande", "\n")
            print("Intento={}".format(n_intentos))
            #Acortara el rango
            maximo=intento-1
            victoria=False
               
        else: 
            print("Has ganado")
            print("Has adivinado el número en {} intento/s!".format(n_intentos))
            victoria=True
            break

    #en caso de no adivinar se mostara el  numero por pantalla
    if numero!=intento:
        print("El numero pensado era {}".format(numero))
         
        


    return   victoria, minimo, maximo, n_intentos, intento_maximo
    

#Funcion para evaluar que el numero dado por pantalla es un numero
def pedir_numero():
    while True:
        #Bucle infinito
        valor=input("Introduce un valor: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
        else:
            break
            sys.exit()
    return valor

#Funcion para evaluar  que el numero dado por pantalla esta en el rango dado
def solicitar_intento(minimo, maximo, intento_maximo):
    invitacion="Adivine un número"
    while True:
        #nucle infinito 


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
#Funciones que nos permite definir la cantidad de veces que queremos jugar
SI=('si', 'Si', 'Yes', 'yes', 'verdadero', 'true', '1', 'YES', 'SI', 'VERDADERO', 'TRUE')
def desea_jugar(invite):
    if input(invite) in SI:
        return True
    else:
        return False 
