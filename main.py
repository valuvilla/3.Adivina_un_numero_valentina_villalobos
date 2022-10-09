import random
import sys



n1 = random.randint(0,100)
n1= int(n1)
print(n1)

#P1: Captar un numero
def intentos(n1): 
  def adivina_numero(n1): 
     
     while True:
      #Creamos un bucle infinito
        n2=input("Introduce un número entero entre 0 y 99: ")
        try:
            n2 = int(n2)
        except:
            pass
        else:
            if 0<=n2<=100:
              if int(n2)<n1:
                print("demasiado pequeño")
              elif int(n2)>n1:
               print("demasiado grande")
              else:
                print('¡has ganado!')
                print("Fin de partida")
                break
                sys.exit()    

       
       
  
  print(adivina_numero(n1))
  
if __name__ == "__main__":
  intentos(n1)
        