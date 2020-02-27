import sys 
from potencia import Potencia
user = sys.argv[1]
pot = sys.argv[2]
detalle = sys.argv[3]
print (user)
print (pot)
print (detalle)

operacion = Potencia(user,pot,detalle)
operacion.verificar()

