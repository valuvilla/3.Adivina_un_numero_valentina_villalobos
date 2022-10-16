
import random
import sys

MIN=0
MAX=100


minimo=MIN
maximo=MAX

numero = random.randint(minimo, maximo)

print(numero)

nombre=''
def usuario(nombre):
    nombre=input("Usuario: ")
    print("hola {}, quiere juegar?".format(nombre))
    respuesta=input("A.Si o B.No")
    print("\n")
    for letra in respuesta:
      if letra=="a" or "A" or "si" or "Si":
        return intentos(numero)
      else:
        return ("HASTA LA PROXIMA, {}".format(nombre))
  
    return nombre

#definimos una función que cuente los intentos
def intentos(numero): 
  #Definimos una función que comparara el numero dado 
  def adivina_numero(numero):
      #Definimos el numero de intentos iniciales a 0
     intento = 0
     while True:
      #Creamos un bucle infinito

       #Pedimos por teclado un número
        intent=input("Intenta adivinar un número entero entre {} y {}: ".format(minimo, maximo))
        
       
       #Cada vez que entre en un bucle se sumara un intento
        intento = intento + 1
       
       #Controlamos las excepciones, en este caso cualquier resultado que no sea un numero o que sea un numero no comprendido en el intervalo dado
        try:
            intent = int(intent)
        except:
            print("Elemento no válido", file=sys.stderr)
            pass
        else:
            if minimo<=intent<=maximo:
              if int(intent)<numero:
                print("demasiado pequeño", "\n")

                
              elif int(intent)>numero:
               print("demasiado grande", "\n")

                
              else: 
                break
     
                sys.exit()  
                
      #condicional para mostrar los intentos finales y el fin de partida          
     if numero==intent:
       intento = str(intento)
       print("Has ganado" + "\n" + "¡Has adivinado el número en " + intento + " intento/s!"+ "\n"+ "FIN DE PARTIDA" )
    
  
  return adivina_numero(numero)

  #Para que se ejecute el código
if __name__ == "__main__":
  usuario(nombre)
        