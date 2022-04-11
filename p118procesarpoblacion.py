#Programas de funciones

from operator import itemgetter

def imprime(poblacion, campo, ascdec):
   if campo!= '':
       poblacion = sorted(poblacion, key=itemgetter(campo), reverse=ascdec)
   print(f"{'pais':>15} {'poblacion_2018':>18} {'poblacion_2019':>15} {'poblacion_2020':>15} {'poblacion_2021':>15} ")
   for j in poblacion:
       print(f"{j['pais']:>15} {j['poblacion_2018']:>13} {j['poblacion_2019']:>13} {j['poblacion_2020']:>16} {j['poblacion_2021']:>16} ")



def valor_mayor(poblacion, campo):
   m = poblacion[0][campo]
   jm = [{}]
   for j in poblacion:
      if j[campo] > m:
          jm[0]=j
   return jm

def valor_menor(poblacion, campo):
   m = poblacion[0][campo]
   jm = [{}]
   for j in poblacion:
     if j[campo] < m:
          jm[0]=j
   return jm

def valor_promedio(poblacion, campo):
   s = 0
   for j in poblacion:
      s += j[campo]
   return s / len(poblacion)
