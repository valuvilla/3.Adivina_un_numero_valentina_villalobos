import pickle

from juego.juego import usuario, n_intentos
datos=[]
datos.append(usuario, n_intentos)

ArchivoBinario=open("ArchivoLista", "wb")

pickle.dump(datos, ArchivoBinario)

ArchivoBinario.close()

Archivo2=open("ArchivoLista", "rb")

Lista2=pickle.load(Archivo2)

print(Lista2)