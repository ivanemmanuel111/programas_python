# Suma de digitos
# 1971 entre 10 = 197.1
# Sobrante 1 + lo entero que es 197..sumamos todos los digitos y da 18

def sumadigitos(n):
   suma=0
   while n!=0:
    dig = n % 10 #Guardamos el sobrante
    suma = suma + dig
    n = n // 10 #Nos quedamos con lo entero
   return suma

n = int(input("Dame un numero y sumaré sus dígitos :? "))
res = sumadigitos(n)
print(f"La suma de los dígitos de {n} es {res}")
