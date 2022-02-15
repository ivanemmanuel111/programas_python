# Calcular funciones trigonometricas en python

import math

print('Calculando funciones trigonometricas...')
angulograd = int(input('Dame el angulo en grados'))
angulo = math.radianes(angulograd) # convierte a radianes
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
print(f'seno {seno}, coseno {coseno}, tangente {tangente}')

