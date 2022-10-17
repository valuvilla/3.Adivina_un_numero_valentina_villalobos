import pickle

datos=[]

datos.append(input(":"))

ArchivoBinario=open("ArchivoLista", "wb")

pickle.dump(datos, ArchivoBinario)

ArchivoBinario.close()

Archivo2=open("ArchivoLista", "rb")

Lista2=pickle.load(Archivo2)

print(Lista2)