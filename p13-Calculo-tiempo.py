# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos, considerando que:
# 1 día tiene 24 horas.
# 1 hora tiene 60 minutos.
# 1 minuto tiene 60 segundos.

horas = int(input('Dar la cantidad de horas: '))

dias = horas / 24
minutos = horas * 60
segundos = horas * 60 * 60

print(f'{horas} Horas son: {dias} días, {minutos} minutos y {segundos} segundos')
