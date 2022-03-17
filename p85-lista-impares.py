#Llenar un lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
#Calcular e imprimir la suma y promedio de los números
#Mostrar los números que son divisibles entre 3 y sumarlos
#Pedir un elemento a buscar en la lista original y decir si esta y en que posición
l1 = []
s = int(input('Hasta que numero?(Toma el numero anterior) '))
for x in range(s):
    l1.append(x)

impares = [x for x in range(s) if x%2!=0] #entrega impares
print(impares)

suma = 0
for n in impares:
    suma = suma+n 

promedio = suma / len(impares)
mp=[]

for n in impares:
   if n<promedio :
       mp.append(n)
print(f"Suma : {suma}")
print(f"Promedio : {promedio}")

t = []
for n in impares:
    if(n%3==0):
        t.append(n)
print(f"Divisibles entre 3 : {t}")

suma3 = 0
for n in t:
    suma3 = suma3+n 
print(f"Suma de div entre 3 : {suma3}")


el = int(input('Dame un elemento de la lista '))
for j in range(len(l1)):
    if el == l1[j]:
        print(f'El elemento {el} se ha encontrado en la posicion {j} ')
        break
       
