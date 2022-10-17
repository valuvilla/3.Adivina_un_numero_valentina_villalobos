
from entrada_datos import *
from menu.menu import *
from entrada_datos.pedir_num import *
from entrada_datos.siono import *



def jugar_partida():
    minimo, maximo = opciones()
    usuario=input("Usuario")
    while True:
        victoria, minimo, maximo, n_intentos = adivina_numero()

        if victoria==True:
            print("{}, has adivinado el número en {} intento/s!".format(usuario, n_intentos))
            break
    return usuario, n_intentos, minimo, maximo, victoria    
            

def jugar():
    while True:
        jugar_partida()
        if not desea_jugar("¿Desea volver a jugar?"):
            print("Hasta pronto")
            break




