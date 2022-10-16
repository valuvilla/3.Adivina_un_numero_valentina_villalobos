
import random

from limites import MAX1, MIN1
from pedirnu

def adivina_numero(intento, minimo=MIN1, maximo=MAX1):
    numero=random.randit(minimo, maximo)
    n_intentos=0
    while intento!=numero:
        pedir_num.solicitar_intento(intento)
        n_intentos+=1
        if intento<numero:
            print("demasiado pequeño", "\n")
                
        elif intento>numero:
            print("demasiado grande", "\n")

                
        else: 
            break
     
            