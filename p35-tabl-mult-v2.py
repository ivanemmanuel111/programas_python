# Tabla de multiplicar V2

import os
while(True):
    os.system('cls') # limpiar pantalla
    t = int(input('Cual tabla quieres?'))
    n = int(input('hasta donde la quieres?'))
    c = 1
    while c <= n:
        print(f'{c} x {t} = {c * t}')
        c += 1
    if input('Dseseas otra tabla (s/n) ?').upper()=='N' : break
print('Gracias')