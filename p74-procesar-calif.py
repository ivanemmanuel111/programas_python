#Procesar calificaciones

#Entrada

print("Introduce calificaciones 0..9 (99 para parar):")
nums=[]
n=0
while n!=99:
    n = float(input("Dame calificacion > "))
    if n>=0 and n<=10:
        nums.append(n) ##metodo append
    else:
        print('x')
print('< fin')

# Calculos
suma = 0
for n in nums:
    suma = suma+n 

promedio = suma / len(nums)
mp=[]

for n in nums:
   if n>promedio :
       mp.append(n)

may=nums[0]
for n in nums:
     if n>may:
          may=n

men=nums[0]
for n in nums:
     if n<men:
          men=n

# Salida
print(f"\nCapturaste {len(nums)} numeros")
print(f"Los numeros son : {nums}")
print("\nEstadisticas >>")
print(f"Suma : {suma}")
print(f"Promedio : {promedio}")
print(f"Mayores promedio : {len(mp)} : {mp}")
print(f"Mayor : {may}")
print(f"Menor : {men}")