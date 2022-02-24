# Hasta la tabla de multiplicar deseada y hasta donde el usiario lo pida
# anidar ciclos
t = int(input('Hasta que tabla Tabla? '))
n = int(input('Hasta donde quieres que llegue? '))

for x in range(1, t+1):
    print('-' *10)
    for r in range(1, n+1):
        print(f'{x} x {r} = {r*x}')
    print('-' *10)
    print(' ')