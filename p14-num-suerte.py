# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. 
# Mostrar los dígitos individuales y el número de la suerte.

año = int(input('Dar el año de nacimiento: '))

mil = año // 1000
cien = año % 1000 // 100 # % es residuo ej 1997%1000 seria 997 division entera 100 seria 9
diez = año % 100 // 10
unidad = año % 1000 % 10

Numsuerte = mil + cien + diez + unidad 

print(f'El primer digito es {mil}, el segundo es {cien}, el tercer es {diez} y el cuarto es {unidad}')
print(f'El numero de la suerte es: {Numsuerte}')