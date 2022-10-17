#Funciones que nos permite determinar la dificultad de la actividad.
 
def opciones():
    print(
        "Opción 1. Nivel 1",
        "Opción 2. Nivel 2",
        "Opción 3. Nivel 3",
        "Opción 4. Nivel 4"
    )

    opcion=input("INTRODUZCA OPCIÓN: ")

    #Dependiendo de la opcion elegida, variara el valor maximo del ramngo y el numero maximo de intentos
    if opcion=="1":
        MIN=0
        MAX1=100
        minimo=MIN
        maximo=MAX1
        intento_maximo=10
        

    elif opcion=="2":
        MIN=0
        MAX2=1000
        minimo=MIN
        maximo=MAX2
        intento_maximo=15
        

    elif opcion=="3":
        MIN=0
        MAX3=10**6
        minimo=MIN
        maximo=MAX3 
        intento_maximo=20

        
         
    else:
        MIN=0
        MAX4=10**12 
        minimo=MIN
        maximo=MAX4  
        intento_maximo=4
        
    
    return minimo, maximo, intento_maximo