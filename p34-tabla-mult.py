# Tabla de multiplicar

while(True):
    t = int(input('Cual tabla quieres?'))
    c = 1
    while c <= 10:
        print(f'{c} x {t} = {c * t}')
        c += 1
    if input('Dseseas otra tabla (s/n) ?').upper()=='N' : break
print('Gracias')

