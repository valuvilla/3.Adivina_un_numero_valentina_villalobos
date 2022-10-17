
from tabulate import tabulate
import pickle

from entrada_datos.entrada import *

def jugar_partida():
    usuario=input("Usuario: ")
    tabla=[["Usuario","Intentos"]]
    while True:
        victoria, minimo, maximo, n_intentos, intento_maximo = adivina_numero()

        tabla.append([usuario, n_intentos])
    

        ArchivoBinario=open("ArchivoLista", "wb")

        pickle.dump(tabla, ArchivoBinario)


        ArchivoBinario.close()


        



        if n_intentos==intento_maximo or victoria==True:
            break
    print(tabulate(tabla))       
    return  minimo, maximo, victoria    
            

def jugar():
    while desea_jugar("Desea jugar: ")==True:
        jugar_partida()
    return "FIN DEL JUEGO"

