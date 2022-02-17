# Convertir una'' temperatura de centigrados a farenheit y viceversa

print('Convirtiendo una temperatura centigrados a farenheit y viceversa ...')
print('[C] centigrados ')
print('[F] farenheit')
print('Elige una opcion')

opcion = str.upper(input())
if opcion == 'C' :
    print('\nConvirtiendo a grados centigrados ...')
    temp = float(input('Grados Farenheit ?'))
    res = (temp-32) * 5 / 9
    print(f'{temp} grados farenheit, equivale a {res} grados centigrados')
else :
    print('\nConvirtiendo a grados farenheit ...')
    temp = float(input('Grados centigrados ?'))
    res = (temp * 9/5) + 32
    print(f'{temp} grados centigrados, equivale a {res} grados farenheit')
print('\nGracias por utilizar este programa ...')
