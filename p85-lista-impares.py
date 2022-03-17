#Llenar un lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
#Calcular e imprimir la suma y promedio de los números
#Mostrar los números que son divisibles entre 3 y sumarlos
#Pedir un elemento a buscar en la lista original y decir si esta y en que posición

c = int(input('Cuantos elementos ? '))
print('\nLeyendo los elementos de la Lista 1:')
lista1=[]

for i in range(c):
      n = int(input(f'Lista1[{i}]: '))
      lista1.append(n)
print(f'\nLista1 : {lista1}')
