# Dividir un numero de tres cifras
# 345 3 centenas. 4 decenas y 5 unidades

numero = int(input('Dame un numero de 3 cifras'))
centenas = numero // 100
decenas = numero - (centenas * 100) // 10
unidades = numero - (centenas * 100 + decenas * 10)

print(f'El numero {numero}')
print(f'Centenas: {centenas}')
print(f'Decenas: {decenas}')
print(f'Unidades: {unidades}')