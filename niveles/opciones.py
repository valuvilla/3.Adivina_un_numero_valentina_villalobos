import sys

valor=''
def pedir_numero(valor):
    while True:
        valor=input("Elige una opción: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
        else:
            break
            sys.exit()
    return valor

def opciones(valor):
    print(
        "Opción 1. Nivel 1",
        "Opción 2. Nivel 2",
        "Opción 3. Nivel 3",
        "Opción 4. Nivel 4"
    )

    opcion=pedir_numero(valor)

    if opcion==1:
        MIN=0
        MAX=10**2
        minimo=MIN
        maximo=MAX
        
    elif opcion==2:
        MIN=0
        MAX=10**3
        minimo=MIN
        maximo=MAX
        
    elif opcion==3:
        MIN=0
        MAX=10**6
        minimo=MIN
        maximo=MAX
         
    else:
        MIN=0
        MAX=10**12
        minimo=MIN
        maximo=MAX

    return minimo, maximo

print(opciones(valor))