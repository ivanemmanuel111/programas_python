# Imprime la tabla de multiplicar deseada hasta donde lo pida

t = int(input('Tabla? '))
n = int(input('Hasta donde quieres que llegue? '))
for r in range(1, n+1):
    print(f'{r} x {t} = {r*t}')