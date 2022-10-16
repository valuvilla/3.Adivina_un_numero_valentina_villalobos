
from importlib import import_module
import random


#from limites.limites import limites
from pedir_num import pedir_numero

def adivina_numero(dato, minimo=0, maximo=100):
    numero=random.randit(minimo, maximo)
    n_intentos=0
    while True:
        n_intentos+=1
        intento=pedir_numero.pedir_num.pedir_numero.solicitar_intento(dato, minimo, maximo)

        if intento<numero:
            print("demasiado pequeño", "\n")
            minimo=intento+1
                
        elif intento>numero:
            print("demasiado grande", "\n")
            maximo=intento+1

               
        else: 
            break
            
    return   n_intentos
     
            