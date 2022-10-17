
from tabulate import tabulate
#Para crear una lista de valores persistentes
import pickle

from entrada_datos.__init__ import *

#funcion responsable de cada juego
def jugar_partida():
    usuario=input("Usuario: ")
    tabla=[["Usuario","Intentos"]]

    while True:

        #Nos permite jugar varias veces
        #bucle infinito

        #llamamos a la funcion que nos permite jugar

        victoria, minimo, maximo, n_intentos, intento_maximo = adivina_numero()

        #Intento de crear una tabla con los intentos
        tabla.append([usuario, n_intentos])
    

        ArchivoBinario=open("ArchivoLista", "wb")

        pickle.dump(tabla, ArchivoBinario)


        ArchivoBinario.close()


        

        #El bucle solo se rompera si se adivina el numero dentro de los intentos establecidos
        #o se acaban los intentos

        if n_intentos==intento_maximo or victoria==True:
            break
    print(tabulate(tabla))       
    return  minimo, maximo, victoria    
            

def jugar():
    while desea_jugar("Desea jugar: ")==True:
        jugar_partida()
    return "FIN DEL JUEGO"

