#Diseña un programa con una función que pida 3 números enteros y devuelva el menor de ellos, usando una
#función. (ver p100 - numero mayor)

def menor(c1,c2,c3):
  if c1<c2 and c1<c3:
    men = c1
  elif c2<c1 and c2<c3:
    men = c2
  elif c3<c1 and c3<c2:
    men = c3
  else:
    men = -1
  return men #Regresa

print("Dame 3 numeros")
c1,c2,c3 = float(input()), float(input()), float(input())

m = menor(c1,c2,c3)
if m == -1:
    print('Numeros iguales')
else:
    print(f'El menor es: {m} ')
print(f"El numero menor es: {menor(c1,c2,c3)}")