import sys

from niveles.nivel1 import nivel1
from niveles.nivel2 import nivel2
from niveles.nivel3 import nivel3
from niveles.nivel4 import nivel4
 


def opciones():
    print(
        "Opción 1. Nivel 1",
        "Opción 2. Nivel 2",
        "Opción 3. Nivel 3",
        "Opción 4. Nivel 4"
    )

    opcion=input("INTRODUZCA OPCIÓN")

    if opcion=="1":
        minimo, maximo=nivel1()
        
    elif opcion==2:
        minimo, maximo=nivel2()
        
    elif opcion==3:
        minimo, maximo=nivel3()
         
    else:
       minimo, maximo=nivel4()

    return minimo, maximo