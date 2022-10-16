

import random


from limites.limites import MAX1, MIN1
from pedir_num import  solicitar_intento

def adivina_numero(dato, minimo=MIN1, maximo=MAX1):
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
            
    return   n_intentos
     
            