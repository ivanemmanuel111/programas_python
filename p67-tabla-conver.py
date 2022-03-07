#El usuario introduce un rango de números, luego se le muestra una tabla de conversiones con 4 columnas
#alineadas: 1 numero decimal en alineación izquierda, 2 número hexadecimal en alineación centrada, 3 número
#octal en alineación izquierda, 4 binario en alineación derecha, el tamaño de cada columna debe ser uniforme y el
#título de la tabla debe centrarse en el ancho de la tabla.


numero_in = int(input('Dame el numero inicial: '))
numero_fn = int(input('Dame el numero final: '))


print(f"{'Tabla de conversiones ':^45}")
print('-'*45)
print('{de:<5}{he:.^16}{oc:.^14}{bi:>5}'.format(de='Decimal',he='Hexa',oc='Octal',bi='Binario'))
print('-'*45)
for x in range(numero_in, numero_fn +1, 1): #(1 empieza, 101 hasta, 1 incremento)
    bin = format(x, '0b') #binario
    hex = format(x, '0x') #hexadecimal
    oct = format(x, '0o') #octal
    print(f'{x:<4} {hex:^21} {oct:<7} {bin:>4}')
print('-'*45)
