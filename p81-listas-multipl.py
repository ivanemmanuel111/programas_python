#Leer dos listas con 5 elementos
#• Multiplica las listas y guárdalos en una tercera lista
#• Imprime las tres listas
print('\nListas con 5 elementos')
c = 5 #Definimos que las listas sean de 5 elementos
print('\nElementos de la Lista 1:')
lista1=[]

for i in range(c):
      n = int(input(f'Lista1[{i}]: '))
      lista1.append(n)
print(f'\nLista1 : {lista1}')

print('\nElementos de la Lista 2:')
lista2=[]
for i in range(c):
      n = int(input(f'Lista2[{i}]: '))
      lista2.append(n)
print(f'\nLista2 : {lista2}')

print('\nLa multiplicacion de la Lista 1 y la Lista 2 entrega Lista 3')
lista3=[]
for i in range(c):
      lista3.append(lista1[i]*lista2[i])
print(f'\nLista1 : {lista1}')
print(f'\nLista2 : {lista2}')
print(f'\nLista3 : {lista3}')

#fin