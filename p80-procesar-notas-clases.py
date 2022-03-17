#Leer n notas hasta introducir un 0
#• Las notas pueden estar entre 0 y 100 (validar)
#• Imprime:
#! cuantas notas, las notas,
#! suma, promedio,
#! notas menores al promedio y cuantas son
#! nota máxima y nota mínima

print("Introducir notas de 0 a 100 (0 para parar):")
nums=[]
n = 1
while n!=0:
    n = float(input("Dame nota > "))
    if n>=1 and n<=100:
        nums.append(n) ##metodo append
    else:
        print('sale del rango')
print('< fin')
suma = 0
for n in nums:
    suma = suma+n 

promedio = suma / len(nums)
mp=[]

for n in nums:
   if n<promedio :
       mp.append(n)
max=nums[0]
for n in nums:
     if n>max:
          max=n

min=nums[0]
for n in nums:
     if n<min:
          min=n
print(f"\nCapturaste {len(nums)} notas")
print(f"Las notas son : {nums}")
print(f"Suma : {suma}")
print(f"Promedio : {promedio}")
print(f"Menores al promedio : {len(mp)} : {mp}")
print(f"Nota Maxima : {max}")
print(f"Nota Minima : {min}")