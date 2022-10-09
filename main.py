import random
import sys


n1 = random.randint(0,100)
n1= int(n1)
print(n1)

#P1: Captar un numero
def adivina_numero(n1):
    while True:
      #Creamos un bucle infinito

      #Pedimos por pantalla un número
      n2=input("Introduce un número entero entre 0 y 99: ")
      try:
        n2=int(n2) and 0<=n2<=99
      except:
        pass
      if int(n2)<n1:
        print("demasiado pequeño")
      elif int(n2)>n1:
        print("Demasiado grande")
      else:
        print("has ganado")
        break
    print("lo hemos conseguido")  
    sys.exit()
    print("fin del juego")


    

    
  




if __name__=="__main__":
  adivina_numero(n1)
  