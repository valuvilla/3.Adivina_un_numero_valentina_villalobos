import random
import sys

print("Define los limites", "\n")
MIN=int(input('¿Cuál es el número más pequeño del intervalo?: '))
MAX=int(input('¿Cuál es el número más grande del intervalo? '))

n1 = random.randint(p,g)
n1= int(n1)
#print(n1)

#definimos una función que cuente los intentos
def intentos(n1): 
  #Definimos una función que comparara el numero dado 
  def adivina_numero(n1):
      #Definimos el numero de intentos iniciales a 0
     intento = 0
     while True:
      #Creamos un bucle infinito

       #Pedimos por teclado un número
        n2=input("Introduce un número entero entre " + str(MIN) + " y " + str(MAX) + ": ")
        
       
       #Cada vez que entre en un bucle se sumara un intento
        intento = intento + 1
       
       #Controlamos las excepciones, en este caso cualquier resultado que no sea un numero o que sea un numero no comprendido en el intervalo dado
        try:
            n2 = int(n2)
        except:
            pass
        else:
            if MIN<=n2<=MAX:
              if int(n2)<n1:
                print("demasiado pequeño", "\n")

                
              elif int(n2)>n1:
               print("demasiado grande", "\n")

                
              else: 
                break
     
                sys.exit()  
                
      #condicional para mostrar los intentos finales y el fin de partida          
     if n1==n2:
       intento = str(intento)
       print("Has ganado" + "\n" + "¡Has adivinado el número en " + intento + " intento/s!"+ "\n"+ "FIN DE PARTIDA" )
    
  
  return adivina_numero(n1)

  #Para que se ejecute el código
if __name__ == "__main__":
  intentos(n1)
        