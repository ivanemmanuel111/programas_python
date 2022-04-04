#Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos
#regrese la suma de números pares o impares en el rango de números especificados. Deberá́ mostrar un menú́ con
#las opciones correspondientes. (ver p106 suma rango)

def suma_impar(ini, fin):
  s = 0
  for i in range(ini, fin+1,2):
    print(i,end=' ')
    s += i
  return s
def suma_par(ini, fin):
  s = 0
  for i in range(ini+1, fin+1,2):
    print(i,end=' ')
    s += i
  return s
print('Dame un rango de valores a sumar')
ini = int(input('Dame inicio '))
fin = int(input('Dame fin '))

print('[ 1 ] Sumar impares')
print('[ 2 ] Sumar pares')
op = int(input("Elige? "))

if op==1:
   print('Sumar impares')
   print(f'La suma del rango es {suma_impar(ini,fin)}')
elif op==2:
   print('Sumar pares')
   print(f'La suma del rango es {suma_par(ini,fin)}')
