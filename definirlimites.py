
import sys

from limitesuperior import limite_sup
limite_sup()

from limitesinferior import limite_inf
limite_inf()

def definir_limites(minimo,maximo):

    while True:
        print("Definir limites")
        limite_inf(minimo)
        limite_sup(maximo)
        try:
            int(maximo)>int(maximo)
        except:
            print("El valor mínimo {} es mayor que el valor máximo {}".format(minimo, maximo))
        else:
            break
        sys.exit()

    return maximo, minimo

print(definir_limites(minimo,maximo))


