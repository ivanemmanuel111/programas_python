# Procesar calificaciones v2
nums=[]
print("Introduce calificaciones 0..9 (99 para terminar):")
n=0
while n!=99:
      n = float(input("Dame calificaciones > "))
      if n>=0 and n<=10:
        nums.append(n)
      else:
        print('x')
print('< fin')
suma = sum(nums)
promedio = suma / len(nums)
mp = [n for n in nums if n>promedio]
print(f"\nCapturaste {len(nums)} numeros")
print(f"Las numeros son : {nums}")
print("\nEstadisticas >>")
print(f"Suma : {suma}")
print(f"Promedio : {promedio}")
print(f"Mayores promedio : {len(mp)} : {mp}")
print(f"Mayor : {max(nums)}")
print(f"Menor : {min(nums)}")