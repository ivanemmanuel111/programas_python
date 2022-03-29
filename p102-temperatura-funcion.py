# Temperaturas
# Con dos funciones

def farenheit(temp):
   return ( temp * (9/5) ) +32

def centigrados(temp):
   return ( temp-32 ) * (5/9)

print('[ 1 ] Convertir a Farenheit')
print('[ 2 ] Convertir a Centigrados')
op = int(input("Elige? "))

if op==1 :
   print('Convertir a Farenheit')
   temp = int(input('Dame la temperatura en Centigrados? '))
   print(f'La temperatura en grados Farenheit es {farenheit(temp)}')
elif op==2:
   print('Convertir a Centigrados')
   temp = int(input('Dame una temperatura en Farenheit? '))
   print(f'La temperatura en grados Centigrados es {centigrados(temp)}')
   