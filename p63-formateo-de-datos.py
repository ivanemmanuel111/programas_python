# formateo de datos
import os; os.system('cls')
nombre = 'Juan Carlos'
edad = 25
sueldo = 123.45686
tasa = .30

print(f'Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo:.2f} Tasa: {tasa:.2%}')
print('Nombre: {}, Edad: {}, Sueldo: {:.2f} Tasa: {:.2%}'.format(nombre,edad,sueldo,tasa))
print('Nombre: {3}, Edad: {2}, Sueldo: {1:.2f} Tasa: {0:.2%}'.format(tasa,sueldo,edad,nombre))

print('Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo:.2f} Tasa: {tasa:.2%}'.format(nombre='Maria Luisa',edad=33,sueldo=456.789,tasa=0.4))

print(f'\n{nombre:>30}\n{nombre:<30}\n{nombre:^30}')

print(f'\nDecimal: {edad:d}, Binario: {edad:b} Octal: {edad:o}, Hexadecimal: {edad:x}')

print('Decimal: {0:d}, Binario: {0:b} Octal: {0:o}, Hexadecimal: {0:x}\n'.format(edad))

print(f"{'Tabla de datos ':^45}")

print('-'*45)

print('{p1:<15}{p2:.^15}{p3:>15}'.format(p1='Nombre',p2='Edad',p3='Sueldo'))

print('-'*45)
for i in range(1,10):
    print(f'{nombre:<15}{edad+i:^15}{sueldo*i*i:>15,.2f}')
print('-'*45)

