# Tabla de conversion a dolar

tc = 20.15
pi = float(input('Valor inicial :'))
pf = float(input('Valor final :'))
c = pi
print('\n Pesos\tdolar') #\t
print('-'*15)
while c <= pf:
    print(f'{c}\t {c/tc:.2f}')
    c += 1
print('-'*15)
