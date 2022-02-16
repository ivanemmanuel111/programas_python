# Se desea calcular el volumen de un cilindro dado su radio y altura, usando la siguiente formula:
# Volumen = PI * (Radio * Radio) * Altura

import math

Radio = float(input('Dar radio: '))
Altura = float(input('Dar altura: '))

Volumen = math.pi * (Radio * Radio) * Altura

print(f'El volumen del cilindro es: {Volumen}')
