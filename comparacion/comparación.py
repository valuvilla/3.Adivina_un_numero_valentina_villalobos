

import random

from niveles.opciones import minimo, maximo
from pedir_num import  solicitar_intento

def adivina_numero(dato, minimo=minimo, maximo=maximo):
    numero=random.randit(minimo, maximo)
    n_intentos=0
    while True:
        n_intentos+=1
        intento=solicitar_intento(dato, minimo, maximo)

        if intento<numero:
            print("demasiado pequeño", "\n")
            minimo=intento+1
            Victoria=False

        elif intento>numero:
            print("demasiado grande", "\n")
            maximo=intento+1
            Victoria=False

               
        else: 
            Victoria=True
            break

    return   Victoria, minimo, maximo
     
            