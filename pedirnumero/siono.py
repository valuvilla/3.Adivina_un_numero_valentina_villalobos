

import sys

SI=('si', 'Si', 'Yes', 'yes', 'verdadero', 'true', 1)
def desea_jugar():
    try:
        return input() in SI
    except:
        return False
        sys.exit()    