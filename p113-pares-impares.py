# Pares e impares en una lista


def pares_impares(lista):
  p=[]
  i=[]
  for n in lista:
    if n % 2 == 0 : p.append(n)
    else: i.append(n)
  return p, i

def sumatodos(l1, l2):
  s = 0 
  for n in l1:
      s = s + n**2 
  for n in l2:
      s = s + n**2
  return s
# Programa principal
nums = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]

pares, impares = pares_impares(nums)
print(f'La numeros : {nums} -> {len(nums)}')
print(f'Los pares : {pares} -> {len(pares)}')
print(f'Los impares: {impares} -> {len(impares)}')

print(f'La suma de todos los elementos al cuadrado es {sumatodos(pares, impares)}')