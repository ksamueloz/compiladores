import sys 
from potencia import Potencia
print(sys.argv)
user = sys.argv[1]
pot = sys.argv[2]
detalle = sys.argv[3]
user = {i for i in user.replace('{','').replace('}','').split(',')}
pot = {i for i in pot}
print (user)
print (pot)
print (detalle)

operacion = Potencia(user,pot,detalle)
operacion.verificar()

