# Imprime los numeros del 1 a n, o de n a 1

import os
os.system('cls')
op = int(input('[1] Ir arriba\n [2] Ir abajo? '))
if op==1:
    print('Imprimiendo hacia arriba ...')
    n = int(input('Hasta donde quieres llegar? '))
    i = int(input('Incrementos? '))
    for x in range(1, n+1, i): #controlamos los incrementos
        print(x, end=' ')

elif op==2:
    print('Imprimiendo hacia abajo ...')
    n = int(input('Desde donde quieres empezar? '))
    i = int(input('Decrementos? '))
    for x in range(n, 0, i):
        print(x, end=' ')