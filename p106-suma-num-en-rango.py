# Suma números en un rango
#programa
def suma_rango(ini, fin):
  s = 0
  for i in range(ini, fin+1):
    s = s + i # s+=1 es lo mismo
  return s

print('Dame un rango de valores a sumar')
ini = int(input('Dame inicio '))
fin = int(input('Dame fin '))
print(f'La suma del rango es {suma_rango(ini,fin)}')