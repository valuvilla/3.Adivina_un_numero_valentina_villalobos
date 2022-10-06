import random
import sys
numero = random.randint(0,100)
print(numero)
#P1: Captar un numero
while True:
  n2=input("Introduce un número entre 0 y 99: ")
  try:
    n2=int(n2)
  except:
    pass
  else:
    if 1 <= n2 <= 99:
      break
print("El número es válido") while True:
  