#Procesar datos fifa
#Nombre sin guiones
#Si

from operator import itemgetter

def imprime(fifa, campo, ascdec):
   if campo!= '':
       fifa = sorted(fifa, key=itemgetter(campo), reverse=ascdec)
   print(f"{'Id':>6} {'Nombre':<35} {'Valeuros':>10} {'Edad':>4} {'Peso':>4} {'Nacionalidad':<15}")
   for j in fifa:
       print(f"{j['id']:>6} {j['nombre']:<35} {j['valeuros']:>10} {j['edad']:>4} {j['peso']:>4} {j['nacionalidad']:<15}")



def valor_mayor(fifa, campo):
   m = fifa[0][campo]
   jm = [{}]
   for j in fifa:
      if j[campo] > m:
          jm[0]=j
   return jm

def valor_menor(fifa, campo):
   m = fifa[0][campo]
   jm = [{}]
   for j in fifa:
     if j[campo] < m:
          jm[0]=j
   return jm

def valor_promedio(fifa, campo):
   s = 0
   for j in fifa:
      s += j[campo]
   return s / len(fifa)


