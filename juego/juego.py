
from comparacion import adivina_numero, numero, intento
from main import usuario
from niveles.opciones import opciones, minimo, maximo
from pedirnumero.pedir_num import valor
import siono

def jugar_partida(minimo, maximo):
    usuario=input("Usuario")
    opciones(valor)
    while True:
        victoria, minimo, maximo = adivina_numero(numero,minimo, maximo )
        
        if victoria==True:
            n_intentos= str(n_intentos)
            print("Has ganado")
            print("{}, has adivinado el número en {} intento/s!".format(usuario, n_intentos))
            
            break
    return usuario, n_intentos, minimo, maximo, victoria    
            

def jugar(numero):
    while True:
        jugar_partida(valor, numero, minimo, maximo)
        if not siono("¿Desea volver a jugar?"):
            print("Hasta pronto, {}!".format(usuario))
            break



