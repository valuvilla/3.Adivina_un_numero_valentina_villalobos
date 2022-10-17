

import random
from entrada_datos.pedir_num import *
from menu.menu import *

def adivina_numero():
    minimo, maximo, intento_maximo = opciones()
    numero=random.randit(minimo, maximo)
    n_intentos=0
    while n_intentos!=intento_maximo:
    
        n_intentos+=1
        intento=jugador()

        if intento<numero:
            print("demasiado pequeño", "\n")
            minimo=intento+1
            victoria=False

        elif intento>numero:
            print("demasiado grande", "\n")
            maximo=intento-1
            victoria=False
               
        else: 
            print("Has ganado")
            victoria=True
            break
        
    if numero!=intento:
        print("El numero pensado era {}".formar(numero))    


    return   victoria, minimo, maximo, n_intentos
    


