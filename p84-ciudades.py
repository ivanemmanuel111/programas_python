#Leer n nombres de ciudades en una lista hasta introducir $
#Imprimir cuantos elementos son, y la lista completa
#Ordenar la lista en orden descendente y mostrar (sort)
#Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres

print("Introduce los nombres de las ciudades: $ pata terminar\n")
ciudades=[]
while True:
     ciudad=input("Ciudad: ")
     if ciudad=="$":
        break
     else:
        ciudades.append(ciudad)
print(f'Ciudades: {ciudades}')
print(f'Son {len(ciudades)} ciudades')

ciudades.sort(reverse=True) #Orden descentente de la lista (con sort)
print(f'Lista de ciudades en Forma descentente {ciudades}')

for ciudad in ciudades:
    if ciudad.startswith('Z'): #No pude utilizar el startswith, buscare como
       print (ciudad)
#print(ciudad.startswith('Z'))
