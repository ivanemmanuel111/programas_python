#Generar 2 listas de 10 números aleatorios
#Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares
#Imprime las 3 listas

import random

l1 = []
l2 = []
l3 = []
c = 10 #10 numerps
print("Gener numeros aleatorios")

for n in range(c): #numeros aleatoeios
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))

print("\nListas:")
print(f"Lista 1 : {l1}")
print(f"Lista 2 : {l2}")

l1impar=[]
for e in l1:
    if e % 2 != 0:
       l1impar.append(e)
       
l2impar=[]
for e in l2:
    if e % 2 != 0:
       l2impar.append(e)
       

l3 = list(map(lambda x,y: x+y, l1impar,l2impar)) #Busque el como sumar las posiciones de la lista

print("\nListas numeros aleatorios impares:")
print(f"Lista 1 : {l1impar}")
print(f"Lista 2 : {l2impar}")
print(f"Lista 3 : {l3}")