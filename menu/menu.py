import sys

from nivel1 import nivel1
from nivel2 import nivel2
from nivel3 import nivel3
from nivel4 import nivel4
 
def opciones():
    print(
        "Opción 1. Nivel 1",
        "Opción 2. Nivel 2",
        "Opción 3. Nivel 3",
        "Opción 4. Nivel 4"
    )

    opcion=input("INTRODUZCA OPCIÓN: ")

    if opcion=="1":
        minimo, maximo, intento_maximo=nivel1()

    elif opcion=="2":
        minimo, maximo, intento_maximo=nivel2()
        

    elif opcion=="3":
        minimo, maximo, intento_maximo=nivel3()
        
         
    else:
        minimo, maximo, intento_maximo=nivel4()
        
    
    return minimo, maximo, intento_maximo