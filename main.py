import random
import sys
n1=1
#n1=random.randint(0,100)
while True:
  n2=input("introduce un número: ")
  try:
    n2=int(n2)
  except:
    pass
else:
  try:
    n2=n1
  except:
    if n2<n1:
      print('Demasiado pequeño')
    else:
      print('f')
            # Tenemos lo que queremos, de modo que salimos del bucle
            break

print('¡ha ganado!')
sys.exit()
random.exit()