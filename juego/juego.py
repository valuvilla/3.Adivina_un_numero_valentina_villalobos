
from comparacion import *
from menu.menu import *
from pedirnumero.pedir_num import *
from siono import desea_jugar


def jugar_partida():
    minimo, maximo = opciones()
    usuario=input("Usuario")
    while True:
        victoria, minimo, maximo = adivina_numero()

        if victoria==True:
            n_intentos = str(n_intentos)
            print("Has ganado")
            print("{}, has adivinado el número en {} intento/s!".format(usuario, n_intentos))
            
            break
    return usuario, n_intentos, minimo, maximo, victoria    
            

def jugar():
    while True:
        jugar_partida()
        if not desea_jugar("¿Desea volver a jugar?"):
            print("Hasta pronto")
            break




